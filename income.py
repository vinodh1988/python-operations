income=float(input("enter income:"))
if(income> 3000000):
    print("Extreme Tax")
elif(income> 1000000 and income<= 3000000 ):
    print("More Tax")
elif(income>=500000 and income<=1000000):
    print("Moderate Tax")
else:
    print("No tax")