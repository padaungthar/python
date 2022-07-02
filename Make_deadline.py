from datetime import datetime

user_input = ''
while user_input != 'exit':
    user_input = input("Enter your goal with a deadline separated by colon\n")
    input_list = user_input.split(":")
    goal = input_list[0]
    deadline = input_list[1]
    deadline_date = datetime.strptime(deadline, "%d.%m.%Y")
    today_date = datetime.today()
    until_time = deadline_date - today_date
    until_hours = int(until_time.total_seconds() / 60 / 60)
# Calculate how many days from today till deadline
    print(f"Dear Users! Time remaining for your goal:{goal} is {until_hours} hours")
else:
    print("Bye, the program is exit")
