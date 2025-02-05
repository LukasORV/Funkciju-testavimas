from typing import List

def my_numbers(first_list: List[int], second_list: List[List[int]]) -> int:
    if len(first_list) != len(second_list):
        return False
sum_list = []
for i in range(len(first_list)):
    sum_list.append(first_list[i] + sum(second_list[i]))
if len(set(sum_list)) == 1:
    return True
return False