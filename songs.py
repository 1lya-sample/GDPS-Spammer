import requests
import asyncio
async def getSong(sid):
    endpoint = database
    data = {
        'songID': sid
    }
    headers = {'User-Agent': ''}
    r = requests.post(endpoint+"getGJSongInfo.php", data=data, headers=headers)
    print(r.text)

startpos = 600000
endpos = 99999999
print("Sample's GDPS Account Spammer") 
database = input("database url (for example: http://ps.fhgdps.com/Geometrykras/): ")
while startpos <= endpos:
    asyncio.run(getSong(startpos))
    startpos+=1
