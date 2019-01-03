import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score, recall_score
from imblearn.over_sampling import SMOTE
import matplotlib.pyplot as plt

np.random.seed(100)

x_tr = pd.read_csv('x_tr.csv', index_col=0)
y_tr = np.array(pd.read_csv('y_tr.csv', header=None).iloc[:, -1])
x_te = pd.read_csv('x_te.csv', index_col=0)
y_te = np.array(pd.read_csv('y_te.csv', header=None).iloc[:, -1])

tree_model = DecisionTreeClassifier()

log_reg_model = LogisticRegression()

knn_model = KNeighborsClassifier()

models_list = [log_reg_model, knn_model, tree_model]

sen, spe = [[],[],[]], [[],[],[]]

print('Original')
for j, model in enumerate(models_list):
    print(str(model))
    model.fit(x_tr, y_tr)
    predictions = model.predict(x_te)
    print("accuracy: " + str(accuracy_score(predictions, y_te)))
    conf_mat = confusion_matrix(y_te, predictions)
    sen[j].append(conf_mat[1, 1] / np.sum(conf_mat[1, :]))
    spe[j].append(conf_mat[0, 0] / np.sum(conf_mat[0, :]))
    print('sensitivity: ' + str(conf_mat[1, 1] / np.sum(conf_mat[1, :])))
    print('specifity: ' + str(conf_mat[0, 0] / np.sum(conf_mat[0, :])))
    print('*' * 100)

print('Smote')
sm = SMOTE()
x_res, y_res = sm.fit_resample(x_tr, y_tr)
for j, model in enumerate(models_list):
    print(str(model))
    model.fit(x_res, y_res)
    predictions = model.predict(x_te)
    print("accuracy: " + str(accuracy_score(predictions, y_te)))
    conf_mat = confusion_matrix(y_te, predictions)
    sen[j].append(conf_mat[1, 1] / np.sum(conf_mat[1, :]))
    spe[j].append(conf_mat[0, 0] / np.sum(conf_mat[0, :]))
    print('sensitivity: ' + str(conf_mat[1, 1] / np.sum(conf_mat[1, :])))
    print('specifity: ' + str(conf_mat[0, 0] / np.sum(conf_mat[0, :])))
    print('*' * 100)

print('Up sampling')
non_zero_ind = np.nonzero(y_tr)
y_res = y_tr
x_res = x_tr
while y_res.mean() < 0.5:
    observation_to_add_ind = non_zero_ind[np.random.randint(len(non_zero_ind))]
    x_res = np.concatenate([x_res, x_tr.iloc[observation_to_add_ind, :]])
    y_res = np.concatenate([y_res, y_tr[observation_to_add_ind]])

for j, model in enumerate(models_list):
    print(str(model))
    model.fit(x_res, y_res)
    predictions = model.predict(x_te)
    print("accuracy: " + str(accuracy_score(predictions, y_te)))
    conf_mat = confusion_matrix(y_te, predictions)
    sen[j].append(conf_mat[1, 1] / np.sum(conf_mat[1, :]))
    spe[j].append(conf_mat[0, 0] / np.sum(conf_mat[0, :]))
    print('sensitivity: ' + str(conf_mat[1, 1] / np.sum(conf_mat[1, :])))
    print('specifity: ' + str(conf_mat[0, 0] / np.sum(conf_mat[0, :])))
    print('*' * 100)

print('Down sampling')
zero_ind = np.nonzero(y_tr == 0)[0]
to_keep_ind = np.random.permutation(zero_ind)[:np.sum(y_tr)]
ones_ind = np.nonzero(y_tr)[0]
y_res = np.concatenate([y_tr[to_keep_ind], y_tr[ones_ind]])
x_res = np.concatenate([x_tr.iloc[to_keep_ind, :], x_tr.iloc[ones_ind, :]])

for j, model in enumerate(models_list):
    print(str(model))
    model.fit(x_res, y_res)
    predictions = model.predict(x_te)
    print("accuracy: " + str(accuracy_score(predictions, y_te)))
    conf_mat = confusion_matrix(y_te, predictions)
    sen[j].append(conf_mat[1, 1] / np.sum(conf_mat[1, :]))
    spe[j].append(conf_mat[0, 0] / np.sum(conf_mat[0, :]))
    print('sensitivity: ' + str(conf_mat[1, 1] / np.sum(conf_mat[1, :])))
    print('specifity: ' + str(conf_mat[0, 0] / np.sum(conf_mat[0, :])))
    print('*' * 100)


def plot_bar_graphs(models_list, sen, spe):
    """Plot two bar graphs side by side, with letters as x-tick labels.
    """


    models_num = len(models_list)
    x = np.arange(len(spe[0]))
    width = 0.25
    titles = ['Logistic Regression','KNN','Decision Tree']
    for i in range(models_num):
        plt.figure()
        axes = plt.axes()
        model_spe = spe[i]
        model_sen = sen[i]
        axes.bar(x, model_spe, width)
        axes.bar(x + width, model_sen, width, color='C2')
        axes.legend(['specifity','sensitivity'])
        axes.set_xticks(x + width)
        axes.set_xticklabels(['orig', 'SMOTE', 'upsample', 'downsample'])
        plt.title(titles[i])
    plt.show()


plot_bar_graphs(models_list, sen, spe)
