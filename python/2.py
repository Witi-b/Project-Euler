def fibonacci():
    n = 4000000
    num1 = 0
    num2 = 1
    next_number = num2 
    even_num = []
    
    while num2 <= n:
        if next_number % 2 == 0:
            even_num.append(next_number)
        num1, num2 = num2, next_number
        next_number = num1 + num2
    return sum(even_num)
r = fibonacci()
print(r)