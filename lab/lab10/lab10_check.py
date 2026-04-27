from datascience import *
import numpy as np


def correctness_check_2_0_1(probability_large_shiny):
    try:
        return np.isclose(probability_large_shiny, 4/13)
    except Exception:
        return False

def correctness_check_2_0_2(probability_shiny):
    try:
        return np.isclose(probability_shiny, 10/13)
    except Exception:
        return False

def correctness_check_2_1_1(probability_shiny_given_large):
    try:
        return np.isclose(probability_shiny_given_large, 4/5)
    except Exception:
        return False

def correctness_check_2_1_2(probability_large_given_shiny):
    try:
        return np.isclose(probability_large_given_shiny, 4/10)
    except Exception:
        return False

def correctness_check_3_1_2(probability_positive_test):
    try:
        return np.isclose(probability_positive_test, 288/10000)
    except Exception:
        return False

def correctness_check_3_2_1(rough_prob_cancer_given_positive):
    try:
        return np.isclose(rough_prob_cancer_given_positive, 4)
    except Exception:
        return False

def correctness_check_3_2_2(prob_cancer_given_positive):
    try:
        return np.isclose(prob_cancer_given_positive, 0.3125)
    except Exception:
        return False

def correctness_check_4_2_1(prob_cancer_given_positive_new):
    try:
        return np.isclose(prob_cancer_given_positive_new, 900/1080)
    except Exception:
        return False