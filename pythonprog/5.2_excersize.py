#Logical operators:
#if has_high_income and has_good_credit:
 #...
#if has_high_income or has_good_credit:
 #...
#if has_high_income and not has_criminal_record:
 #...

has_high_income = False
has_good_credit = True
has_criminal_record = False #False means - No criminal record


if has_high_income or has_good_credit:
    print("Eligible for loan")
else:
    print("Not eligible for loan")

if has_high_income and has_good_credit:
    print("Eligible for loan")
else:
    print("Not eligible for loan")

if has_good_credit and not has_criminal_record:
    print("Eligible for loan")
else:
    print("Not eligible for loan")

#o/p
#Eligible for loan
#Not eligible for loan
#Eligible for loan 