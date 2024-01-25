import random
computer_move = random.randint(0,2)
rps = input(" choose r for rock p for paper and s for sisors: ")
if computer_move ==0:
	computer_move = "rock"
elif computer_move ==1:
	computer_move = "paper"
elif computer_move == 2:
	computer_move = "scisor"
	

if rps == "r" and computer_move=="rock":
	print(f"computer picked {computer_move} you picked rock its a draw")
elif rps == "r" and computer_move=="paper":
	print(f"computer picked {computer_move} you picked rock you lost")
elif rps == "r" and computer_move=="scisor":
	print(f"computer picked {computer_move} you picked rock its a draw")
	


if rps == "p" and computer_move=="rock":
	print(f"computer picked {computer_move} you picked paper you won")
elif rps == "p" and computer_move=="paper":
	print(f"computer picked {computer_move} you picked paper its a draw")
elif rps == "p" and computer_move=="scisor":
	print(f"computer picked {computer_move} you picked paper you lost ")
	

if rps == "s" and computer_move=="rock":
	print(f"computer picked {computer_move} you picked scisor you lost")
elif rps == "s" and computer_move=="paper":
	print(f"computer picked {computer_move} you picked scisor you won")
elif rps == "s" and computer_move=="scisor":
	print(f"computer picked {computer_move} you picked scisor its a draw")
	
