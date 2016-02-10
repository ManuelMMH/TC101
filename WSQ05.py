F=int(input("What is the temperature in Fahrenheit?: "))
#Make an input represented by a variable ("F" in this example), then, type the temperature you want to evaluate (add "int" to convert the number into an integer, so it can be evaluated).

C=5*(F-32)//9
#Our second variable ("C") is the formula to convert from Fahrenheit degrees to Celsius degrees, so just include your variable in the formula and you're good.
#Tip: Use "//" on divison for evading float numbers like 35.77777777777.

print ("A temperature of",F,"degrees Fahrenheit is",C,"degrees in Celsius.")
#Do the first simple print, showing the two variables you got.

if C < 100:
    print("Water does not boil at this temperature (under typical conditions).")
if C > 100:
    print("Water will boil at this temperature (under typical conditions).")
#Time of "if"'s; the first one actually applies for every celsius temperature that is under 100 celsius degrees, if this condition applies, a sentence saying that water will not boil at the temperature we typed will be printed. So, in the second one, for every temperature that passes 100 celsius degrees, a sentence saying that water will boil at the temperature we typed will be printed. 
