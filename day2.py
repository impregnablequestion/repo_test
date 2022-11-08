#GO TO WORK#
# SET is_it_raining = INPUT "is it raining?"
# IF is_it_raining is "yes"
#   THEN PRINT "You should take the car"
# ELSE 
#   IF distance <5
#       THEN PRINT "You should walk or cycle"
#   ELSE
#       THEN PRINT "You should get the bus"
#END#

distance = 6
is_it_raining = input("Is it raining?")

if is_it_raining == "yes":
    print("You should take the car")
elif distance < 5:
    print("You should walk or cycle")
else:
    print("Go on, take the bus")