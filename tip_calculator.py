# This is a tip calculator I'm creating as an exercise from CodeAcademy, but using
# user input through the command line.

meal = raw_input("How much was that meal? > ")
tip = raw_input("How much would you like to tip? 15%, 18%, 20%? > ")

meal = float(meal)
tip = float(tip)

tip = tip * .01
total_tip = meal * tip
total = total_tip + meal

print "You should tip $%r." % total_tip
print "Your total is $%r." % total
