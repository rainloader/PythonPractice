def pycha_03(string):
    charDic = {};
    for char in string:
        if charDic.get(char, "None") == "None":
            charDic[char] = 1
        else:
            charDic[char] += 1
    for key in charDic.keys():
        if charDic[key] == 1:
            print (key)

    

