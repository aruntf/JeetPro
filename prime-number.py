import math
class PrimeChecker:
    number = int (input("Enter a interger"))
    def isPrime(number):
        for count in range (2, math.isqrt(number)+1):
            if (number % count == 0):
                return False
            
        return True

    print (isPrime(23))