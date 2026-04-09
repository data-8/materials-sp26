from datascience import *
import numpy as np

def correctness_check_1_1(standard_units):
    try:
        return standard_units([-3, -2, 1, 0, 1, 2, 3])
    except Exception:
        return False
    
def correctness_check_1_2(standard_array):
    try:
        correct = [2,3,4,5]
        incorrect = [1]
        return all(x in standard_array for x in correct) and all(x not in standard_array for x in incorrect)
    except Exception:
        return False
    
def correctness_check_1_3(correlation):
    try:
        return bool(np.isclose(correlation([-3, 0, 3], [-3, 0, 3]), 1.0000000000000002))
    except Exception:
        return False

def correctness_check_1_4(r_array):
    try:
        correct = [1,2,3,4]
        incorrect = [5]
        return all(x in r_array for x in correct) and all(x not in r_array for x in incorrect)
    except Exception:
        return False
    
def correctness_check_1_5(slope):
    try:
        return bool(np.isclose(slope([-2, 4], [3, -6]), -1.5))
    except Exception:
        return False
    
def correctness_check_1_6(slope_array):
    try:
        correct = [2,4,5]
        incorrect = [1,3]
        return all(x in slope_array for x in correct) and all(x not in slope_array for x in incorrect)
    except Exception:
        return False
    
def correctness_check_1_7(intercept):
    try:
        return bool(np.isclose(intercept([1, 3], [2, 5]), 0.5))
    except Exception:
        return False
    
def correctness_check_1_8(intercept_array):
    try:
        correct = [1,4]
        incorrect = [2,3,5]
        return all(x in intercept_array for x in correct) and all(x not in intercept_array for x in incorrect)
    except Exception:
        return False
    
def correctness_check_2_2(r_guess):
    try:
        return bool(r_guess == -0.75)
    except Exception:
        return False
    
def correctness_check_2_4(regression_answers):
    try:
        correct = [1,3,6]
        incorrect = [2,4,5]
        return all(x in regression_answers for x in correct) and all(x not in regression_answers for x in incorrect)
    except Exception:
        return False
    
def correctness_check_2_6(plot_comparison):
    try:
        correct = [1,3]
        incorrect = [2,4]
        return all(x in plot_comparison for x in correct) and all(x not in plot_comparison for x in incorrect)
    except Exception:
        return False
    
def correctness_check_2_7(rmse):
    try:
        return bool(np.isclose(rmse(10, 15), 76003670.150502235))
    except Exception:
        return False
    
def correctness_check_2_9(rmse_reasoning):
    try:
        return rmse_reasoning == 2
    except Exception:
        return False
    
def correctness_check_2_10(error_array):
    try:
        return bool(error_array.item(0) == 2 and error_array.item(1) == 4)
    except Exception:
        return False
    
def correctness_check_2_11(scoring_array):
    try:
        correct = [1,3]
        incorrect = [2,4]
        return all(x in scoring_array for x in correct) and all(x not in scoring_array for x in incorrect)
    except Exception:
        return False