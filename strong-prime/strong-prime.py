def isPrime(num: int) -> bool:
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def isStrongPrime(num: int) -> bool:
    if isPrime(num):
        if isPrime(sum([int(n) for n in str(num)])):
            return True
        else:
            return False
    else:
        return False
