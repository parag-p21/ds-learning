
def calculate_variance(numbers):
    mean = sum(numbers) / len(numbers)
    squared_deviations = [(x - mean) ** 2 for x in numbers]

    variance = sum(squared_deviations) / len(numbers)

    return variance

def calculate_std_dev(numbers):
       variance = calculate_variance(numbers)
       return variance ** 0.5

class_a = [70, 72, 68, 71, 69]
class_b = [20, 120, 50, 90, 70]

print("Class A variance:", calculate_variance(class_a))
print("Class A std dev:", calculate_std_dev(class_a))
print("Class B variance:", calculate_variance(class_b))
print("Class B std dev:", calculate_std_dev(class_b))