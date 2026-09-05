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


