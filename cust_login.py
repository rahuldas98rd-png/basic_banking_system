#this file is accessed after sucessful login or signup by the customer

import input_auth as inp
import main_file as main
import banking as bank

def login_menu(user_id,id,password,pos,user_details): #customer menu after successful login/signup
    print('\n1. VIEW PERSONAL DETAILS\n2. UPDATE PERSONAL DETAILS\n3. BANKING\n4. LOGOUT\n')
    option = inp.int_validation()
    if option == 1:
        view_data(user_id,id,password,pos,user_details)
    elif option == 2:
        update_data(user_id,id,password,pos,user_details)
    elif option == 3:
        bank.bank_menu(user_id,id,password,pos,user_details)
    elif option == 4:
        main.main_menu(user_id,password,user_details)
    
def view_data(user_id,id,password,pos,user_details): #function to view customer details
        print('\n____CUSTOMER DETAILS_____\n....PERSONAL DETAILS.....')
        print(f'\nCUSTOMER ID: {id}\nACCOUNT PASSWORD: {password[pos]}\nNAME: {user_details[id]['name']}\nAGE: {user_details[id]['age']}\nGENDER: {user_details[id]['gender']}\n....CONTACT DETAILS.....\n\nPHONE NUMBER: {user_details[id]['phone']}\nADDRESS: {user_details[id]['address']}\n\n.....FINANCIAL DETAILS.....\nAVAILABLE BALANCE: {user_details[id]['balance']}')
        login_menu(user_id,id,password,pos,user_details)

def update_data(user_id,id,password,pos,user_details): #function to update customer details
    print('\n____Enter what you want to update___')
    print('\nNAME\nPASSWORD\nPHONE NUMBER\nADDRESS')
    choice = input('enter your choice: ').strip().lower()
    if choice == 'name':
        value = input('Update your name: ').strip().lower()
        user_details[id]['name'] = value
        print('\nSUCCESSFULLY UPDATED\n')
    elif choice == 'password':
        value = input('Update your password: ').strip().lower()
        password[pos] = value
        print('\nSUCCESSFULLY UPDATED\n')
    elif choice == 'phone number':
        value = input('Update your phone number: ').strip().lower()
        user_details[id]['phone'] = value
        print('\nSUCCESSFULLY UPDATED\n')
    elif choice == 'address':
        value = input('Update your address: ').strip().lower()
        user_details[id]['address'] = value
        print('\nSUCCESSFULLY UPDATED\n')
    else:
        print('\nINVALID OPTION\n')
    login_menu(user_id,id,password,pos,user_details)