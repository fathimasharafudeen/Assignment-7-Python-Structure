string1 = "Hello "
string2 = input("Enter your Name: ")
greeting = string1 + string2
print(greeting)
string3 = ", welcome to Python programming"
full_text = greeting + string3
print(full_text)

text = full_text   # "Hello Zara, welcome to Python programming"

print(text[0])        # a. first character  -> H
print(text[-1])       # b. last character   -> g
print(text[:5])       # c. first 5 chars    -> Hello
print(text[-11:])     # d. last 11 chars    -> programming
print(text[::-1])     # e. reverse string
print(text[23:29])    # f. Python

start = text.find("Python")          # finds where "Python" begins
print(text[start:start + 6])         # "Python" has 6 letters

strM = "Python beginner tutorial"

print(strM.upper())        # a. PYTHON BEGINNER TUTORIAL
print(strM.lower())        # b. python beginner tutorial
print(strM.lower().capitalize())   # c. Python beginner tutorial
print(strM.count("t"))     # d. 3
print(strM.replace("Python", "Machine Learning"))  # e. Machine Learning beginner tutorial

t1 = (10, 20, 30)
t2 = (40, 50, 60)

# a. Concatenate
t_combine = t1 + t2
print(t_combine)          # (10, 20, 30, 40, 50, 60)

# b. Repeat 3 times
print(t_combine * 3)      # (10, 20, 30, 40, 50, 60, 10, 20, 30, 40, 50, 60, 10, 20, 30, 40, 50, 60)

# c. 3rd element (index 2)
print(t_combine[2])       # 30

# d. First three elements
print(t_combine[:3])      # (10, 20, 30)

# e. Last three elements
print(t_combine[-3:])     # (40, 50, 60)
