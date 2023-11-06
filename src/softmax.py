import numpy as np
from scipy.special import softmax


def observations_to_dataset(data_list, costs, T=1):
    T = 1  # np.std(energies)
    print("T =", T)
    probs = softmax(-np.array(costs) / T)

    data_dict = dict(zip(data_list, probs))
    sm = sum(data_dict.values())
    data_dict = {k: v / sm for k, v in data_dict.items()}

    return data_dict
