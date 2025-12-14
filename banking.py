import input_auth as inp
import cust_login as cust
import login_auth as log

def bank_menu(user_id,id,password,pos,user_details): #banking menu for customer
    print('\n1. BALANCE ENQUIERY\n2. CASH DEPOSIT\n3. CASH WITHDRAWL\n4. LOGIN MENU')
    choice = inp.int_validation()
    if choice==1:
        bal_eq(user_id,id,password,pos,user_details)
    elif choice==2:
        deposit(user_id,id,password,pos,user_details)
    elif choice==3:
        withdrawl(user_id,id,password,pos,user_details)
    elif choice==4:
        cust.login_menu(user_id,id,password,pos,user_details)

def bal_eq(user_id,id,password,pos,user_details): #balance enquiry function
    print(f'\nyour available account balance is: {user_details[id]['balance']}')
    bank_menu(user_id,id,password,pos,user_details)

def deposit(user_id,id,password,pos,user_details): #cash deposit function
    amount = int(input('enter the amount you want to deposit: '))
    user_details[id]['balance'] += amount
    print('\nTRANSACTION SUCCESFULL!!\n')
    bank_menu(user_id,id,password,pos,user_details)

def withdrawl(user_id,id,password,pos,user_details): #cash withdrawl function
    if log.password_chk(pos,password):
        if log.otp_chk(user_details[id]['phone']): #OTP Authentication before withdrawl
            amount = int(input('enter the amount you want to withdraw: '))
            if amount<=user_details[id]['balance']:
                user_details[id]['balance'] -= amount
                print('\nTRANSACTION SUCCESFULL!!\n')
                bank_menu(user_id,id,password,pos,user_details)
            else:
                print('\ntransaction failed!!\nyour account balance is low\ndo you want to check your account balance?(yes/no)')
                choice = inp.string_validation()
                if choice == 'yes':
                    print(f'\nyour available account balance is: {user_details[id]['balance']}')
                    bank_menu(user_id,id,password,pos,user_details)
                else:
                    bank_menu(user_id,id,password,pos,user_details)