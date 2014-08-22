def pycha_02(string):
    letterString = 'abcdefghijklmnopqrstuvwxyz'
    resultString = ""
    for char in string:
        if char in letterString:
            position = letterString.find(char)
            resultString += letterString[(position+2)%26]
        else:
            resultString += char
    return resultString


            
