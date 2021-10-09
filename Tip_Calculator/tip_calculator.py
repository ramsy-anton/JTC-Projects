#Asking user what is the total cost of the food and converting the total from a string to a float.
Cost = float(input('Total Cost of the food? '))

#Asking user the number of people splitting the bill and converting the total from a string to an integer.
People = int(input('Number of people splitting the bill? '))

#Asking user how much to tip and converting the amount to an integer.
Percent = int(input('Percentage of tip? '))

#Tax rate
Tax = 10

#Total tax of the bill
Total_tax = Cost / Tax

#Total bill cost with the tip
Cost_with_tip = (Percent / 100) * Cost + Cost

#Total cost per person inclusive of tip and tax. There is no tip on the tax!
Cost_per_person = ((Cost_with_tip + Total_tax) / People)

#Print the total bill rounded to 2 decimal places.
#Source: https://pythonguides.com/python-print-2-decimal-places/
print(f'Total bill: ${Cost_with_tip + Total_tax:.2f}')

#Print how much each person should pay rounded to 2 decimal places.
print(f'Each person should pay ${Cost_per_person:.2f}')