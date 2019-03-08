c = input("Enter a character : ")
if(c >= 'a' and c <= 'z'):
    print("Lowercase Alphabet")
elif (c >= 'A' and c <= 'Z'): 
    print("Uppercase Alphabet") 
elif(c >= '0' and c <= '9'):
    print("Number")
else:
    print("Special Character")
