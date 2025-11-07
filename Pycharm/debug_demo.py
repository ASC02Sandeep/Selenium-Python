def calculate_total(items):
    total = 0

    
    for item in items:  # Set breakpoint here

        total += item

        print(f"Added {item}, total: {total}")

    return total


def main():
    prices = [10, 20, 30, 40]

    final_total = calculate_total(prices)

    print(f"Final total: {final_total}")


if __name__ == "__main__":
    main()