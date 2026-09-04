import random
import matplotlib.pyplot as plt

# # Simulate something that follows a normal distribution
# # random.gauss(mean, std_dev) generates normally-distributed random numbers
# heights = [random.gauss(165, 10) for _ in range(10000)]    # mean=165cm, std=10cm

# plt.hist(heights, bins=50)
# plt.title("Simulated Heights - Normal Distribution")
# plt.xlabel("Height (cm)")
# plt.ylabel("Frequency")
# plt.savefig("normal_distribution.png")
# plt.show()


# def verify_68_95_99_rule(data, mean, std_dev):
#     within_1_std = sum(1 for x in data if mean - std_dev <= x <= mean + std_dev)
#     within_2_std = sum(1 for x in data if mean - 2*std_dev <= x <= mean + 2*std_dev)
#     within_3_std = sum(1 for x in data if mean - 3*std_dev <= x <= mean + 3*std_dev)
    
#     n = len(data)
#     print(f"Within 1 std dev: {within_1_std/n*100:.1f}% (expected ~68%)")
#     print(f"Within 2 std dev: {within_2_std/n*100:.1f}% (expected ~95%)")
#     print(f"Within 3 std dev: {within_3_std/n*100:.1f}% (expected ~99.7%)")

# verify_68_95_99_rule(heights, 165, 10)


# import random

# def simulate_binomial(n_trials, p_success, n_experiments):
#     """Simulate flipping a biased coin n_trials times, repeated n_experiments times"""
#     results = []
#     for _ in range(n_experiments):
#         successes = sum(1 for _ in range(n_trials) if random.random() < p_success)
#         results.append(successes)
#     return results

# # Simulate: flip a coin 10 times, repeat 10000 times, count heads each time
# results = simulate_binomial(10, 0.5, 10000)

# plt.hist(results, bins=range(12))
# plt.title("Binomial Distribution - Heads in 10 Coin Flips")
# plt.xlabel("Number of Heads")
# plt.ylabel("Frequency")
# plt.savefig("binomial_distribution.png")
# plt.show()

# import random

# def simulate_poisson(lambda_rate, n_experiments):
#     """Simulate number of events occurring, given average rate lambda_rate"""
#     results = []
#     for _ in range(n_experiments):
#         # Simple simulation: break the interval into many tiny slices, 
#         # each with small probability of an event
#         events = sum(1 for _ in range(1000) if random.random() < lambda_rate/1000)
#         results.append(events)
#     return results

# # Simulate: average 3 customer complaints per day, repeat 10000 days
# results = simulate_poisson(3, 10000)

# plt.hist(results, bins=range(15))
# plt.title("Poisson Distribution - Customer Complaints per Day")
# plt.xlabel("Number of Complaints")
# plt.ylabel("Frequency")
# plt.savefig("poisson_distribution.png")
# plt.show()


# # import random

# # def simulate_ab_test_under_null(n_users, true_click_rate, n_simulations):
# #     """
# #     Simulates running the SAME button (no real difference) on two groups,
# #     many times, to see how much random variation we'd expect by chance alone.
# #     """
# #     differences = []
    
# #     for _ in range(n_simulations):
# #         # Simulate group A
# #         clicks_a = sum(1 for _ in range(n_users) if random.random() < true_click_rate)
# #         # Simulate group B — SAME true rate, since H0 assumes no real difference
# #         clicks_b = sum(1 for _ in range(n_users) if random.random() < true_click_rate)
        
# #         rate_a = clicks_a / n_users
# #         rate_b = clicks_b / n_users
# #         differences.append(rate_b - rate_a)
    
# #     return differences

# # # Simulate 1000 users per group, true rate 10%, repeat 10000 times
# # diffs = simulate_ab_test_under_null(1000, 0.10, 10000)

# # import matplotlib.pyplot as plt
# # plt.hist(diffs, bins=50)
# # plt.title("Distribution of Differences Under Null Hypothesis (No Real Effect)")
# # plt.xlabel("Difference in Click Rate (B - A)")
# # plt.savefig("null_distribution.png")
# # plt.show()

# # # Our actual observed difference was 11.2% - 10% = 1.2%
# # observed_diff = 0.112 - 0.100

# # # How many of our simulated "no real difference" trials produced 
# # # a difference AT LEAST as extreme as what we observed?
# # extreme_count = sum(1 for d in diffs if abs(d) >= abs(observed_diff))
# # p_value = extreme_count / len(diffs)

# # print(f"Observed difference: {observed_diff:.4f}")
# # print(f"P-value: {p_value:.4f}")

# import random

# def simulate_ab_test_under_null(n_users, true_click_rate, n_simulations):
#     differences = []
#     for _ in range(n_simulations):
#         clicks_a = sum(1 for _ in range(n_users) if random.random() < true_click_rate)
#         clicks_b = sum(1 for _ in range(n_users) if random.random() < true_click_rate)
#         rate_a = clicks_a / n_users
#         rate_b = clicks_b / n_users
#         differences.append(rate_b - rate_a)
#     return differences

# diffs = simulate_ab_test_under_null(1000, 0.10, 10000)

# observed_diff = 0.112 - 0.100
# extreme_count = sum(1 for d in diffs if abs(d) >= abs(observed_diff))
# p_value = extreme_count / len(diffs)

# print(f"Observed difference: {observed_diff:.4f}")
# print(f"P-value: {p_value:.4f}")


from scipy import stats
import numpy as np

group_a = np.array([1]*100 + [0]*900)
group_b = np.array([1]*112 + [0]*888)

t_stat, p_value = stats.ttest_ind(group_a, group_b)
print(f"P-value: {p_value:.4f}")