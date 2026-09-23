Age = int(input("Please tell me your age : "))

i = 0
while i <= 30 :
	if i == 0:
		print(f"You are currently {Age} years old")
	else:
		print(f"In {i} years, you'll be {Age + i} years old")
	i += 10
