#Weight Convertor program - Convert weight kgs to lbs

#weight = input("Weight: ")
#unit = input("Kgs or Lbs: ")
#if unit == "K":
    #converted = weight / 0.45  

#o/P
#TypeError: unsupported operand type(s) for /: 'str' and 'float'  - LINE 6


#weight = int(input("Weight: "))
#unit = input("Kgs or Lbs: ")
#if unit == "K":
    #converted = weight / 0.45
    #print("Weight in lbs: " + converted)

#o/P
#TypeError: can only concatenate str (not "float") to str - LINE 16

weight = int(input("Weight: "))
print(type(weight))
unit = input("Kgs or Lbs: ")
print(type(unit))
if unit.upper() == "K":
    converted = weight / 0.45
    print("Weight in lbs: " + str(converted))

#o/P
#Weight: 76
#Kgs or Lbs: K
#Weight in lbs: 168.88888888888889