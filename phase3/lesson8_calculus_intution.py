def error(x):
    return (x - 5) ** 2

# The derivative of (x-5)^2 is 2(x-5) — this tells us the SLOPE at any point x
def derivative(x):
    return 2 * (x - 5)

# Gradient descent: start somewhere random, take small steps toward lower error
def gradient_descent(start_x, learning_rate, steps):
    x = start_x
    history = [x]
    
    for _ in range(steps):
        slope = derivative(x)
        x = x - learning_rate * slope    # move AGAINST the slope direction
        history.append(x)
    
    return x, history

final_x, history = gradient_descent(start_x=20, learning_rate=0.1, steps=50)
print(f"Final x: {final_x:.4f}")
print(f"First 10 steps: {history[:10]}")

# Too small — painfully slow
final_x, _ = gradient_descent(20, 0.01, 50)
print(f"Small learning rate (0.01): {final_x:.4f}")

# Good — converges nicely
final_x, _ = gradient_descent(20, 0.1, 50)
print(f"Good learning rate (0.1): {final_x:.4f}")

# Too large — overshoots, might even diverge
final_x, _ = gradient_descent(20, 0.9, 50)
print(f"Large learning rate (0.9): {final_x:.4f}")

final_x, _ = gradient_descent(20, 1.1, 20)
print(f"Too large learning rate (1.1): {final_x:.4f}")