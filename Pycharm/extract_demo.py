def process_data(numbers):
    # Select the below 3 lines → Refactor → Extract → Method

    total = 0

    for num in numbers:
        total += num

    average = total / len(numbers)

    return average


data = [1, 2, 3, 4, 5]

result = process_data(data)

print("Average:", result)