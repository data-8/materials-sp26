from datascience import *
import numpy as np

def correctness_check_0(secret_word):
    solution = 'valentine'
    return secret_word == solution

def correctness_check_1_2(final_scores, games, sum_scores):
    cal_scores = games.apply(sum_scores, "Cal 1Q","Cal 2Q", "Cal 3Q", "Cal 4Q")
    opp_scores = games.apply(sum_scores, "Opp 1Q", "Opp 2Q", "Opp 3Q", "Opp 4Q")
    correct = games.with_columns("Cal Score", cal_scores, "Opponent Score", opp_scores).select("Opponent", "Cal Score", "Opponent Score")
    return final_scores.column(0).item(5) == "Oregon State" and final_scores.column(1).item(5) == 40 and final_scores.column(2).item(5) == 52

def correctness_check_1_3(did_cal_lose, final_scores):
    return did_cal_lose(final_scores.row(6)) == True

def same_score_check_1_3(did_cal_lose):
    same_score = Table().with_columns("Opponent", ["UC Berkeley"], "Cal Score", [1], "Opponent Score", [1]).row(0)
    return did_cal_lose(same_score) == False

def correctness_check_1_4(cal_wins,cal_losses):
    return np.isclose(cal_wins - cal_losses, -1)

def results_array_check_1_4(results_array):
    return [results_array.item(6), results_array.item(1), results_array.item(5)] == [True, True, True]

def correctness_check_2_1(burritos):
    return len(np.unique(burritos.group('Name').column(1))) == 10

def correctness_check_2_3(ratings_observations):
    solution = make_array(2,4)
    return np.all(np.sort(ratings_observations) == solution)

def results_array_check_2_4(california_burritos):
    return np.isclose(round(california_burritos.where(0, "California").column(1).item(0), 4), 3.5242)

def correctness_check_2_5(best_california_burrito):
    return best_california_burrito == "Pork California" or best_california_burrito == "California Chipotle"

def correctness_check_2_7(burritos_less_than_six):
    return 19 <= burritos_less_than_six <= 26

def correctness_check_3_2(sort_then_group):
    solution = make_array(1,4,5)
    return np.all(np.sort(sort_then_group) == solution)

def correctness_check_3_3(department_ranges,sf):
    def compensation_range(compensation):
        return max(compensation) - min(compensation)
    correct = sf.pivot("Organization Group", "Department", "Total Compensation", compensation_range)
    return department_ranges.take(3) == correct.take(3)

def correctness_check_3_4(department_ranges):
    solution = make_array(2,3,4)
    return np.all(np.sort(department_ranges) == solution)

def correctness_check_3_5(num_over_125k):
    solution = 23
    return num_over_125k == solution
