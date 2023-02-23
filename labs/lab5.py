print "To calculate how long you have been on Earth,please enter your birthday..."
bd_y = input("Year: ")
bd_m = input("Month (1-12): ")
bd_d = input("Date: ")

from datetime import date
now = date.today()

birthdate = date(int(bd_y), int(bd_m), int(bd_d))

age =  now-birthdate

print "YOu have been on earth for  %s" % age
