import input_auth as inp
import login_auth as log
import cust_reg as reg
import cust_login as cust

user_id = ['1101','1102','1103','1104','1105','1106']
password = ['aaa','bbb','ccc','ddd','eee','fff']

user_details = {
    '1101':{'name':'rakesh','age':22,'gender':'male','phone':35465431,'address':'siliguri-98698','balance':12000},
    '1102':{'name':'suresh','age':26,'gender':'male','phone':32132131,'address':'bangalore-98698','balance':15000},
    '1103':{'name':'ramesh','age':30,'gender':'male','phone':68786736,'address':'mumbai-223243','balance':18000},
    '1104':{'name':'sunita','age':28,'gender':'female','phone':443386736,'address':'pune-777243','balance':25000},
    '1105':{'name':'sushil','age':45,'gender':'male','phone':68786736,'address':'mumbai-223243','balance':18000},
    '1106':{'name':'rimi','age':32,'gender':'female','phone':68786736,'address':'mumbai-223243','balance':55000}
}

def login(user_id,password,user_details): #login function
    id = input('enter user id:')
    pos = log.id_chk(id,user_id)
    if pos>=0:
        if log.password_chk(pos,password):
            if log.otp_chk(user_details[id]['phone']):
                print('\nyou have successfully logged into your bank account')
                cust.login_menu(user_id,id,password,pos,user_details)
    else:
        print('entered user id does not exist\nDo you want to signup?(yes/no)')
        choice = inp.string_validation()
        if choice=='yes':    
            reg.signup(user_id,password,user_details)
        else:
            print('THANK YOU\nVISIT AGAIN')

def main_menu(user_id,password,user_details):
    print('\n________WELCOME TO INDIAN BANK________\n\n1. LOGIN\n2. SIGN UP\n3. EXIT PROGRAM')
    choice = inp.int_validation()
    if choice==1:
        login(user_id,password,user_details)
    elif choice==2:
        reg.signup(user_id,password,user_details)

if __name__=='__main__':
    main_menu(user_id,password,user_details)