
#loop 
multicands = (2,2,2,3,3,5)
product = 1
for i in multicands:
    product = product * i
print(product)

# Check the uppercase letter in string
s = 'steganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image, Or video.'
for char in s:
    if char.isupper():
        print(char , end = '')

#Range function
for i in range(5):
    print("This is number",i)

# while loop

i = 0
while i < 10:
    print(i , end = ' ')
    i+=1

#  List comprehensions
squares = [n**2 for n in range(10)]
print(squares)

# ........................................................
# Strings and Dictionaries

# Strings 
x  = 'Pluto is a planet'
y = 'Pluto is a planet'
if x == y:
    print("Both are equal")

# Convert lowercase string to uppercase string

claim = "Pluto is a planet"
print(claim.upper())
print(claim.lower())

# Dictionaries 
numbers = {"one":1 , "two":2, "Three":3}
print(numbers['one'])

# We can add another key in dictionary
numbers['eleven'] = 11
print(numbers)

#Change the value of exiting value of key 

numbers['one'] = 'Pluto'
print(numbers)

