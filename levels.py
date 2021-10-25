import requests
from random import randint as rand
from base64 import b64encode as b64e

def postLevel(levelName, userName, levelDesc, levelLength, audioTrack, levelString, udid):
    endpoint = database
    data = {
        'gameVersion': 21,
        'userName': userName,
        'gjp': '',
        'levelID': 0,
        'secret': 'Wmfv3899gc9',
        'levelVersion': 1,
        'levelName': levelName,
        'levelDesc': levelDesc,
        'levelLength': levelLength,
        'audioTrack': audioTrack,
        'levelString': levelString,
        'udid': udid
    }
    headers = {'User-Agent': ''}
    r = requests.post(endpoint+"uploadGJLevel21.php", data=data, headers=headers)
    return r.text
def generateUDID():
    udid = "S"+str(rand(111111111, 999999999))+str(rand(111111111, 999999999))+str(rand(111111111, 999999999))+str(rand(111111111, 999999999))+str(rand(1,9))
    return udid

print("Sample's GDPS Levels Spammer") 
database = input("database url (for example: http://ps.fhgdps.com/Geometrykras/): ")
userName = input("custom username: ")
levelName = input("custom levelname: ")
levelDesc = input("custom description: ")
while True:
    l = postLevel(levelName, userName, levelDesc, 3, 4, "fwfwefwefwwef"+str(rand(111111111, 999999999)), generateUDID())
    print(l)
