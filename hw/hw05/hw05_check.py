from datascience import *
import numpy as np

def correctness_check_1_11(dollar_bet_on_red):
    try:
        return dollar_bet_on_red('red') == 1
    except Exception:
        return False

def correctness_check_1_12(dollar_bet_on_red):
    try:
        return dollar_bet_on_red('green') == -1
    except Exception:
        return False

def correctness_check_1_2(wheel):
    try:
        return sum(wheel.column("Winnings: Red")) == -2
    except Exception:
        return False

def correctness_check_1_3(ten_bets):
    try:
        return ten_bets.num_rows == 10
    except Exception:
        return False

def correctness_check_1_4(net_gain_red):
    try:
        return -10000 <= net_gain_red(10000) <= 10000
    except Exception:
        return False

def correctness_check_1_51(simulated_gains_red):
    try:
        return len(simulated_gains_red) == 10000
    except Exception:
        return False

def correctness_check_1_52(simulated_gains_red):
    try:
        return np.count_nonzero(simulated_gains_red <= 100) == 10000
    except Exception:
        return False

def correctness_check_1_71(dollar_bet_on_split):
    try:
        return dollar_bet_on_split('6') == 17
    except Exception:
        return False

def correctness_check_1_72(dollar_bet_on_split):
    try:
        return dollar_bet_on_split('10') == -1
    except Exception:
        return False

def correctness_check_1_8(wheel):
    try:
        return sum(wheel.column("Winnings: Split")) == -2
    except Exception:
        return False

def correctness_check_1_91(simulated_gains_split):
    try:
        return len(simulated_gains_split) == 10000
    except Exception:
        return False

def correctness_check_1_92(simulated_gains_split):
    try:
        return np.count_nonzero(simulated_gains_split >= -200) == 10000
    except Exception:
        return False

def correctness_check_1_10(histogram_statements):
    try:
        return (histogram_statements.item(0) == 1 and
                histogram_statements.item(1) == 2 and
                histogram_statements.item(2) == 3)
    except Exception:
        return False

def correctness_check_2_1(first_three_black):
    try:
        return 0.106 == round(first_three_black, 3)
    except Exception:
        return False

def correctness_check_2_2(no_green):
    try:
        return 0.582 < no_green < 0.583
    except Exception:
        return False

def correctness_check_2_3(at_least_one_green):
    try:
        return 0.417643346770 <= at_least_one_green <= 0.417643346771
    except Exception:
        return False

def correctness_check_2_4(lone_winners):
    try:
        return 0.0011 == round(lone_winners, 4)
    except Exception:
        return False

def correctness_check_3_1(movie_frequency_answer):
    try:
        if len(movie_frequency_answer) != 3:
            return False
        return sum(movie_frequency_answer == make_array(1,4,5)) == 3
    except Exception:
        return False

def correctness_check_3_2(same_studio_answer):
    try:
        if len(same_studio_answer) != 2:
            return False
        return sum(same_studio_answer == make_array(1,4)) == 2
    except Exception:
        return False