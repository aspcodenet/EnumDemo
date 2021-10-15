def getInputBetween(startval: int,endval: int)->int:
    while True:
        try:
            val=int(input("Mata in:"))
            if val >= startval and val <= endval:
                return val
            print(f"Ogiltigt val, mellan {startval} och {endval}, tack")
        except:
            print("Ange ett tal tack!")

print("1. Si")            
print("2. Så")            
print("3. Avslu")            
sel = getInputBetween(1,3)

print("1. Si")            
print("2. Så")            
print("3. What")            
print("4. Avslu")         
sel = getInputBetween(1,4)   
