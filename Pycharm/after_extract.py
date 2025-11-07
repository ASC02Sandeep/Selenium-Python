def process_data(numbers):
    # Select the below 3 lines → Refactor → Extract → Method

    total = method_name(numbers)

    average = total / len(numbers)

    return average


def method_name(numbers) -> int:
    total = 0

    for num in numbers:
        total += num
    return total


data = [1, 2, 3, 4, 5]

result = process_data(data)

print("Average:", result)