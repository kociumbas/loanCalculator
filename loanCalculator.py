amount = input ("Please, write the loan amount ")
payment = input ("Please, write the monthly payment ")
interest = input ("Please, write the interest rate ")
numPay = input ("Please, write the number of payments ")

cost = (float(amount)*float(interest)*(1+float(interest)))*float(numPay)/((1+float(interest)*float(numPay)-1))
print(cost)