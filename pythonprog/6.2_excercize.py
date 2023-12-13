#Weight Convertor program - Convert weight kgs to lbs and vice versa

weight = int(input("Weight: "))
unit = input("Kgs or Lbs: ")
if unit.upper() == "K":
    converted = weight / 0.45
    print("Weight in lbs: " + str(converted))
    print(f"Weight in lbs {converted} pounds")
else:
    converted = weight * 0.45
    print("Weight in kgs: " + str(converted))
    print(f"Weight in kgs {converted} kilos")

#o/P
#Weight: 76
#Kgs or Lbs: K
#Weight in lbs: 168.88888888888889
#Weight in lbs 168.88888888888889 pounds

#Weight: 170
#Kgs or Lbs: l
#Weight in kgs: 76.5
#Weight in kgs 76.5 kilos