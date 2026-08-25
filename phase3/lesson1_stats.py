def mean(numbers):
    return sum(numbers) / len(numbers)

print(mean([10, 20, 30, 40, 50]))

def median(numbers):
    numbers = sorted(numbers)
    n = len(numbers)

    if n % 2 == 1:
        return numbers[n // 2]
    else:
        return (numbers[n // 2 - 1] + numbers[n // 2]) / 2
