'''
Setting today_sale and monthly_target to None so that the value given by the user may be used outside of choice 1 and 2
'''
today_sale = None
monthly_target = None

def welcome():
    '''
    A function made up of a welcome message for the user
    '''
    print('Welcome to Sale Target Tracker!')
    print('With this program, you can input your daily sales and compare it to your monthly target.')

def main_menu():
    '''
    Displays main menu options to the user and sets today_sale and monthly_target globally so that it can be called outside of choice 1 and 2
    '''
    global today_sale, monthly_target

    print("Main Menu: ")
    print("1. Add Sale")
    print("2. Add Target")
    print("3. Compare Sales to Target")
    print("4. Exit")
    choice = input("Enter your choice(1, 2, 3, 4): ")
    if choice == "1":
        '''
        Asks user for the date and the sale amount made on the date inputted with validation
        '''
        date = input("Enter today's date as ddmmyy: ")
        while len(date) != 6 or not date.isdigit():
            print("Invalid date format. Please enter 6 digits in the form of ddmmyy.")
            date = input("Enter today's date as ddmmyy: ")
        today_sale = input('Enter the sale amount made today: ')
        while True:
            try:
                today_sale = int(today_sale)
                break
            except:
                print("Invalid number for today's sale.")
                today_sale = input('Enter the sale amount made today: ')
        print("Sale for today(",date,") has been inputted.")
        return(
            choice,
            date,
            today_sale
        )

    elif choice == "2":
        '''
        Asks user for name of the month and the sale target amount with input validation for both
        '''
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
            except:
                print("Invalid number for monthly target.")
                monthly_target = input("Enter the sale target of the month: ")
        print("Target for the month of",month,"has been set.")
        return(
            choice,
            month,
            monthly_target
        )
    
    elif choice == "3":
        if today_sale is None or monthly_target is None:
            print("Please enter value for today's sale and target of the month.")
        elif today_sale > monthly_target:
            compare = today_sale - monthly_target
            print("Congratulations! You have passed the target by", compare)
        else:
            remaining = monthly_target - today_sale
            print("There is",remaining,"left before you reach your target for the month!")

    elif choice == "4":
        print("Exiting program.")
        return(choice)
    else:
        print("Invalid choice. Please enter 1, 2, 3 or 4.")
        return(choice)
    
def loop():
    '''
    Function that prints and loops the program until user decides to exit
    '''
    welcome()
    while True:
        choice = main_menu()
        if choice == "4":
            break

if __name__ == "__main__":
    loop()
