import math

def checkPrime(numbers):

    for n in numbers:
        isPrime = n > 1 and all( n%i for i in range(2, int(math.sqrt(n)+1)))
        print('Prime' if isPrime else 'Not prime')

if __name__ == '__main__':
    ar_count = int(input())

    numbers = list();
    for i in range(ar_count):
        n = int(input().strip())
        numbers.append(n)

    checkPrime(numbers)
