ans = input("what will you want to do S or A: ")

ans = ans.lower()


x = float( input("insert first num : "))
y =  float(input("insert second num: "))

if ans == "s":
   result = x-y
   print (f"{result}")
elif ans== "a":
   result = x * y
   print (f"{result}")

else: 
    print ("useyourhead")

