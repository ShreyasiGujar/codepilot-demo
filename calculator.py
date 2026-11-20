def calculate_average(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    total = sum(numbers)
    return total / len(numbers)
