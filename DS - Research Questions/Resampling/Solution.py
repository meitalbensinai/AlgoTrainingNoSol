import pandas as pd
import numpy as np
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

np.random.seed(100)

df = pd.read_csv('german.data-numeric', header=None, sep="\s+|\t+|\s+\t+|\t+\s+")

feature_names = []
for i in range(1, 25):
    feature_names.append("feature" + str(i))
feature_names.append('target')
df.columns = feature_names
print(df.head())
print(df.shape)

from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.model_selection import KFold, RepeatedKFold
from sklearn.utils import resample
from sklearn.metrics import accuracy_score

y = df['target']
X = df.drop(columns='target')
X_train, X_test, y_train, y_test = train_test_split(np.array(X), np.array(y), stratify=y, test_size=0.2)
model = SVC()
c_vector = list(range(-2, 8, 1))
# c_vector = list(range(-2, 0, 1))
c_vector = [2**c for c in c_vector]
k_means = np.zeros(len(c_vector))
kr_means = np.zeros(len(c_vector))
bt_means = np.zeros(len(c_vector))
k_stds = np.zeros(len(c_vector))
kr_stds = np.zeros(len(c_vector))
bt_stds = np.zeros(len(c_vector))

for i, c in enumerate(c_vector):

    ## k fold
    kf = KFold(n_splits=10)
    acc = []
    for train_ind, val_ind in kf.split(X_train):
        model = SVC(C=c)
        model.fit(X_train[train_ind], y_train[train_ind])
        acc.append(accuracy_score(y_train[val_ind], model.predict(X_train[val_ind])))
    k_means[i] = np.mean(np.array(acc))
    k_stds[i] = np.std(np.array(acc))

    ## k fold repeated
    rkf = RepeatedKFold(n_splits=10, n_repeats=50)
    acc = []
    for train_ind, val_ind in rkf.split(X_train):
        model = SVC(C=c)
        model.fit(X_train[train_ind], y_train[train_ind])
        acc.append(accuracy_score(y_train[val_ind], model.predict(X_train[val_ind])))
    kr_means[i] = np.mean(np.array(acc))
    kr_stds[i] = np.std(np.array(acc))

    ## bootstrapped
    acc = []
    for j in range(50):
        indices = np.arange(len(X_train))
        bagged_ind = resample(indices,replace=True)
        oob_ind = [x for x in indices if x not in bagged_ind]
        bagged_X,bagged_y = X_train[bagged_ind],y_train[bagged_ind]
        oob_X,oob_y = X_train[oob_ind],y_train[oob_ind]
        model = SVC(C=c)
        model.fit(bagged_X, bagged_y)
        acc.append(accuracy_score(oob_y, model.predict(oob_X)))
    bt_means[i] = np.mean(np.array(acc))
    bt_stds[i] = np.std(np.array(acc))
    print(c)

import matplotlib.pyplot as plt

plt.figure()
(_, caps, _) = plt.errorbar(
    c_vector, k_means, k_stds, fmt='o', markersize=8, capsize=20)

for cap in caps:
    cap.set_markeredgewidth(1)
plt.title('10-Fold CV')
plt.ylabel('Acc')
plt.xlabel('C')
plt.ylim((0.6,0.8))
plt.xscale('log')
plt.figure()
(_, caps, _) = plt.errorbar(
    c_vector, kr_means, kr_stds, fmt='o', markersize=8, capsize=20)

for cap in caps:
    cap.set_markeredgewidth(1)
plt.title('Repeated 10-Fold CV')
plt.ylabel('Acc')
plt.xlabel('C')
plt.ylim((0.6,0.8))
plt.xscale('log')
plt.figure()
(_, caps, _) = plt.errorbar(
    c_vector, bt_means, bt_stds, fmt='o', markersize=8, capsize=20)

for cap in caps:
    cap.set_markeredgewidth(1)
plt.title('Bootstrapped')
plt.ylabel('Acc')
plt.xlabel('C')
plt.xscale('log')
plt.ylim((0.6,0.8))


plt.show()