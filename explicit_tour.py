import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
# import sklearn
import pandas as pd
from numpy.linalg import solve


def train_test_split(ratings):
    test = np.zeros(ratings.shape)
    train = ratings.copy()
    for user in range(ratings.shape[0]):
        test_ratings = np.random.choice(ratings[user, :].nonzero()[0],
                                        0.2 * len(ratings[user, :].nonzero()[0]),
                                        replace=False)
        train[user, test_ratings] = 0.
        test[user, test_ratings] = ratings[user, test_ratings]

    # Test and training are truly disjoint
    assert (np.all((train * test) == 0))
    return train, test


def get_mse(pred, actual):
    # Ignore nonzero terms.
    pred = pred[actual.nonzero()].flatten()
    actual = actual[actual.nonzero()].flatten()
    return mean_squared_error(pred, actual)

class ExplicitMF:
    def __init__(self, ratings, n_factors=40, learning='sgd', item_fact_reg=0.01, user_fact_reg=0.01,
                 item_bias_reg=0.01, user_bias_reg=0.01, verbose=False):
        """
        Train a matrix factorization model to predict empty
        entries in a matrix. The terminology assumes a
        ratings matrix which is ~ user x item

        Params
        ======
        ratings : (ndarray)
            User x Item matrix with corresponding ratings

        n_factors : (int)
            Number of latent factors to use in matrix
            factorization model
        learning : (str)
            Method of optimization. Options include
            'sgd' or 'als'.

        item_fact_reg : (float)
            Regularization term for item latent factors

        user_fact_reg : (float)
            Regularization term for user latent factors

        item_bias_reg : (float)
            Regularization term for item biases

        user_bias_reg : (float)
            Regularization term for user biases

        verbose : (bool)
            Whether or not to printout training progress
        """

        self.ratings = ratings
        self.n_users, self.n_items = ratings.shape
        self.n_factors = n_factors
        self.item_fact_reg = item_fact_reg
        self.user_fact_reg = user_fact_reg
        self.item_bias_reg = item_bias_reg
        self.user_bias_reg = user_bias_reg
        self.learning = learning
        if self.learning == 'sgd':
            self.sample_row, self.sample_col = self.ratings.nonzero()
            self.n_samples = len(self.sample_row)
        self._v = verbose

    def als_step(self,
                 latent_vectors,
                 fixed_vecs,
                 ratings,
                 _lambda,
                 type='user'):
        """
        One of the two ALS steps. Solve for the latent vectors
        specified by type.
        """
        if type == 'user':
            # Precompute
            YTY = fixed_vecs.T.dot(fixed_vecs)
            lambdaI = np.eye(YTY.shape[0]) * _lambda

            for u in range(latent_vectors.shape[0]):
                latent_vectors[u, :] = solve((YTY + lambdaI),
                                             ratings[u, :].dot(fixed_vecs))
        elif type == 'item':
            # Precompute
            XTX = fixed_vecs.T.dot(fixed_vecs)
            lambdaI = np.eye(XTX.shape[0]) * _lambda

            for i in range(latent_vectors.shape[0]):
                latent_vectors[i, :] = solve((XTX + lambdaI),
                                             ratings[:, i].T.dot(fixed_vecs))
        return latent_vectors

    def train(self, n_iter=10, learning_rate=0.1):
        """ Train model for n_iter iterations from scratch."""
        # initialize latent vectors
        self.user_vecs = np.random.normal(scale=1. / self.n_factors, \
                                          size=(self.n_users, self.n_factors))
        self.item_vecs = np.random.normal(scale=1. / self.n_factors,
                                          size=(self.n_items, self.n_factors))

        if self.learning == 'als':
            self.partial_train(n_iter)
        elif self.learning == 'sgd':
            self.learning_rate = learning_rate
            self.user_bias = np.zeros(self.n_users)
            self.item_bias = np.zeros(self.n_items)
            self.global_bias = np.mean(self.ratings[np.where(self.ratings != 0)])
            self.partial_train(n_iter)

    def partial_train(self, n_iter):
        """
        Train model for n_iter iterations. Can be
        called multiple times for further training.
        """
        ctr = 1
        while ctr <= n_iter:
            if ctr % 10 == 0 and self._v:
                print('\tcurrent iteration: {}'.format(ctr))
            if self.learning == 'als':
                self.user_vecs = self.als_step(self.user_vecs,
                                               self.item_vecs,
                                               self.ratings,
                                               self.user_fact_reg,
                                               type='user')
                self.item_vecs = self.als_step(self.item_vecs,
                                               self.user_vecs,
                                               self.ratings,
                                               self.item_fact_reg,
                                               type='item')
            elif self.learning == 'sgd':
                self.training_indices = np.arange(self.n_samples)
                np.random.shuffle(self.training_indices)
                self.sgd()
            ctr += 1

    def sgd(self):
        for idx in self.training_indices:
            u = self.sample_row[idx]
            i = self.sample_col[idx]
            prediction = self.predict(u, i)
            e = (self.ratings[u, i] - prediction)  # error

            # Update biases
            self.user_bias[u] += self.learning_rate * \
                                 (e - self.user_bias_reg * self.user_bias[u])
            self.item_bias[i] += self.learning_rate * \
                                 (e - self.item_bias_reg * self.item_bias[i])

            # Update latent factors
            self.user_vecs[u, :] += self.learning_rate * \
                                    (e * self.item_vecs[i, :] - \
                                     self.user_fact_reg * self.user_vecs[u, :])
            self.item_vecs[i, :] += self.learning_rate * \
                                    (e * self.user_vecs[u, :] - \
                                     self.item_fact_reg * self.item_vecs[i, :])

    def predict(self, u, i):
        """ Single user and item prediction."""
        if self.learning == 'als':
            return self.user_vecs[u, :].dot(self.item_vecs[i, :].T)
        elif self.learning == 'sgd':
            prediction = self.global_bias + self.user_bias[u] + self.item_bias[i]
            # 加上一个视觉特征
            prediction += self.user_vecs[u, :].dot(self.item_vecs[i, :].T)
            return prediction

    def predict_all(self):
        """ Predict ratings for every user and item."""
        predictions = np.zeros((self.user_vecs.shape[0],
                                self.item_vecs.shape[0]))
        for u in range(self.user_vecs.shape[0]):
            for i in range(self.item_vecs.shape[0]):
                predictions[u, i] = self.predict(u, i)

        return predictions

    def calculate_learning_curve(self, iter_array, test, learning_rate=0.1):
        """
        Keep track of MSE as a function of training iterations.

        Params
        ======
        iter_array : (list)
            List of numbers of iterations to train for each step of
            the learning curve. e.g. [1, 5, 10, 20]
        test : (2D ndarray)
            Testing dataset (assumed to be user x item).

        The function creates two new class attributes:

        train_mse : (list)
            Training data MSE values for each value of iter_array
        test_mse : (list)
            Test data MSE values for each value of iter_array
        """
        iter_array.sort()
        self.train_mse = []
        self.test_mse = []
        iter_diff = 0
        for (i, n_iter) in enumerate(iter_array):
            if self._v:
                print('Iteration: {}'.format(n_iter))
            if i == 0:
                self.train(n_iter - iter_diff, learning_rate)
            else:
                self.partial_train(n_iter - iter_diff)

            predictions = self.predict_all()

            self.train_mse += [get_mse(predictions, self.ratings)]
            self.test_mse += [get_mse(predictions, test)]
            if self._v:
                print('Train mse: ' + str(self.train_mse[-1]))
                print('Test mse: ' + str(self.test_mse[-1]))
            iter_diff = n_iter


# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.set()
def plot_learning_curve(iter_array, model):
    plt.plot(iter_array, model.train_mse, \
             label='Training', linewidth=5)
    plt.plot(iter_array, model.test_mse, \
             label='Test', linewidth=5)

    plt.xticks(fontsize=16);
    plt.yticks(fontsize=16);
    plt.xlabel('iterations', fontsize=30);
    plt.ylabel('MSE', fontsize=30);
    plt.legend(loc='best', fontsize=20);
    plt.show()

if __name__ == "__main__":
    np.random.seed(0)
    # Load data from disk
    # idx  poiID  seqID  userID poiTheme  visitDuration  avgDuration
    # df = pd.read_csv("E:/R_WorkSpace/TourCodes_assistant/result_data/Buda/buda_dfVisitTimes.csv", sep=';')
    # df = pd.read_csv("E:/R_WorkSpace/TourCodes_assistant/result_data/Edinburgh/edin_dfVisitTimes.csv", sep=';')
    df = pd.read_csv("E:/R_WorkSpace/TourCodes_assistant/result_data/Vien/vien_dfVisitTimes.csv", sep=';')
    # df = pd.read_csv("E:/R_WorkSpace/TourCodes_assistant/result_data/Toronto/toronto_dfVisitTimes.csv", sep=';')

    df.head()

    # print(df.head())
    # for row in df.itertuples():
    #    print(row[0],row[6],row[7])

    # unique users and pois
    users = df.userID.unique()
    items = df.poiID.unique()

    n_users = users.shape[0]
    n_items = items.shape[0]

    # map user name to user id
    uname_2_uid = {}
    uid_2_uname = {}
    iname_2_iid = {}
    iid_2_iname = {}
    ucount = 0
    icount = 0
    for i in range(n_users):
        uname_2_uid[users[i]] = ucount
        ucount = ucount + 1

    for j in range(n_items):
        iname_2_iid[items[j]] = icount
        icount = icount + 1

    # change the key and value of dict
    for key in uname_2_uid:
        value = uname_2_uid[key]
        uid_2_uname[value] = key

    for key in iname_2_iid:
        value = iname_2_iid[key]
        iid_2_iname[value] = key

    # Go from dataframe to likes matrix
    # Also, build index to ID mappers.
    # explicit
    # print(iname_2_iid[30])
    likes = np.zeros((n_users, n_items))
    count = 0
    for row in df.itertuples():
        # count = count + 1
        # print(count)
        uname = row[3]
        iname = row[1]
        print(iname)
        likes[uname_2_uid[uname], iname_2_iid[iname]] = float(row[5]) / float(row[6])

    MF_SGD = ExplicitMF(likes, 40, learning='sgd', verbose=True)
    iter_array = [1, 2, 5, 10, 25, 50, 100, 200, 300, 500, 800]
    #     iter_array = [1, 2, 5]
    MF_SGD.calculate_learning_curve(iter_array, likes, learning_rate=0.001)
    predictions = MF_SGD.predict_all()

    # 转为explicit.cvs存储
    # idx_to_rid_df = pd.DataFrame.from_dict(idx_to_rid,orient="index")
    # idx_to_cid_df = pd.DataFrame.from_dict(idx_to_cid,orient="index")

    list1 = []

    for x in range(predictions.shape[0]):
        for y in range(predictions.shape[1]):
            list1.append([uid_2_uname[x], iid_2_iname[y], predictions[x, y]])

    dfVisitTimesPred = pd.DataFrame(list1)
    dfVisitTimesPred.columns = ['userID', 'poiID', 'interest']

    dfVisitTimesPred.to_csv('C:/Users/RonnieXu/Desktop/vien_dfVisitTimesPred.csv')
    # dfVisitTimesPred.to_csv('C:/Users/RonnieXu/Desktop/edin_dfVisitTimesPred.csv')
    # dfVisitTimesPred.to_csv('C:/Users/RonnieXu/Desktop/buda_dfVisitTimesPred.csv')
    # dfVisitTimesPred.to_csv('C:/Users/RonnieXu/Desktop/toronto_dfVisitTimesPred.csv')



    # plot_learning_curve(iter_array, MF_SGD)
    print(iter_array)
    print(MF_SGD.test_mse)

