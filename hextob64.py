"""Hexadecimal -> Base64"""
b64map = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "/", "="]

hexAlphas = {
    "a" : 10,
    "b" : 11,
    "c" : 12,
    "d" : 13,
    "e" : 14,
    "f" : 15
}

stringIn = raw_input("Enter String>>")  #input string

binaryChars = ""        #string to hold binary of char values

brokenArr = []          #Array to hold 6bit values from binaryChars

cnt = 0                 #counter var

combined = ""           #used to help break into 6bit

baseOut = ""            #return result

padded = False          #bool to know if padding was used

dpad = False            #need to know if you use 2 '='s 

###Hex to Binary Function
def h2b(hexIn):
    """Hexadecimal to Binary"""
    cnt = 0     #Reset counter just in case
    
    hbOut = ""  #initialize return value
    
    while cnt < len(hexIn):
        if hexIn[cnt] in hexAlphas:    
            hbOut += d2b(hexAlphas[hexIn[cnt].lower()])
    
        else:            
            hbOut += d2b(hexIn[cnt])
        cnt += 1            

    return hbOut

def d2b(decimalIn):
    """ Decimal to Binary function"""    
    #initialize remainder
    rem = 0

    dec = int(decimalIn)
    
    #string to store binary value
    binval = ""

    while dec > 0:
        rem = dec % 2 #remainder
        dec = dec / 2
    
        binval += str(rem)

    #Need length of binval for appropriate output 
    binLength = len(binval)

    #Depending on size of binval, pad with zeros for 4bits
    if binLength < 4 and int(decimalIn) < 16:
        padamt = 4 - len(binval)    
        binval += "0"*padamt

    #Reverse binary string for appropriate value
    binval = binval[::-1]

    return binval

def b2d(binIn):
    """Binary to Decimal"""
    
    cnt = 0     #init counter    

    decVal = 0  #init return decimal value
    
    revbin = binIn[::-1] #Need to reverse input binary for fn

    while cnt < len(binIn):
        if int(revbin[cnt]) is 1:
            decVal += 2**cnt
    
        cnt += 1  #increment x

    return decVal
##/Fn

#Get binary of each character
for x in stringIn:
    binaryChars += h2b(x)

#Need to pad with zeros at the end if not a multiple of 6
if len(binaryChars)%6 != 0:
    binaryChars += "0"*(len(binaryChars)%6)
    padding = True

lencount = 0    #counter

#Now we need to break the binary into 6bit strings
while cnt < len(binaryChars) - 1:
    combined += binaryChars[cnt]
    if (cnt > 0) and (len(combined) % 6 == 0): 
        brokenArr.append(combined)
        combined = ""   #Reset var
        lencount += 6

    cnt += 1

last = ""               #temp arr to hold remaining characters

#if there are any leftover binary vals, append them
if lencount < len(binaryChars):
    last = binaryChars[lencount:len(binaryChars)]    
    brokenArr.append(binaryChars[lencount:len(binaryChars)])
    
    #If there is no "1" in the last array item,
    #base64 requires 2 = chars at the end    
    if "1" in last:
        dpad = False
    else:
        dpad = True
    
#Now get base64 values!
for bins in brokenArr:
    baseOut += b64map[b2d(bins)]

#if padding was used, append "=" char
if (padded is True) and (dpad is False):
    baseOut += "="
elif (padded is True) and (dpad is True):
    baseOut += "=="


#Finally print value
print baseOut
