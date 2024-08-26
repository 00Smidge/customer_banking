# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from cd_account import create_cd_account
from savings_account import create_savings_account

# Define the main function
def main():
	"""This function prompts the user to enter the savings and cd account balance, interest rate,
	and the length of months to determine the interest gained.
	It displays the interest earned on the savings and CD accounts and updates the balances.
	"""

	# Prompt the user to set the savings balance, interest rate, and months for the savings account.
	# ADD YOUR CODE HERE
	savings_balance = input('\nPlease enter the balance for you savings account') or 10000
	print(f'You entered {savings_balance}\n')
	savings_interest = input('Please enter the interest for you savings account') or 0.9
	print(f'You entered {savings_interest}\n')
	savings_maturity = input('Please enter the maturity ( months ) for you savings account') or 12
	print(f'You entered {savings_maturity}\n')

	# Call the create_savings_account function and pass the variables from the user.
	create_savings_account(savings_balance, savings_interest, savings_maturity)

	# Print out the interest earned and updated savings account balance with interest earned for the given months.
	# ADD YOUR CODE HERE
	# interest_earned = savings.interest

	# Prompt the user to set the CD balance, interest rate, and months for the CD account.
	# ADD YOUR CODE HERE
	cd_balance = input('\nPlease enter the balance for you cd account') or 10000
	print(f'You entered {cd_balance}\n')
	cd_interest = input('Please enter the interest for you cd account') or 0.9
	print(f'You entered {cd_interest}\n')
	cd_maturity = input('Please enter the maturity ( months ) for you cd account') or 12
	print(f'You entered {cd_maturity}\n')

	# Call the create_cd_account function and pass the variables from the user.
		
	create_cd_account(cd_balance, cd_interest, cd_maturity)

	# Print out the interest earned and updated CD account balance with interest earned for the given months.
	# ADD YOUR CODE HERE

if __name__ == "__main__":
	# Call the main function.
	main()