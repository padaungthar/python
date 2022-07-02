calculation_to_unit = 24
name_of_unit = "hours"

def days_to_unit(num_of_days):
        return f"{num_of_days} days are {num_of_days * calculation_to_unit} {name_of_unit}"

def verify_and_execute(user_input):
    try:
        user_input_number = int(user_input)
        if user_input_number > 0:
            calculated_value = days_to_unit(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("Your entered num is 0, pls type a valid postive num!")
        else:
            print("Your input num is negative num,so can't convert it")
    except ValueError:
        print("Your input is invalid num.Pls, try with the valid positive num.")

user_input = ""
while user_input != "exit":
    user_input = input("Hey Guys, Pls enter a number of days and it will be converted to hours!\n ")
    list_of_days = user_input.split(", ")

    print(list_of_days)
    print(set(list_of_days))

    print(type(list_of_days))
    print(type(set(list_of_days)))

    for num_of_days_elements in set(list_of_days):
        verify_and_execute(num_of_days_elements)
else:
    print("Bye, the program is exit")