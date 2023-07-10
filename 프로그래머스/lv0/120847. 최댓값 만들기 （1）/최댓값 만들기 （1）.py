def solution(numbers):
    numbers.sort(reverse=True)
    answer = 0
    answer = numbers[0]*numbers[1]
    return answer