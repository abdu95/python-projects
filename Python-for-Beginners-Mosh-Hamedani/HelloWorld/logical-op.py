#  If an applicant has high income and good credit,
#  then they're eligible for a loan

# AND: both
# OR: at least one
# NOT:

has_high_income = False
has_good_credit = True

# if has_high_income and has_good_credit:
#     print("Eligible for loan")
# else:
#     print("Not eligible")

if has_high_income or has_good_credit:
    print("Eligible for loan")
else:
    print("Not eligible")


has_criminal_record = True

if has_good_credit and not has_criminal_record:
    print("Eligible for loan")
else:
    print("Not eligible")