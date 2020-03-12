import hilton_Debugger
from hilton_Debugger import print_Debug_String

def generateAuthPassphrase(str1,str2,str3,str4):
    """Str1: Password
       Str2: Date/Time
       Str3: /authenticate
       Str4: Username"""
    print_Debug_String(f"Generating passpharse with: {str1},{str2},{str3},{str4}")
    print_Debug_String(f"Returned: {str1}&{str2}&{str3}&{str4}")
    return f"{str1}&{str2}&{str3}&{str4}"