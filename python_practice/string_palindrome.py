def is_palindrome(s):
    x = "".join(s.split()).upper()
    y = "".join(reversed(x))
    return x == y
    
s = input("Input:")
ss = is_palindrome(s)
print(ss)