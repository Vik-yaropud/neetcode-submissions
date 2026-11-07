from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    max_s = 0
    name_max = ""
    for n, s in scores:
        if s>max_s:
            max_s = s
            name_max = n
    return name_max


# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
