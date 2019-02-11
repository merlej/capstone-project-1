import numpy as np
import pandas as pd

def bootstrap_replicate_1d(data, func):
    bs_sample = np.random.choice(data, len(data))
    return func(bs_sample)


def draw_bs_reps(data, func, size=1):
    bs_reps = np.empty(size)
    
    for i in range(size):
        bs_reps[i] = bootstrap_replicate_1d(data, func)

    return bs_reps
