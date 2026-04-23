from datascience import *
import numpy as np

def correctness_check_1_1_1(distance_example):
    try:
        return np.isclose(distance_example, 5.196152422706632)
    except Exception:
        return False
    
def correctness_check_1_1_2(tradeoff):
    try:
        correct = [1,2,4]
        incorrect = [3]
        return all(x in tradeoff for x in correct) and all(x not in tradeoff for x in incorrect)
    except Exception:
        return False
    
def correctness_check_1_2(train,test,coordinates):
    try:
        return (train.num_rows + test.num_rows) == coordinates.num_rows
    except Exception:
        return False
    
def correctness_check_1_3(features):
    try:
        return sorted(features) == ['latitude', 'longitude']
    except Exception:
        return False
    
def correctness_check_1_4(classify,coordinates):
    try:
        sorted_coordinates = coordinates.sort("school")
        return classify(sorted_coordinates.row(85), 3, sorted_coordinates.take(np.arange(50, 100))) == 'Stanford'
    except Exception:
        return False

def correctness_check_1_5(accuracy):
    try:
        return 0.90 <= accuracy <= 1
    except Exception:
        return False
    
def correctness_check_1_6(k):
    try:
        return k == 47
    except Exception:
        return False
    
def correctness_check_1_7_1(train_test_split):
    try:
        correct = [1,4]
        incorrect = [2,3]
        return all(x in train_test_split for x in correct) and all(x not in train_test_split for x in incorrect)
    except Exception:
        return False
    
def correctness_check_1_7_2(test_set_reasoning):
    try:
        correct = [2,3]
        incorrect = [1,4]
        return all(x in test_set_reasoning for x in correct) and all(x not in test_set_reasoning for x in incorrect)
    except Exception:
        return False
    
def correctness_check_1_8(k_reasoning):
    try:
        correct = [2,4]
        incorrect = [1,3]
        return all(x in k_reasoning for x in correct) and all(x not in k_reasoning for x in incorrect)
    except Exception:
        return False
    
def correctness_check_1_9_1(prob_furd):
    try:
        return np.isclose(prob_furd, 0.4275092936802974)
    except Exception:
        return False
    
def correctness_check_1_9_2(prob_test):
    try:
        return np.isclose(prob_test, 0.5)
    except Exception:
        return False