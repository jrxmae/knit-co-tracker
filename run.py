import csv

# Setting today_sale and monthly_target to None
# so that the value given by the user may be used outside of choice 1 and 2
today_sale = None
monthly_target = None


def welcome():
    '''
    A function made up of a welcome message for the user
    '''
    print('Welcome to Sale Target Tracker!')
    print('With this program, you can input your daily sales '
          'and compare it to your monthly target.')


def main_menu():
    '''
    Displays main menu options to the user
    and sets today_sale and monthly_target globally
    so that it can be called outside of choice 1 and 2
    '''
    global today_sale, monthly_target

    print("Main Menu: ")
    print("1. Add Sale")
    print("2. Add Target")
    print("3. Compare Sales to Target")
    print("4. Exit")
    choice = input("Enter your choice(1, 2, 3, 4): ")

    # Asks user for the date and the sale amount
    # made on the date inputted with validation
    if choice == "1":
        date = input("Enter today's date as ddmmyy: ")
        while len(date) != 6 or not date.isdigit():
            print("Invalid date format.")
            ("Please enter 6 digits in the form of ddmmyy.")
            date = input("Enter today's date as ddmmyy: ")
        today_sale = input('Enter the sale amount made today: ')
        while True:
            try:
                today_sale = int(today_sale)
                break
            except Exception as error:
                print("Invalid number for today's sale.")
                today_sale = input('Enter the sale amount made today: ')
                continue
        print("Sale for today(", date, ") has been inputted.")

        return (
            choice,
            date,
            today_sale
        )

    # Asks user for name of the month and
    # the sale target amount with input validation for both
    elif choice == "2":
        month = input('Enter the name of the month: ')
        while month.lower() not in [
            "january",
            "february",
            "march",
            "april",
            "may",
            "june",
            "july",
            "august",
            "september",
            "october",
            "november",
            "december"
        ]:
            print("Invalid month.")
            month = input('Enter the name of the month: ')

        monthly_target = input("Enter the sale target of the month: ")
        while True:
            try:
                monthly_target = int(monthly_target)
                break
            except Exception as error:
                print("Invalid number for monthly target.")
                monthly_target = input("Enter the sale target of the month: ")
                continue
        print("Target for the month of", month, "has been set.")

        return (
            choice,
            month,
            monthly_target
        )

    # Informs the user whether the target has been reached
    # or what is left of the target by using the sale and target input
    elif choice == "3":
        if today_sale is None or monthly_target is None:
            print("Please enter value for today's sale "
                  "and target of the month.")
        elif today_sale > monthly_target:
            compare = today_sale - monthly_target
            print("Congratulations! You have passed the target by", compare)
        else:
            remaining = monthly_target - today_sale
            print("There is", remaining,
                  " left before you reach your target for the month!")

    # Exits the program when the user is finished
    elif choice == "4":
        print("Exiting program.")
        return choice
    # When the user does not choose any of the available options
    # a message will print to show them an example of an acceptable choice
    else:
        print("Invalid choice. Please enter 1, 2, 3 or 4.")
        return choice


def open_data():
    '''
    Opens the CVS file after the user exits the program to show what they have inputted
    '''
    try:
        os.system("start sales_data.csv") # For Windows
    except Exception as error:
        try:
            os.system("open sales_data.csv") # For macOS
        except Exception as error:
            try:
                os.system("xdg-open sales_data.csv") # For Linux
            except Exception as error:
                print("Failed to open CSV file. Please open 'sales_data.csv' manually.")



def save_data(date, today_sale, month, monthly_target, target_reached):
    '''
    Writes the user input into a csv file where they may view it later
    '''
    with open('sales_data.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, today_sale, month,
                        monthly_target, target_reached])


def loop():
    '''
    Function that prints and loops the program until user decides to exit
    '''
    welcome()
    while True:
        choice = main_menu()
        if choice == "4":
            break
        if choice == "1" or choice == "2":
            save_data(today_sale, monthly_target)


if __name__ == "__main__":
    loop()
