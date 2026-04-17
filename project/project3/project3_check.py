from datascience import *
import numpy as np

def correctness_check_5(accuracy):
    try:
        return np.isclose(np.round(accuracy, 3), 0.9)
    except Exception:
        return False