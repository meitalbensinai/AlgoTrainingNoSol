import pandas as pd
from sklearn.preprocessing import LabelEncoder
from itertools import product
import numpy as np


# load df
def load():
    feature_names = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status',
                     'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss',
                     'hours-per-week', 'native-country', 'salary']
    train = pd.read_csv('adult.data', header=None)
    test = pd.read_csv('adult.data', header=None)
    train.columns = feature_names
    test.columns = feature_names
    return train, test


def check_target_nulls(df):
    # check nulls in salary
    nulls_in_salary = df['salary'].isnull().sum()
    if nulls_in_salary > 0:
        print('Nulls in salary!!!')
    # none, continue


def split_train(train):
    x_tr = train.drop(columns=['salary'])
    y_tr = train['salary'].map({' <=50K': 0, ' >50K': 1})
    return x_tr, y_tr


def encode(features):
    # encode all object type columns
    le = LabelEncoder()
    for col in features.columns:
        if features[col].dtype == 'object':
            le = LabelEncoder()
            le.fit(features[col])
            features[col] = le.transform(features[col])
    return features


def decorrelate(x_tr, test):
    # decorrelate
    correlation = np.array(x_tr.corr())
    corr_values = []
    for i, j in product(np.arange(correlation.shape[0]), np.arange(correlation.shape[1])):
        if i >= j:
            continue
        if np.abs(correlation[i, j]) > 0.3:
            corr_values.append([x_tr.columns[i], x_tr.columns[j]])

    for corr_tuple in corr_values:
        x_tr.drop(columns=[corr_tuple[1]], inplace=True)
        test.drop(columns=[corr_tuple[1]], inplace=True)
    return x_tr, test


def save_to_csv(x_tr, y_tr, x_te, y_te):
    x_tr.to_csv('x_tr.csv')
    y_tr.to_csv('y_tr.csv')
    x_te.to_csv('x_te.csv')
    y_te.to_csv('y_te.csv')


if __name__ == '__main__':
    train, test = load()
    check_target_nulls(train)
    check_target_nulls(test)
    x_tr, y_tr = split_train(train)
    x_te, y_te = split_train(test)
    x_tr = encode(x_tr)
    x_te = encode(x_te)
    x_tr, x_te = decorrelate(x_tr, x_te)
    save_to_csv(x_tr, y_tr, x_te, y_te)
