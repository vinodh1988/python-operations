# while loop 
#initialization
a=10

while a>=1:
    print(a,end=" ")
    a-=1   # in python there is no increment decrement operator

# loop to take continous user input

store=""
data=input("input string:")
while data!="EXIT":
      store+=data+"\n"
      data=input("Input String:")

print("The data you inserted is")
print("------------------------------------")
print(store)