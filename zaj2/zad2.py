from typing import List

def average(numbers: List[float]) -> float:
    return sum(numbers) / len(numbers)

print(average([1.5, 2.5, 5.0]))