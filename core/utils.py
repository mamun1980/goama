
class Utils:
    
    def is_prime(number):
        if number <= 1:
            return False
        elif number <= 3:
            return True
        elif number % 2 == 0 or number % 3 == 0:
            return False
        i = 5
        while i * i <= number:
            if number % i == 0 or number % (i + 2) == 0:
                return False
            i += 6
        return True


    def get_factors(number):
        factors = []
        for i in range(1, number + 1):
            if number % i == 0:
                factors.append(i)
        return factors
