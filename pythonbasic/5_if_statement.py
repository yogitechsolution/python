# if it's hot
    #It's a hot day
    #Drink plenty of water
#otherwise if it's cold
    #It's a cold day
    #Wear warm cloths
#otherwaise
    #It's a lovely day!

is_hot = False
is_cold = True
is_cold = False

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm cloths")
else:
    print("It's a lovely day!")

print("Enjoy your day!")

temp = 20

if temp > 30:
    print("It's a hot day")
    print("Drink plenty of water")
elif temp > 20: #(20, 30)
    print ("It's a nice day")
elif temp > 10: #(10, 20)
    print("It's a bit cold")
else:
    print("It's cold!")
print("Done")

#o/p
#It's a lovely day!
#Enjoy your day!

#It's a bit cold
#Done