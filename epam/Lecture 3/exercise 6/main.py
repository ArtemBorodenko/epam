def fizzbuzz(a: int) -> None:
    if (a < 1) or (a > 100):
        print(a, "is out of range [1,100]")
    else:
        if a % 3 == 0:
            print("Fizz", end="")
        if a % 5 == 0:
            print("Buzz")
        if (a % 5 != 0) and (a % 3 != 0):
            print(a)



if __name__ == '__main__':
    n = int(input('Enter the number:'))
    fizzbuzz(n)
