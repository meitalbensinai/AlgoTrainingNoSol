import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
from mlxtend.feature_selection import SequentialFeatureSelector as sfs
from mlxtend.feature_selection import ExhaustiveFeatureSelector as efs
import time


np.random.seed(100)

train_size = 500
test_size = 500
n_features = 100


def create_target(x,noise):
    y = 10 * np.sin(np.pi * x[:, 0] * x[:, 1]) + \
          20 * (x[:, 2] - 0.5) ** 2 + 10 * x[:, 3] + 5 * x[:, 4] + noise
    return y

xtr = np.random.rand(train_size, n_features)
noise = np.random.normal(0,1,train_size)
ytr = create_target(xtr,noise)

xte = np.random.rand(test_size, n_features)
noise2 = np.random.normal(0,1,test_size)
yte = create_target(xte,noise2)

lr = DecisionTreeRegressor()

model = lr

def error(xtr, ytr, xte, yte):
    model.fit(xtr,ytr)
    preds = model.predict(xte)
    mse = mean_squared_error(yte,preds)
    print(mse)
print('Original')
error(xtr, ytr, xte, yte)

# print('Backward Selection')
# rfe = RFE(estimator=model, n_features_to_select=1, step=1)
# start_time = time.time()
# rfe.fit(xtr, ytr)
# end_time = time.time()
# total_time = end_time-start_time
# print('time: ' + str(total_time))
# ranking = np.sort(rfe.ranking_[:5]-1)
# error(xtr[:, ranking], ytr, xte[:, ranking], yte)


print('Forward Selection')
sfs1 = sfs(model,
           k_features=20,
           forward=True,
           scoring='neg_mean_squared_error',
           cv=5)
start_time = time.time()
sfs1.fit(xtr, ytr)
end_time = time.time()
total_time = end_time-start_time
print('time: ' + str(total_time))
ranking = np.sort(np.array(list(sfs1.k_feature_idx_)))
error(xtr[:, ranking], ytr, xte[:, ranking], yte)

from mlxtend.plotting import plot_sequential_feature_selection as plot_sfs
import matplotlib.pyplot as plt
fig1 = plot_sfs(sfs1.get_metric_dict(), kind='std_dev')

plt.title('Sequential Forward Selection (w. StdDev)')
plt.grid()
plt.show()


print('Exhaustive Selection')
efs1 = efs(model,
           min_features=1,
           max_features=6,
           scoring='neg_mean_squared_error',
           cv=5)
start_time = time.time()
efs1.fit(xtr, ytr)
end_time = time.time()
total_time = end_time-start_time
print('time: ' + str(total_time))
ranking = np.sort(np.array(list(efs1.k_feature_idx_)))
error(xtr[:, ranking], ytr, xte[:, ranking], yte)

