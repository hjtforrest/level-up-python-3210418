def get_prime_factors(number):
    factors = []
    divisor = 2
    while divisor <= number:
        if number % divisor == 0:
            factors.append(divisor)
            number = number // divisor
        else:
            divisor += 1
    return factors

def get_prime_factors_test1(number) -> list:
    factors = []
    divisor = 2
    while divisor <= number:
        if number % divisor == 0:
            factors.append(divisor)
            number = number // divisor
        else:
            divisor += 1

    return factors
            

# commands used in solution video for reference
if __name__ == '__main__':
    print(get_prime_factors_test1(630))  # [2, 3, 3, 5, 7]
    print(get_prime_factors_test1(13))  # [13]
