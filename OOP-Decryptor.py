# Decryption_Marquez, Francis Ivan B._BSCpE 1-5

#user input
user_input = input("Enter encrypted text: ")
output = ""

#decryption
for i in range(len(user_input)):
    # if *, change to a
    if user_input[i] == "*":
        output += "a"
    # if &, change to e
    elif user_input[i] == "&":
        output += "e"
    # if #, change to i
    elif user_input[i] == "#":
        output += "i"
    # if +, change to o
    elif user_input[i] == "+":
        output += "o"
    # if !, change to u

#output
print(output)
#additional