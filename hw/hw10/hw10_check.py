from datascience import *
import numpy as np

def correctness_check_0(secret_word):
    try:
        return secret_word == 'artemis'
    except Exception:
        return False

def correctness_check_1_1(null_hypothesis, alt_hypothesis):
    try:
        return (null_hypothesis == 4) and (alt_hypothesis == 5)
    except Exception:
        return False

def correctness_check_1_2(correlation,birds):
    try:
        return np.isclose(round(correlation(birds, "Egg Weight", "Bird Weight"), 3), 0.847)
    except Exception:
        return False
    
def correctness_check_1_3(fit_line, birds):
    try:
        return np.allclose(np.round(fit_line(birds, "Egg Weight", "Bird Weight"), 5), np.array([ 0.71852, -0.05827]))
    except Exception:
        return False
    
def correctness_check_1_6(ci_conclusion):
    try:
        correct = [1,3,6]
        incorrect = [2,4,5]
        return all(x in ci_conclusion for x in correct) and all(x not in ci_conclusion for x in incorrect)
    except Exception:
        return False
    
def correctness_check_1_7(confidence_interval_uses):
    try:
        correct = [1,3]
        incorrect = [2]
        return all(x in confidence_interval_uses for x in correct) and all(x not in confidence_interval_uses for x in incorrect)
    except Exception:
        return False
    
def correctness_check_2_1(egg_weight_eight):
    try:
        return np.isclose(round(egg_weight_eight, 5), 5.68985)
    except Exception:
        return False

def correctness_check_2_2(experts_egg):
    try:
        return np.isclose(round(experts_egg, 5), 6.40837)
    except Exception:
        return False

def correctness_check_2_3(compute_resampled_line, birds):
    try:
        np.random.seed(0)
        return np.allclose(compute_resampled_line(birds, "Egg Weight", "Bird Weight"), np.array([0.64163345, 0.53766856]))
    except Exception:
        return False
    
def correctness_check_2_6(plover_statements):
    try:
        return plover_statements.item(0) == 3
    except Exception:
        return False
    