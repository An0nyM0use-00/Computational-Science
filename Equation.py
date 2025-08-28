import os
def linear_regression(x_data, y_data):
    n = len(x_data)
    
    # Calculate sums
    sum_x = sum(x_data)
    sum_y = sum(y_data)
    sum_xy = sum(x * y for x, y in zip(x_data, y_data))
    sum_x_squared = sum(x ** 2 for x in x_data)
    
    # Calculate slope (m)
    m = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x ** 2)
    
    # Calculate y-intercept (b)
    b = (sum_y * sum_x_squared - sum_x * sum_xy) / (n * sum_x_squared - sum_x ** 2)
    
    return (m, b)

# Example usage
x_data = [1.0, 2.0, 3.0, 4.0, 5.0]
y_data = [2.5, 4.2, 5.8, 7.5, 9.1]

slope, intercept = linear_regression(x_data, y_data)
os.system('cls')

print(f"x data = {x_data}")
print(f"y data = {y_data}")
print(f"slope ({slope}), intercept ({intercept})")  # Should output approximately (1.65, 0.96)
