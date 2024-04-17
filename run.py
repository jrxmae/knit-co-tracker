'''
A function made up of a welcome message for the user
'''
def welcome():
    print('Welcome to Sale Target Tracker!')
    print('With this program, you can input your daily sales and compare it to your monthly target')


'''
Calls welcome function to print the welcome message to the user
'''
welcome()

'''
Asks user for name of the month and the sale target amount
'''
month = input('Enter the name of the month: ')
monthly_target = int(input("Enter the sale target of the month: "))