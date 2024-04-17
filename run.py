'''
A function made up of a welcome message for the user
'''
def welcome():
    print('Welcome to Sale Target Tracker!')
    print('With this program, you can input your daily sales and compare it to your monthly target.')


'''
Calls welcome function to print the welcome message to the user
'''
welcome()

'''
Asks user for name of the month and the sale target amount
'''
month = input('Enter the name of the month: ')
monthly_target = int(input("Enter the sale target of the month: "))

'''
Asks user for the date and the sale amount made on the date inputted
'''
date = int(input("Enter today's date as ddmmyy: "))
today_sale = int(input('Enter the sale amount made today: '))

'''
Compares the sale amount made on the day inputted to the sale target for the month
'''
print("You have made", today_sale, "out of", monthly_target)
print("There is", monthly_target - today_sale, "left to make. Goodluck!")