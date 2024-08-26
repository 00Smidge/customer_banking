"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
from account import Account

def create_cd_account(balance, interest_rate, months):
    """Creates a CD account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.

    Returns:
        float: The updated CD account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    # Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE
    user_cd = Account(100000, 0.14)
    
    # Calculate interest earned
    # ADD YOUR CODE HERE
    interest_earned = user_cd.balance * user_cd.interest
    print(f'Your interest rate of {user_cd.interest_rate} will earn ${interest_earned} on a current balance of ${user_cd.balance}')
    
    # Update the savings account balance by adding the interest earned
    # ADD YOUR CODE HERE
    updated_balance = user_cd.balance + interest_earned

    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
    user_cd.set_balance(updated_balance)

    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
    user_cd.set_interest(interest_earned)

    # Return the updated balance and interest earned.
    print(f'After generating ${interest_earned} off interest your new balance is ${updated_balance}')

    # ADD YOUR CODE HERE
    return interest_earned, updated_balance
