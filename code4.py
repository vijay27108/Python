# Conditional statements
#For a list of common symbols you can use to construct conditions, check out the chart below.

#Symbol	Meaning
#==	equals
#!=	does not equal
#<	less than
#<=	less than or equal to
#>	greater than
#>=	greater than or equal to


# if statement
def evalutate_temp(temp):
    message = "Normal Temperature"
    if temp >38:
        message = "Fever"
    return message

#Normal Temperature
print(evalutate_temp(35))
# Fever
print(evalutate_temp(40))

#  if else statement

def evaluate_tempifel(temp):
    if temp> 38:
        print("Fever")
    else:
        print("Normal temperature")
#  Normal
evaluate_tempifel(35)
# Fever
evaluate_tempifel(40)

#"if ... elif ... else" statements

def evalutate_tempifelseif(temp):
    if temp >35 and temp<38:
        print("Mild Fever")
    elif temp > 38:
        print("High Fever")
    else:
        print("Normal")

#  High Fever
evalutate_tempifelseif(40)
#  Mild Fever
evalutate_tempifelseif(36)
#  Normal
evalutate_tempifelseif(34)

#  Multiple ifelse
def get_dose(weight):
    # Dosage is 1.25 ml for anyone under 5.2 kg
    if weight < 5.2:
        dose = 1.25
    elif weight < 7.9:
        dose = 2.5
    elif weight < 10.4:
        dose = 3.75
    elif weight < 15.9:
        dose = 5
    elif weight < 21.2:
        dose = 7.5
    # Dosage is 10 ml for anyone 21.2 kg or over
    else:
        dose = 10
    return dose
print(get_dose(10))

# ....................................................................................................................
# List
flowers_list = ["pink primrose", "hard-leaved pocket orchid", "canterbury bells", "sweet pea", "english marigold", "tiger lily", "moon orchid", "bird of paradise", "monkshood", "globe thistle"]
print(type(flowers_list))
print(flowers_list)

# Indexing
#  Start with Zero indexing

print("first index:",flowers_list[0])

#Side Note: You may have noticed that in the code cell above, we use a single print() to print multiple items (both a Python string (like "First entry:") and a value from the list (like flowers_list[0]). To print multiple things in Python with a single command, we need only separate them with a comma.
#Slicing
#You can also pull a segment of a list (for instance, the first three entries or the last two entries). This is called slicing. For instance:
#to pull the first x entries, you use [:x], and
#to pull the last y entries, you use [-y:]
print("First three entries:", flowers_list[:3])
print("Final two entries:", flowers_list[-2:])

#  Removing the items from the list
flowers_list.remove("pink primrose")
print(flowers_list)
#  Adding items 
flowers_list.append("pink primrose")
print(flowers_list)


#  Adding number in the list
hardcover_sales = [139, 128, 172, 139, 191, 168, 170]

print("Length of the list:", len(hardcover_sales))
print("Entry at index 2:", hardcover_sales[2])

#  To get min, max and sum of the list
print("Minimum:", min(hardcover_sales))
print("Maximum:", max(hardcover_sales))
print("Total books sold in one week:", sum(hardcover_sales))

#Slicing and sum
print("Average books sold in first five days:", sum(hardcover_sales[:5])/5)