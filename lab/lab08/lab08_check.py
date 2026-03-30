from datascience import *
import numpy as np


def correctness_check_1_2_1(age_mean):
    try:
        return bool(round(age_mean, 3) == 27.228)
    except Exception:
        return False

def correctness_check_1_2_2(age_sd):
    try:
        return bool(round(age_sd, 3) == 5.815)
    except Exception:
        return False

def correctness_check_1_3_1(height_mean):
    try:
        return bool(round(height_mean, 3) == 64.049)
    except Exception:
        return False

def correctness_check_1_3_2(height_sd):
    try:
        return bool(round(height_sd, 3) == 2.525)
    except Exception:
        return False
    
def correctness_check_2_4(q2_4):
    try:
        return (1 in q2_4) and (4 in q2_4) and (len(q2_4) == 2)
    except Exception:
        return False

def correctness_check_2_5(q2_5):
    try:
        return (1 in q2_5) and (3 in q2_5) and (len(q2_5) == 2)
    except Exception:
        return False

def correctness_check_2_6(SD_of_sample_means):
    try:
        return SD_of_sample_means == 3
    except Exception:
        return False

def correctness_check_2_7(pop_vs_sample):
    try:
        return (3 in pop_vs_sample) and (4 in pop_vs_sample) and (len(pop_vs_sample) == 2)
    except Exception:
        return False

def correctness_check_2_8(q2_8):
    try:
        return q2_8 == 1
    except Exception:
        return False