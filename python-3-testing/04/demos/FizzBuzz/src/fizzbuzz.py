def fizzbuzz(number):
    if number % 15 == 0:
        return "FizzBuzz"
    if number % 5 == 0:
        return "Buzz"
    if number % 3 == 0:
        return "Fizz"
    return str(number)


def print_fizzbuzz(highest_number):
    fizzbuzz_numbers = (fizzbuzz(i) for i in range(1, highest_number + 1))
    for n in fizzbuzz_numbers:
        print(n)


if __name__ == "__main__":
    print_fizzbuzz(100)
