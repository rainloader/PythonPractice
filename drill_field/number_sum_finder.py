def number_sum_finder():
    inputString = input('put numbers [ex)3 4 6 7 9] : ')
    numberList = [int(k) for k in inputString.split(' ')]
    numberList = sorted(numberList)
    print (numberList)
