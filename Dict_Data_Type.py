
def days_to_unit(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} minutes"
    else:
        return "Unsupported Units"


def verify_and_execute():
    try:
        user_input_number = int(dict_days_and_unit["days"])
        if user_input_number > 0:
            calculated_value = days_to_unit(user_input_number, dict_days_and_unit["unit"])
            print(calculated_value)
        elif user_input_number == 0:
            print("Your entered num is 0, pls type a valid positive num!")
        else:
            print("Your input num is negative num,so can't convert it")
    except ValueError:
        print("Your input is invalid num.Pls, try with the valid positive num.")


user_input = ""
while user_input != "exit":
    user_input = input("Hey Guys, Pls enter number of days and conversion unit!\n ")
    days_and_unit = user_input.split(":")

    print(days_and_unit)
    dict_days_and_unit = {"days": days_and_unit[0], "unit": days_and_unit[1]}

    print(dict_days_and_unit)
    print(type(dict_days_and_unit))
    verify_and_execute()
else:
    print("Bye, the program is exit.")