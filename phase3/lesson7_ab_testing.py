import random

def simulate_ab_test_under_null(n_users, true_click_rate, n_simulations):
    """
    Simulates running the SAME button (no real difference) on two groups,
    many times, to see how much random variation we'd expect by chance alone.
    """
    differences = []
    
    for _ in range(n_simulations):
        # Simulate group A
        clicks_a = sum(1 for _ in range(n_users) if random.random() < true_click_rate)
        # Simulate group B — SAME true rate, since H0 assumes no real difference
        clicks_b = sum(1 for _ in range(n_users) if random.random() < true_click_rate)
        
        rate_a = clicks_a / n_users
        rate_b = clicks_b / n_users
        differences.append(rate_b - rate_a)
    
    return differences

# Simulate 1000 users per group, true rate 10%, repeat 10000 times
diffs = simulate_ab_test_under_null(1000, 0.10, 10000)

import matplotlib.pyplot as plt
plt.hist(diffs, bins=50)
plt.title("Distribution of Differences Under Null Hypothesis (No Real Effect)")
plt.xlabel("Difference in Click Rate (B - A)")
plt.savefig("null_distribution.png")
plt.show()

# Our actual observed difference was 11.2% - 10% = 1.2%
observed_diff = 0.112 - 0.100

# How many of our simulated "no real difference" trials produced 
# a difference AT LEAST as extreme as what we observed?
extreme_count = sum(1 for d in diffs if abs(d) >= abs(observed_diff))
p_value = extreme_count / len(diffs)

print(f"Observed difference: {observed_diff:.4f}")
print(f"P-value: {p_value:.4f}")





import random

def simulate_fair_coin_100_flips():
    """One experiment: flip a fair coin 100 times, count heads"""
    heads = sum(1 for _ in range(100) if random.random() < 0.5)
    return heads

# Repeat this experiment 10000 times
results = [simulate_fair_coin_100_flips() for _ in range(10000)]

print(results[:20])    # show first 20 results, just to look at them



import random

def simulate_ab_test_under_null(n_users, true_click_rate, n_simulations):
    differences = []
    for _ in range(n_simulations):
        clicks_a = sum(1 for _ in range(n_users) if random.random() < true_click_rate)
        clicks_b = sum(1 for _ in range(n_users) if random.random() < true_click_rate)
        rate_a = clicks_a / n_users
        rate_b = clicks_b / n_users
        differences.append(rate_b - rate_a)
    return differences

diffs = simulate_ab_test_under_null(1000, 0.10, 10000)

observed_diff = 0.112 - 0.100
extreme_count = sum(1 for d in diffs if abs(d) >= abs(observed_diff))
p_value = extreme_count / len(diffs)

print(f"Observed difference: {observed_diff:.4f}")
print(f"P-value: {p_value:.4f}")



from scipy import stats

# Group A (old button): 100 clicks out of 1000
# Group B (new button): 112 clicks out of 1000

import numpy as np
group_a = np.array([1]*100 + [0]*900)     # 100 clicks, 900 no-clicks
group_b = np.array([1]*112 + [0]*888)      # 112 clicks, 888 no-clicks

t_stat, p_value = stats.ttest_ind(group_a, group_b)
print(f"P-value: {p_value:.4f}")


from scipy import stats
import numpy as np

group_a = np.array([1]*100 + [0]*900)
group_b = np.array([1]*112 + [0]*888)

t_stat, p_value = stats.ttest_ind(group_a, group_b)
print(f"P-value: {p_value:.4f}")