#This code take percentage from user and give a grade as per percentage.

percentage=float(input("Enter Percentage: "))
if percentage<40:
  print("Grade F")
elif 40<=percentage<50:
  print("Grade E")
elif 50<=percentage<60:
  print("Grade D")
elif 60<=percentage<70:
  print("Grade C")
elif 70<=percentage<80:
  print("Grade B")
elif 80<=percentage<90:
  print("Grade A")
elif 90<=percentage<100:
  print("Grade A+")
