def n_a(names,age):
  age += 1
  for i in range(len(names)):
    names [i] = ""
  return age 

names = input("Enter your name:")
age = int(input("Enter you age:"))
print("Hello, my name is {} and I will be {}.".format(names,age+1))


