def is_even(n):
    for i in range(1,100): 
        if n % 2 == 0:
            return True
        else: 
            return False
        
n = int(input("Enter a num:"))
result = is_even(n)
print(n,result)