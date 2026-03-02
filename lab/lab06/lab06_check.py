from datascience import *
import numpy as np

def correctness_check_1_2(expected_proportion_correct):
    try:
        return expected_proportion_correct == 0.5
    except Exception:
        return False

def correctness_check_1_3(valid_stat):
    try:
        return int(sum(valid_stat)) == 2
    except Exception:
        return False

def correctness_check_1_6(observed_statistic):
    try:
        return int(round(observed_statistic,2)) == 6
    except Exception:
        return False