import pickle
import json
import numpy as np

global __model
global __data_columns
__data_columns = None
__model = None


def get_estimated_salary(total_exp):
    x = np.zeros(len(__data_columns))
    x[0] = total_exp

    return round(__model.predict([x])[0], 2)


def load_saved_artifacts():
    print("loading saved artifacts...start")


with open("./artifacts/input.json", "r") as f:
    __data_columns = json.load(f)['data_columns']

    if __model is None:
        with open('./artifacts/Expsal.pickle', 'rb') as f1:
            __model = pickle.load(f1)
    print("loading saved artifacts...done")


def get_data_columns():
    return __data_columns


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_estimated_salary(1.5))
    print(get_estimated_salary(10.3))
