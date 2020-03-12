class debug:
    toggled = False

def print_Debug_String(string):
    if debug.toggled == True:
        print(string)
    else:
        pass