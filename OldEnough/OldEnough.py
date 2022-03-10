drivingAge = eval(input("What is the legal driving age where you live?\n"))
yourAge = eval(input("How old are you?\n"))
if yourAge>=drivingAge:
    print("You are old enough to drive!!")
if yourAge<drivingAge:
    print("Sorry, you cannot drive in ", drivingAge-yourAge, " Years!!")