"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
from account import Account  # noqa: F401

# Define a function for the Savings Account
def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.
    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.
    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """

    # calculate the interest earned based on user input, update the account balance with the earned interest, and return the updated balance and interest earned.
    
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    # Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE
    user_savings = Account(balance, interest_rate, months)
    
    # Calculate interest earned
    # ADD YOUR CODE HERE
    interest_earned = user_savings.balance * user_savings.interest_rate
    print(f'Your interest rate of {user_savings.interest_rate:.2f} will earn ${interest_earned:.2f} on a current balance of ${user_savings.balance:.2f}.\n')
    
    # Update the savings account balance by adding the interest earned
    # ADD YOUR CODE HERE
    updated_balance = user_savings.balance + interest_earned

    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
    user_savings.balance = updated_balance

    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
    user_savings.interest_rate = interest_earned 

    # Return the updated balance and interest earned.
    # ADD YOUR CODE HERE
    return interest_rate, updated_balance