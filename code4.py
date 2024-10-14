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
