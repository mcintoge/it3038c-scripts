from datetime import date
import holidays


#Ask User for date
#Ask user for state initials
us_holidays = holidays.UnitedStates()

print ("Hello, what date would you like to check for a Holiday?")

input_date = input("YYYY-MM-DD:")

holiday_name = us_holidays.get(input_date)

if holiday_name != None:
	output = "{} is a US Holidays. It's {}".format(input_date, holiday_name)
else:
	output = "{} is not a US Holiday".format(input_date)
	
print (output)

print('-----------------------------------------------------------------')

print ("To view the Holiday calendar year, please enter a state code, by its initials (such as, OH).")          

input_state = input("Sate Initials:") 

for day, name in sorted(holidays.USA(years=2023, state= input_state).
items()):
	print(day, name)      
	
	
	
#Citations
#https://pypi.org/project/holidays/ holiday library documentation
#https://www.geeksforgeeks.org/python-holidays-library/ Helped with for statement
#https://www.javatpoint.com/python-holidays-module 
#https://www.javatpoint.com/python-holidays-module

                                                                         
																		                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   