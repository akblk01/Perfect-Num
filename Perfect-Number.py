def perfect(number):
    total = 0

    for i in range(1, number):

        if (number % i == 0):
            total += i

    return total == number


for i in range(1, 1001):
    if (perfect(i)):
        print("Perfect Number:", i)