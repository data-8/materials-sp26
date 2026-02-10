def correctness_check_1_1(answer):
    correct = 20.0
    return answer == correct

def correctness_check_1_2(answer):
    import numpy as np
    correct = 70.71067811865476
    return np.isclose(answer, correct)

def correctness_check_2_2(answer):
    correct = '$53.25 '
    return str(answer) == correct

def correctness_check_2_3(answer):
    correct = 53250000
    return answer == correct

def correctness_check_3_3(answer):
    import math
    correct = 11558613.861386139
    return math.isclose(answer, correct, rel_tol = 0.1)

def correctness_check_3_6(answer):
    import math
    correct = 11794790.817048479
    return math.isclose(answer, correct, rel_tol = 0.1)

def correctness_check_4_2(answer):
    correct = 5
    return answer == correct