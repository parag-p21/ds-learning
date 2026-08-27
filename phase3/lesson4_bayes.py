import random

# Simulate drawing cards many times, track how often King appears
# given that we already know it's a face card

def simulate_conditional_probability(trials):
    face_cards = ["J", "Q", "K",1,2,3,4,5,6,7,8,9,"A"] * 4    
    kings_given_face = 0
    
    for _ in range(trials):
        card = random.choice(face_cards)
        if card == "K":
            kings_given_face += 1
    
    return kings_given_face / trials

print(simulate_conditional_probability(100000))    


import random

def simulate_medical_test(population_size):
    disease_rate = 0.30          # 1% of population has disease
    test_accuracy = 0.95          # 95% accurate both ways
    
    has_disease = []
    tested_positive = []
    
    for person in range(population_size):
        sick = random.random() < disease_rate    # True if this person has disease
        
        if sick:
            test_result = random.random() < test_accuracy    # 95% chance test correctly says positive
        else:
            test_result = random.random() < (1 - test_accuracy)    # 5% chance test WRONGLY says positive
        
        has_disease.append(sick)
        tested_positive.append(test_result)
    
    return has_disease, tested_positive

# Simulate 100,000 people
sick, positive = simulate_medical_test(100000)

# Among people who tested positive, how many ACTUALLY have the disease?
actually_sick_and_positive = sum(1 for s, p in zip(sick, positive) if s and p)
total_positive = sum(positive)

probability = actually_sick_and_positive / total_positive
print(f"Probability of actually having disease given positive test: {probability:.4f}")