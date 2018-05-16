#Laura Davis
#11 March 2016
#This program calculates a XXX% tip and a 6% tax on a meal price.
#The user will enter the meal price and the program will calculate tip, tax, and the total.
#The program will print the calculated values of tip, tax, and total.
#The total is the meal price plus the tip plus the tax.


#This is the main function.
def main():
	print "Welcome to the meal calculator program."
	print #prints a blank line
	mealPrice = input_meal()
	tip = calc_tip(mealPrice)
	tax = calc_tax(mealPrice)
	total = calc_total(mealPrice, tip, tax)
	print_info(mealPrice, tip, tax, total)
	
#This function will input meal price.
def input_meal():
	mealPrice = input("Enter the meal price $")
	mealPrice = float (mealPrice)
	return mealPrice

#This function will calculate tip at XXX% according to predetermined meal price ranges.
def calc_tip(mealPrice):
	if 	mealPrice > 25.00:
		tip = mealPrice * .22
	elif mealPrice > 17.00: 
		tip = mealPrice * .19	
	elif mealPrice > 12.00:
		tip = mealPrice * .16
	elif mealPrice > 6.00:
		tip = mealPrice * .13	
	else:	
		tip = mealPrice * .10
	return tip

#This function will calculate tax at 6%.
def calc_tax(mealPrice):
	tax = mealPrice * .06
	return tax
	
#This function will calculate tax, tip, and the total cost.
def calc_total(mealPrice, tip, tax):
	total = mealPrice + tip + tax
	return total

#This function will print tax, tip, the meal price, and the total.
def print_info(mealPrice, tip, tax, total):
	print "The meal price is $", mealPrice
	print "The tip is $", tip
	print "The tax is $", tax
	print "The total is $", total

#calls main.
main() 
