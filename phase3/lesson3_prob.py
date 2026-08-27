# import random

# # Simulate flipping a coin 10 times
# for _i in range(10):
#     flip = random.choice(["Heads", "Tails"])
#     print(flip)


import random

def simulate_coin_flips(n):
    heads_count = 0

    for _ in range(n):
        flip = random.choice(["Heads", "Tails"])
        if flip == "Heads":
            heads_count += 1
    return heads_count / n  

       
print(simulate_coin_flips(10))       # might be 0.3 or 0.7 — small sample, unreliable
print(simulate_coin_flips(1000))       # closer to 0.5
print(simulate_coin_flips(100000))       # very close to 0.5


import random

def simulate_dice_roll(n):
    counts = {}

    for _ in range(n):
        roll = random.randint(1, 6)

        if roll in counts:
            counts[roll] += 1
        else:
            counts[roll] = 1

    proportions = {p: a / n for p, a in counts.items()}

    return proportions


print(simulate_dice_roll(60))
print(simulate_dice_roll(60000))

