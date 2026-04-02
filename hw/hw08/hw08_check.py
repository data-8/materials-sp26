from datascience import *
import numpy as np

def correctness_check_1_1_a(q1_1_percentage):
    try:
        return np.isclose(q1_1_percentage, 93.75)
    except Exception:
        return False
    
def correctness_check_1_1_b(q1_1_reasoning):
    try:
        return (1 in q1_1_reasoning) and (3 in q1_1_reasoning) and (len(q1_1_reasoning) == 2)
    except Exception:
        return False
    
def correctness_check_1_2_a(q1_2_percentage):
    try:
        return np.isclose(q1_2_percentage, 6.25)
    except Exception:
        return False

def correctness_check_1_2_b(q1_2_reasoning):
    try:
        return np.isclose(q1_2_reasoning, 1)
    except Exception:
        return False
    
def correctness_check_1_3_a(q1_3_percentage):
    try:
        return np.isclose(q1_3_percentage, 6.25)
    except Exception:
        return False

def correctness_check_1_3_b(q1_3_reasoning):
    try:
        return np.isclose(q1_3_reasoning, 4)
    except Exception:
        return False


def correctness_check_2_1(smallest):
    try:
        return smallest == 1112
    except Exception:
        return False
    
def correctness_check_2_2(sample_size_answer):
    try:
        return sample_size_answer == 2
    except Exception:
        return False
    
def correctness_check_2_3(smallest_num):
    try:
        return smallest_num == 757
    except Exception:
        return False
    
def correctness_check_2_4(sd_answers):
    try:
        return (1 in sd_answers) and (5 in sd_answers) and (len(sd_answers) == 2)
    except Exception:
        return False

def correctness_check_2_5(option):
    try:
        return option == 4
    except Exception:
        return False
    
def correctness_check_3_2(clt_answers):
    try:
        return (1 in clt_answers) and (2 in clt_answers) and (4 in clt_answers) and (len(clt_answers)==3)
    except Exception:
        return False
    
def correctness_check_3_3(approximate_sd):
    try:
        return np.isclose(approximate_sd, ((210/400) * (190/400) / 400) ** 0.5)
    except Exception:
        return False
    
def correctness_check_3_4(exact_sd):
    try:
        return 0.02 <= exact_sd <= 0.03
    except Exception:
        return False

def correctness_check_3_5_lower(lower_limit):
    try:
        return np.isclose(lower_limit, 0.47506253911140456)
    except Exception:
        return False
    
def correctness_check_3_5_upper(upper_limit):
    try:
        return np.isclose(upper_limit, 0.5749374608885954)
    except Exception:
        return False
    
def correctness_check_3_6(marissa_sample_mean_sd):
    try:
        return np.isclose(marissa_sample_mean_sd, .005)
    except Exception:
        return False
    
def correctness_check_3_7(smaller_sample_mean_sd):
    try:
        return smaller_sample_mean_sd > .005
    except Exception:
        return False
    
def correctness_check_3_8(larger_sample_mean_sd):
    try:
        return larger_sample_mean_sd < .005
    except Exception:
        return False