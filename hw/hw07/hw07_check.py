from datascience import *
import numpy as np

def correctness_check_1_1(one_resampled_percentage,votes):
    try:
        np.random.seed(123)
        return bool(np.isclose(one_resampled_percentage(votes), 52.400000000000006))
    except Exception:
        return False
    
def correctness_check_1_2_1(percentages_in_resamples):
    try:
        np.random.seed(123)
        return bool(np.isclose(percentages_in_resamples().item(0), 52.400000000000006))
    except Exception:
        return False

def correctness_check_1_2_2(percentages_in_resamples):
    try:
        np.random.seed(123)
        return bool(np.isclose(percentages_in_resamples().item(10), 51.33333333333333))
    except Exception:
        return False
    
def correctness_check_1_3(imm_lower_bound,imm_upper_bound,resampled_percentages):
    try:
        return bool(all([imm_lower_bound == percentile(2.5, resampled_percentages), imm_upper_bound == percentile(97.5, resampled_percentages)]))
    except Exception:
        return False

def correctness_check_1_4(one_resampled_difference,votes):
    try:
        np.random.seed(123)
        return bool(-6 <= float(one_resampled_difference(votes)) <= 15)
    except Exception:
        return False
    
def correctness_check_1_6_1(diff_lower_bound,diff_upper_bound):
    try:
        return bool(-1.8 <= diff_lower_bound <= diff_upper_bound <= 13.4)
    except Exception:
        return False
    
def correctness_check_1_6_2(diff_lower_bound,diff_upper_bound,sampled_leads):
    try:
        return bool(all([diff_lower_bound == percentile(2.5, sampled_leads), diff_upper_bound == percentile(97.5, sampled_leads)]))
    except Exception:
        return False

def correctness_check_2_1(CI_70_percent,CI_90_percent,CI_99_percent):
    try:
        return (CI_70_percent == 2) and (CI_90_percent == 3) and (CI_99_percent == 1)
    except Exception:
        return False
    
def correctness_check_2_2(confidence_answers):
    try:
        return (1 in confidence_answers) and (2 in confidence_answers) and (len(confidence_answers)==2)
    except Exception:
        return False

def correctness_check_2_3(true_percentage_intervals):
    try:
        return bool(int(true_percentage_intervals) == 5700)
    except Exception:
        return False
    
def correctness_check_2_4(cutoff_five_percent):
    try:
        return bool(cutoff_five_percent == 1)
    except Exception:
        return False
    
def correctness_check_2_5(cutoff_one_percent):
    try:
        return bool(cutoff_one_percent == 3)
    except Exception:
        return False
    
def correctness_check_2_6(cutoff_ten_percent):
    try:
        return bool(cutoff_ten_percent == 1)
    except Exception:
        return False
    

def correctness_check_3(secret_word):
    try:
        return bool(secret_word == "cherryblossom")
    except Exception:
        return False