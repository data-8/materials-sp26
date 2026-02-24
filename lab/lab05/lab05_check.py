from datascience import *
import numpy as np

def correctness_check_1_1(number_cheese):
    try:
        return number_cheese == 3
    except Exception:
        return False

def correctness_check_1_2(say_please):
    try:
        return say_please == 'More please'
    except Exception:
        return False
    
def correctness_check_1_5(number_wow_reactions):
    try:
        return number_wow_reactions == 4
    except Exception:
        return False

def correctness_check_2_1(longer_than_five):
    try:
        return longer_than_five == 35453
    except Exception:
        return False