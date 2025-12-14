# this file is for login authentication like checking user_id, password and otp

import random as r
import main_file as main

def id_chk(id,user_id): # checking existing user or not
    for i in user_id:
        if i==id:
            pos =  user_id.index(i)
            return pos
    return -1

def password_chk(pos,password): # password Authentication
    attempt = 3
    while attempt>0:
        pwd = input('enter your password: ').strip()
        if password[pos]==pwd:
            return True
        attempt -= 1
        print('\nincorrect password')
        print(f'{attempt} attempts left')
    print('\nyou have exceeded max limit')
    main.main_menu()

def otp_chk(phone): # OTP Authentication
    attempt = 3
    while attempt>0:
        otp = r.randint(100000,999999)
        print(f'\notp has been sent to your registered mobile no.: {phone}\nyour otp is {otp}')
        get_otp = int(input('please enter your otp: ').strip())
        if get_otp==otp:
            return True
        attempt -= 1
        print('\nINVALID OTP!!')
        print(f'{attempt} attempts left')
    print('you have exceeded max limit')
    main.main_menu()
