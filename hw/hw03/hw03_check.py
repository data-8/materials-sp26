def correctness_check_1_1(answer, pop):
    correct = sum(pop.column('BIRTHS'))/sum(pop.column('START_POP'))
    return answer == correct

def correctness_check_1_2(answer):
    correct = 9
    return answer == correct

def correctness_check_1_3(answer):
    correct = 979657
    return answer == correct

def correctness_check_1_4(answer):
    correct = 3
    return answer == correct

def boston_check(boston_under_15):
    import numpy as np
    return np.isclose(boston_under_15, 5 * 1.2 + 5 * 3.2 + 5 * 4.9)

def manila_check(manila_under_15):
    import numpy as np
    return np.isclose(manila_under_15, 5 * 0.6 + 5 * 1.4 + 5 * 2.2)
 
def correctness_check_2_3(answer):
    correct = 1
    return answer == correct

def correctness_check_2_5(answer):
    correct = 3
    return answer == correct

def correctness_check_2_6(answer):
    from datascience import make_array
    import numpy as np
    correct = make_array(1,3)
    return np.all(np.sort(answer) == np.sort(correct))

def correctness_check_2_7(answer):
    from datascience import make_array
    import numpy as np
    correct = make_array(1,4)
    return np.all(np.sort(answer) == np.sort(correct))

def correctness_check_3_1(answer):
    correct = 3
    return answer == correct

def correctness_check_3_2(answer):
    from datascience import make_array
    import numpy as np
    correct = make_array(2,4,5)
    return np.all(np.sort(answer) == np.sort(correct))

def correctness_check_3_3(answer):
    correct = 2
    return answer == correct

def correctness_check_3_4(answer):
    from datascience import make_array
    import numpy as np
    correct = make_array(1,2,3)
    return np.all(np.sort(answer) == np.sort(correct))