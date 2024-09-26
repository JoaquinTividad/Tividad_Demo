#The program will ask for the customer's loan amount and monthly salary.
loan_amount = (float(input("Please enter the desired loan amount:")))
monthly_salary = (float(input("Please enter your monthly salary:")))
eligibility = monthly_salary * 10

#Determine if the customer's salary is higher than or equal to 30,000.00 and the requested loan is less than or equal to 10 times their monthly salary
if(monthly_salary>=float(30000) and loan_amount<=(eligibility)):
    print("You are now eligible for a loan.")
    #If the customer is eligible, the program will ask how many months to pay and will add a 10% interest.
    months = int(input("Please enter the amount of months due payment:"))
    interest = loan_amount * 0.10
    new_loan_amount = loan_amount + interest
    print("Payment Amount:", new_loan_amount/months)
#if the customer is not eligible because their salary is lower than 30,000.00, announce that the salary is too low
elif(monthly_salary<30000):
    print("You are not eligible for a loan.")
    print("Reason: Salary is too low.")
#if the customer is not eligible because the loan requested is higher than 10x their monthly salary, announce that the loan amount request is too high.
elif(loan_amount>eligibility):
    print("You are not eligible for a loan.")
    print("Reason: Loan Amount Request is too high.")