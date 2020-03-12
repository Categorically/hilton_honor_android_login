import random
import os
from binascii import b2a_hex
import time
import requests
from requests import Timeout
import hilton_Debugger
from datetime import datetime
from hilton_access_token import get_Access_Token
from hilton_salt import generateAuthSalt
from hilton_passphrase import generateAuthPassphrase
from hilton_hmac import hmac_Token
from hilton_obfuscate_password import obfuscatePassword
#Disable debugger prints
hilton_Debugger.debug.toggled = True

#Akamai sensor data
sensor_Data = ""

#A random Android device id
android_Id = b2a_hex(os.urandom(8)).decode("utf-8")[:15]

#Call access token. Parsing access_Token, issued_Date for salting
access_Token,issued_Date = get_Access_Token(android_Id,sensor_Data)

#Salting issued_Date, client_Id, access_Token
salt = generateAuthSalt(str(issued_Date),"E0j9ibsjpULYqOWCekfrw8TdzGPoOJRy",str(access_Token))

#ISO 8601 format for passphrase
date_Timestamp = str(time.time())[:14]
datetime_object = datetime.fromtimestamp(float(date_Timestamp))
date_Time = datetime_object.strftime("%Y-%m-%dT%H:%M:%SZ.%f")[:23] + "Z"

#Username and password for passphrase
username = ""
password = ""

#Creating passphrase from password,date_Time,path,username
passphrase = generateAuthPassphrase(password,date_Time,"/authenticate",username)
 
#Create Hptoken from passphrase, Salt
hptoken = hmac_Token(passphrase,salt).hex()

#Create the obfucated password
obfuscated_Password = obfuscatePassword(password)

#Final headers are the following
headers = {"Accept-Encoding": "gzip",
            "User-Agent": "HHonors/3.11.1 Dalvik/2.1.0 (Linux; U; Android 8.0.0; Samsung Galaxy S7 Build/OPR6.170623.017)",
            "Content-Length": "0",
            "DeviceID": android_Id,
            "hhonorsId": username,
            "hptoken": obfuscated_Password,
            "timestamp": date_Time,
            "token": hptoken,
            "x-acf-sensor-data": sensor_Data,
            "x-hilton-upsell": "true",
            "Authorization": f"Bearer {str(access_Token)}"}
url = "https://prd.hiltonapi.com/hhonors/v1/loyalty/authenticate"
try:
    hilton_Request = requests.post(url=url,headers=headers,timeout=5)
except Timeout:
    #When sensor data is banned hilton will timeout
    print("Connection timed out")
if 'ErrorCode":"022"' in hilton_Request.text:
    print("Failed login")
elif 'StatusMessage":"Success"' in hilton_Request.text:
    print("Successful login")
else:
    print("Error while calling hilton authenticate")