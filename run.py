
def welcome():
    '''
    A function made up of a welcome message for the user
    '''
    print('Welcome to Sale Target Tracker!')
    print('With this program, you can input your daily sales and compare it to your monthly target.')

def user_input():
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

    '''
    Asks user for the date and the sale amount made on the date inputted
    '''
    date = int(input("Enter today's date as ddmmyy: "))
    today_sale = int(input('Enter the sale amount made today: '))
    return (
        month,
        monthly_target,
        date,
        today_sale
    )

def compare(
    month,
    monthly_target,
    date,
    today_sale
):
    '''
    Compares the sale amount made on the day inputted to the sale target for the month and prints depending on if the target was reached or not
    '''
    if today_sale < monthly_target:
        print("There is", monthly_target - today_sale, "left to make. Goodluck!")
    else:
        print("Congratulations! You passed the target by", today_sale - monthly_target)
        
def loop():
    '''
    Function that prints and loops the program until user decides to exit
    '''
    welcome()
    while True:
        (
            month,
            monthly_target,
            date,
            today_sale
        ) = user_input()
        compare(
            month,
            monthly_target,
            date,
            today_sale
        )

if __name__ == "__main__":
    loop()
