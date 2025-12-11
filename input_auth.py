#this file is for user input authentication

def string_validation(): # code for yes & no validation
    while True:
        try:
            n = input('Enter choice: ').strip().lower()
            if n=='yes' or n=='no':
                return n
            else:
                print('please enter a valid option')
        except ValueError:
            print('please enter a valid option')

def int_validation(): # code for integer option validation
    while True:
        try:
            n = int(input('Enter your option: ').strip())
            if n==1 or n==2 or n==3 or n==4:
                return n
            else:
                print('enter valid option')
        except ValueError:
            print('enter valid option')