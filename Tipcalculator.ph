print("********welcome to the tip calculator********")
t_bill = int(input("what was the total bill?"))
percent_bill = int(input("what percentage of tip would you like? 10 ,12 , 15  ?"))
ppl = int(input("how many people are gonna split the bill?"))

if percent_bill == 10 :
	print(f"each person should pay: {round(t_bill*1.10/ppl,2)} $")
elif percent_bill == 12 : 
	print(f"each person should pay: {round(t_bill*1.12/ppl,2)}  $")
else :
    print(f"each person should pay: {round(t_bill*1.15/ppl,2)} $")
