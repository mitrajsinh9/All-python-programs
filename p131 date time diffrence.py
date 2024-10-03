import datetime
today = datetime.date.today()
birthDate = datetime.date(1978, 9, 16)
age = today.year - birthDate.year
print(age)