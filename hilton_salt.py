import hilton_Debugger
from hilton_Debugger import print_Debug_String

def generateAuthSalt(str1,str2,str3):
    """Str1: Timestamp
        Str2: HILTON_AUTH_CLIENT_ID
        Str3: HILTON_ACCESS_TOKEN"""
    print_Debug_String(f"Generating salt with: {str1},{str2},{str3}")
    sb = ""
    sb2 = str1[::-1]
    i = 0
    i2 = 0
    i3 = 0
    while i < 5:
        sb += sb2[i2+1:i2 + 3]
        i4 = i3 + 1
        i5 = i3 + 5
        sb += str2[i4:i5]
        sb += str3[i4:i5]
        i += 1
        i2 = i *2
        i3 = i *4
    sb += str2[::-1][1:8]
    sb += str3[::-1][1:8]
    print_Debug_String(f"Returned salt: {sb.lower()}")
    return sb.lower()