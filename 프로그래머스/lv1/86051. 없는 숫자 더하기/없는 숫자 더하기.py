def solution(numbers):
    num_list = [0,1,2,3,4,5,6,7,8,9]

    answer = sum(list(set(num_list)-set(numbers)))
    return answer