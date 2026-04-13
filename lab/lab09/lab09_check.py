from datascience import *
import numpy as np


def correctness_check_1_0(least_squares_order):
    try:
        answer = make_array(4, 1, 3, 2)
        return answer == least_squares_order
    except Exception:
        return False

def correctness_check_1_3_a(duration_std):
    try:
        return round(duration_std, 2) == 1.14
    except Exception:
        return False

def correctness_check_1_3_b(wait_std):
    try:
        return round(wait_std, 2) == 13.57 
    except Exception:
        return False
    
def correctness_check_1_5(correlation):
    try:
        return correlation == 4
    except Exception:
        return False

def correctness_check_1_6(r):
    try:
        return round(r,3) == 0.901
    except Exception:
        return False

def correctness_check_2_1(slope):
    try:
        return np.round(slope, 4) == 10.7296
    except Exception:
        return False

def correctness_check_2_2(intercept):
    try:
        return np.round(intercept, 3) == 33.474
    except Exception:
        return False

def correctness_check_3_1_a(two_minute_predicted_waiting_time):
    try:
        return round(two_minute_predicted_waiting_time, 3) == 54.934
    except Exception:
        return False

def correctness_check_3_1_b(five_minute_predicted_waiting_time):
    try:
        return round(five_minute_predicted_waiting_time, 3) == 87.123
    except Exception:
        return False

def correctness_check_5_1(below_3_r, above_3_r):
    try:
        return np.allclose([below_3_r, above_3_r], [0.290189526493, 0.372782225571])
    except Exception:
        return False


def correctness_check_6(secret):
    try:
        return secret == "beep boop"
    except Exception:
        return False