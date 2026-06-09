vowels = ['a','e','i','o','u']
words = input("Input:")
i = list(words)
left , right = 0, len(words) -1
while left < right:
    while left < right and i[left] not in vowels:
        left += 1
    while left < right and i[right] not in vowels:
        right -= 1
    if left  < right:
        i[left],i[right] = i[right],i[left]
        left += 1
        right -= 1
print("Output:","".join(i))
