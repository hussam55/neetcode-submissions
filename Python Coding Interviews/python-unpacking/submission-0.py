from typing import List, Tuple


def sum_3_integers(triplet: List[int]) -> int:
    num1, num2, num3 = triplet
    sum = num1 + num2 + num3
    return sum


def compute_volume(box_dimensions: Tuple[int, int, int]) -> int:
    width , hieght, depth = box_dimensions
    volume = width * hieght * depth
    return volume
  

# do not modify below this line
print(sum_3_integers([1, 2, 3]))
print(sum_3_integers([4, 6, 2]))

print(compute_volume((1, 2, 3)))
print(compute_volume((3, 2, 1)))
print(compute_volume((3, 9, 7)))
