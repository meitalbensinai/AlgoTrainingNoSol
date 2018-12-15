import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1200)

names = ['class', 'date', 'plant-stand', 'precip', 'temp', 'hail', 'crop-hist',
         'area-damaged', 'severity', 'seed-tmt', 'germination', 'plant-growth',
         'leaves', 'halo', 'marg', 'size', 'shread', 'half', 'mild', 'stem', 'lodging',
         'cankers', 'lesion', 'bodies', 'decay', 'mycelium', 'discolor', 'sclerotia',
         'pods', 'spots', 'seed', 'growth', 'seedd', 'seeds', 'shriveling', 'roots']

train = pd.read_csv('soybean-large.data', header=None)
train.columns = names

test = pd.read_csv('soybean-large.test', header=None)
test.columns = names


print('Column Missing Values')
unique_classes=train['class'].unique()
sd2 = np.zeros(len(unique_classes))
for column in train.columns:
    if '?' in np.unique(train[column]):
        print(column,(train[column]=='?').sum())
        sd= train.groupby(by=['class'])[column].value_counts().unstack()._values[:, -1]
        sd2+=np.nan_to_num(sd)

ind = np.nonzero(sd2)[0]
width = 10
bins = np.arange(0,width*len(unique_classes[ind]), width)
bins2 = 1+np.arange(0,width*len(unique_classes[ind]), width)
ax = plt.axes()
ax.grid()
plt.bar(height=sd2[ind],width=0.75,x=bins,color='black')
plt.xticks(bins2,labels=unique_classes[ind],size=14)
plt.ylabel('Missing')
plt.title('Missing vs. Class')
plt.show()

def impute_with_median(train,test):

    ty = train['class']
    tx = train.drop(columns=['class'])

    ry = test['class']
    rx = test.drop(columns=['class'])

    for column in tx.columns:
        tx[column]=tx[column].fillna(tx[column].median())
        rx[column]=rx[column].fillna(tx[column].median())
    return tx,ty,rx,ry

def f2(x):
    return x

def impute_with_median_by_class(train,test):

    for column in train.columns[1:]:
        train[column]=train.groupby('class')[column].transform(lambda x:x.fillna(x.median()))
        test[column]=test.groupby('class')[column].transform(lambda x:x.fillna(x.median()))
    return impute_with_median(train, test)

def delete_rows_with_NANs(train,test):
    train = train.dropna()
    return impute_with_median(train, test)



train = pd.read_csv('soybean-large.data', header=None)
train.columns = names

test = pd.read_csv('soybean-large.test', header=None)
test.columns = names

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
train['class']=le.fit_transform(train['class'])
test['class']=le.transform(test['class'])

def f(x):
    if x == '?':
        return np.NaN
    return x

train = train.applymap(func=f)
test = test.applymap(func=f)

tx,ty,rx,ry=impute_with_median(train,test)
tx2,ty2,rx2,ry2=impute_with_median_by_class(train,test)
tx3,ty3,rx3,ry3=delete_rows_with_NANs(train,test)

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

acc=0
exp = 1000
for i in range(exp):
    model = RandomForestClassifier(n_estimators=100)
    model.fit(tx,ty)
    pre =model.predict(rx)
    acc += accuracy_score(ry,pre)
print(acc/exp)

acc2=0
for i in range(exp):
    model2 = RandomForestClassifier(n_estimators=100)
    model2.fit(tx2,ty2)
    pre2 =model2.predict(rx2)
    acc2 += accuracy_score(ry2,pre2)
print(acc2/exp)

acc3=0
for i in range(exp):
    model3 = RandomForestClassifier(n_estimators=100)
    model3.fit(tx3,ty3)
    pre3 =model3.predict(rx3)
    acc3 += accuracy_score(ry3,pre3)
print(acc3/exp)




