from datascience import *
import numpy as np

def correctness_check_1_2(statistic_choice):
    try:
        return statistic_choice == 3
    except Exception:
        return False

def first_element_check(deck_model_probabilities):
    try:
        return deck_model_probabilities.item(0) == 4/13
    except Exception:
        return False

def second_element_check(deck_model_probabilities):
    try:
        return deck_model_probabilities.item(1) == 9/13
    except Exception:
        return False
    
def sample_size_check(sample_size):
    try:
        return sample_size == 318
    except Exception:
        return False

def percentv1_check(percent_V1):
    try:
        return np.isclose(percent_V1, 66.35220125786164)
    except Exception:
        return False

def correctness_check_1_5(jade_conclusions):
    try:
        return jade_conclusions.item(0) == 1 and jade_conclusions.item(1) == 2 and jade_conclusions.item(2) == 5
    except Exception:
        return False
    
def correctness_check_2_2(vaccine_null):
    try:
        return vaccine_null == 1
    except Exception:
        return False

def correctness_check_2_3(vaccine_alt):
    try:
        return vaccine_alt == 4
    except Exception:
        return False
    
def correctness_check_2_4(valid_test_stat):
    try:
        return valid_test_stat == 4
    except Exception:
        return False
    
def correctness_check_2_5(observed_statistic):
    try:
        return np.isclose(observed_statistic, 6.352201257861637)
    except Exception:
        return False
    
def correctness_check_2_6(assumption_needed):
    try:
        return assumption_needed == 1
    except Exception:
        return False
    
def correctness_check_2_8(assumption_needed):
    try:
        return assumption_needed == 1
    except Exception:
        return False
    
def correctness_check_2_8(p_value):
    try:
        return 0.016 < p_value < 0.026
    except Exception:
        return False
    
def correctness_check_3_1(a,b,c,d,e):
    try:
        return a == 4 and b == 1 and c == 3 and d == 7 and e == 2
    except Exception:
        return False
    
def correctness_check_3_5(pvalue_answers):
    try:
        return sum(pvalue_answers == make_array(1,3)) == 2
    except Exception:
        return False

def correctness_check_3_6(conclusion_answers):
    try:
        return sum(conclusion_answers == make_array(2,5)) == 2
    except Exception:
        return False
    
def correctness_check_4_1(num_females):
    try:
        return num_females == 260
    except Exception:
        return False
    
def correctness_check_4_2(avg_male_vs_female):
    try:
        return avg_male_vs_female == True
    except Exception:
        return False
    
def correctness_check_4_3(null_statement_number,alternative_statement_number):
    try:
        return (null_statement_number == 2) and (alternative_statement_number == 5)
    except Exception:
        return False
    
def correctness_check_4_6(observed_statistic_ab):
    try:
        return np.isclose(observed_statistic_ab, 1.314102564102562)
    except Exception:
        return False
    
def correctness_check_4_7(original_with_shuffled_labels):
    try:
        same_3_7 = original_with_shuffled_labels.column("Age") != original_with_shuffled_labels.column("Shuffled Label")
        if type(same_3_7) == np.ndarray:
            same_3_7 = all(same_3_7)
        return same_3_7
    except Exception:
        return False
    
def correctness_check_4_10(simulated_statistics_ab):
    try:
        return len(simulated_statistics_ab) == 5000
    except Exception:
        return False
    
def correctness_check_4_11(p_val):
    try:
        return 0.10 < p_val < 0.15
    except Exception:
        return False
    
def conclusion_check(conclusion):
    try:
        return conclusion == 'The data are consistent with the null hypothesis.'
    except Exception:
        return False