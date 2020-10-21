import math

def count_negatives(numbers: list) -> int:
    numbers.append(0)
    numbers.sort()
    return numbers.index(0)


if __name__ == '__main__':
    input_numbers = [4, -9, 8, -11, 8]
    print(f'There are {count_negatives(input_numbers)} negative numbers in list {input_numbers}')
