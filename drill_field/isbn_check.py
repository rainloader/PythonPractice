# this module checks isbn validity
def isbn_check(targetStr):
    result = "valid"
    length = len(targetStr)
# check 1st condition : first digit must be num, 'x', 'X', '-'
    if not targetStr[0] in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'x', 'X', '-') :
        result = "invalid"
# check 2nd condition : the digit before last digit must not 
    print (result)
