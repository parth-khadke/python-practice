print("*** Interest Calculator ***")
print("This program calculates simple and compound interest.")
print("Rate of interest is fixed at 5%pa. Compunding frequency is semi-annual.")
principal = float(input("Enter the principal amount: "))
term= int(input("Enter the term in years: "))
print()
rate= 0.05
n=2  # compounding frequency per year
simple_interest= principal * rate * term
compound_interest= principal * (1 + rate/n)**(n*term) - principal
print("Simple Interest on {:.2f} for {} years is: {:.2f}\n".format(principal, term, simple_interest))
print("Compound Interest on {:.2f} for {} years is: {:.2f}\n".format(principal, term, compound_interest))