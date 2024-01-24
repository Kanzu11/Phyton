print("welcome to the treasur island",
"your mission is to find the treasure")
left_right = input("you are across the road where do you wanna go : left , right?")
left_lower = left_right.lower()
if left_lower == "right":
	print("game over")
swim_wait = input("there is a river ahead : swim or wait ")
swim_lower = swim_wait.lower()
if swim_lower == "swim":
	print("game over")
choose_door =input("choose a door: red,blue,yellow")
choose_lower = choose_door.lower()
if choose_lower == "red" or "blue":
	print("game over")
else:
	print("congrats you won!!!")
