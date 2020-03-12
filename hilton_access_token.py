import random
import requests
import re
import hilton_Debugger
from hilton_Debugger import print_Debug_String
def get_Access_Token(android_Id,sensor_Data):
    print_Debug_String("Calling access token")
    url = "https://prd.hiltonapi.com/v1/oauth/accesstoken?grant_type=client_credentials"
    headers = {"Accept-Encoding": "gzip",
            "User-Agent": "HHonors/3.11.1 Dalvik/2.1.0 (Linux; U; Android 8.0.0; Samsung Galaxy S7 Build/OPR6.170623.017)",
            "DeviceID": android_Id,
            "x-acf-sensor-data": sensor_Data,
            "x-hilton-upsell": "true",
            "Authorization": "RTBqOWlic2pwVUxZcU9XQ2VrZnJ3OFRkekdQb09KUnk6cElnbWlkUHM5UDNqZW5LOQ=="}
    access_Token_Text = requests.get(url=url,headers=headers).text
    access_Token = re.search('access_token":"(.*?)"',access_Token_Text).group(1)
    issued_Date = re.search('issued_at":"(\\d+)"',access_Token_Text).group(1)
    print_Debug_String(f"Access token returned: {access_Token}")
    print_Debug_String(f"issued_Date returned: {issued_Date}")
    return [access_Token,issued_Date]