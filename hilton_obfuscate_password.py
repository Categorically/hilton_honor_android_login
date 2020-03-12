import random
import hilton_Debugger
from hilton_Debugger import print_Debug_String
random_Char_Set = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def obfuscatePassword(str1):
    """Str1: password"""
    print_Debug_String(f"Obfucating: {str1}")
    sb = ""
    for char in str1:
        sb += str(ord(char))
        sb += random.choice(random_Char_Set)
        sb += random.choice(random_Char_Set)
    length = 128 - len(sb)
    while 1:
        i = length-1
        if length <= 0:
            print_Debug_String(f"Returned: {sb[::-1]}")
            return sb[::-1]
        sb += random.choice(random_Char_Set)
        length = i