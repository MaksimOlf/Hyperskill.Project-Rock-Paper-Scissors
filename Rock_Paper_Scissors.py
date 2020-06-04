# Write your code here
import random
name_1 = input("Enter your name: ")
print(f"Hello, {name_1}")
asd = open("rating.txt", "r")
score = int(0)
for line in asd:
	if name_1 in line:
	    line = line.split()
	    score = line[1]
asd.close()
b = input().split(",")
if b == [""]:
	print("Okay, let\'s start")
	while True:
		p_choose = str(input())
		list_1 = ["rock", "paper", "scissors"]
		ii_choose = random.choice(list_1)
		if p_choose == "!exit":
			print("Bye!")
			break
		elif p_choose == "!rating":
			score = str(score)
			print(f"Your rating: {score}")
			score = int(score)
		elif p_choose == ii_choose:
			print(f"There is a draw ({p_choose})")
			score = int(score)
			score += 50
		elif p_choose == "rock":
			if ii_choose == "scissors":
				print("Well done. Computer chose scissors and failed")
				score = int(score)
				score += 100
			elif ii_choose == "paper":
				print("Sorry, but computer chose paper")
		elif p_choose == "scissors":
			if ii_choose == "rock":
				print("Sorry, but computer chose rock")
			elif ii_choose == "paper":
				print("Well done. Computer chose paper and failed")
				score = int(score)
				score += 100
		elif p_choose == "paper":
			if ii_choose == "rock":
				print("Well done. Computer chose rock and failed")
				score = int(score)
				score += 100
			elif ii_choose == "scissors":
				print("Sorry, but computer chose scissors")
		else:
			print("Invalid input")
else:
	print("Okay, let\'s start")
	while True:
		ii2_choose = random.choice(b)
		s = b.index(ii2_choose)
		s += len(b)
		g = (len(b) - 1) // 2
		h = (len(b) + 1) // 2
		b_3 = b + b + b
		win_2 = b_3[s-g:s]
		lose_2 = b_3[s+1:s+h]
		pp_choose = str(input())
		if pp_choose == ii2_choose:
			print(f"There is a draw ({ii2_choose})")
			score = int(score)
			score += 50
		elif pp_choose in win_2:
			print(f"Sorry, but computer chose {ii2_choose}")
		elif pp_choose in lose_2:
			print(f"Well done. Computer chose {ii2_choose} and failed")
			score = int(score)
			score += 100
		elif pp_choose == "!exit":
			print("Bye!")
			break
		elif pp_choose == "!rating":
			score = str(score)
			print(f"Your rating: {score}")
			score = int(score)
		else:
			print("Invalid input")