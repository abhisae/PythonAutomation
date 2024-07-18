# write a program that calculate and displays the letter
# grade for a given score
# A = 90 - 100
# B = 80 - 89
# C = 70 - 79
# D = 60 - 69
# F = 0 - 59


a=int(input("Enter the grade:"))
if(a>=90 and a<=100):
    print("Congrats you got A grade")
elif(a>=80 and a<=89):
    print("Congrats you got B grade")
elif(a>=70 and a<=79):
    print("Congrats you got C grade")
elif(a>=60 and a<=69):
    print("Congrats you got D grade")
elif(a>=0 and a<=59):
    print("Congrats you got F grade")
else:
    print("Invalid Score")
