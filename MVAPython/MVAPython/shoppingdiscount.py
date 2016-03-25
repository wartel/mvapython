#This code is used to calculate if shopping costs has to be charged

shippingCosts = 10
shippingCosts = float(shippingCosts)
#Ask user for the shopping amount
purchaseAmount = input("Please enter the total amount of purchases: ")
purchaseAmount = float(purchaseAmount)
#Check if amount is under 50
if purchaseAmount < 50 :
    totalAmount = purchaseAmount + shippingCosts
    print("The total amount with shipping costs is {0:.2f}".format(purchaseAmount))
else :
    print("The total amount is {0:.2f}".format(purchaseAmount))