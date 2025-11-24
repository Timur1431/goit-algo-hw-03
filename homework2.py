import random

def get_numbers_ticket(min, max, quantity):
    if not (1 <= min < max <= 1000):
        return []
    if (max-min<quantity):
        return []
    numbers = random.sample(range(min, max + 1), quantity)

    return sorted(numbers)

for i in range (5):
    print(get_numbers_ticket(10, 14, 6))
    print(" ")