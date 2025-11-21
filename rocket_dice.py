import random
# Initial player balance
balance = 1000

# Function to handle betting logic
def bet(bet_amount, balance):
    if bet_amount > balance:
        return "you cant bet more than you have dummy"
    if bet_amount <= balance and bet_amount > 0:
        balance -= bet_amount
        print(f"Bet of {bet_amount} accepted. your balance is now {balance}")
    
    num = int(input("Choose a number between 2 and 11: "))
    if num < 2 or num > 11:
        return "Invalid number chosen."
    over_under = input(f"Do you want to bet over or under {num}").lower()
    if over_under not in ['over', 'under']:
        return "Invalid choice. Please choose 'over' or 'under': ."
    return bet_amount, balance, num, over_under
    


# dice roll
def dice_roll():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    print(f"Dice rolled: {die1} and {die2}. Total: {total}")
    return total




# Multipliers for "over" and "under"
multipliers_over = {
    11: 35.3,
    10: 11.8,
    9: 5.88,
    8: 3.53,
    7: 2.35,
    6: 1.68,
    5: 1.36,
    4: 1.18,
    3: 1.07,
    2: 1.01
}

multipliers_under = {
    11: 1.01,
    10: 1.07,
    9: 1.18,
    8: 1.36,
    7: 1.68,
    6: 2.35,
    5: 3.53,
    4: 5.88,
    3: 11.8,
    2: 35.3
}


# game logic
def run_game(bet_amount, balance, num, over_under):
    if over_under == "over":
        if dice_roll() > num:
            win = True
            print(f"You win! {multipliers_over[num]}x")
            winnings = bet_amount * multipliers_over[num]
            balance += winnings
            print(f"Your balance is now {balance}")
        else:
            print("You lose!")
            print(f"Your balance is now {balance}")
            winnings = 0
            win = False
    elif over_under == "under":
        if dice_roll() < num:
            win = True
            print(f"You win! {multipliers_under[num]}x")
            winnings = bet_amount * multipliers_under[num]
            balance += winnings
            print(f"Your balance is now {balance}")
        else:
            print("You lose!")
            print(f"Your balance is now {balance}")
            winnings = 0
            win = False
    return balance, win, winnings
    
def risk(balance, winnings):
    print("-------------")
    print(f"you made {winnings}")
    run_risk = input("do you want to risk your winnings? (Y/N)").lower()
    
    if run_risk == "y":
        print("you will pick 3 numbers now and if the dice lands on one of those numbers you win.")
        risk_num = []
        for i in range(3):
            placeholder = int(input(f"pick number {i+1} (1-6): "))
            risk_num.append(placeholder)
        risk_outcome = random.randint(1,6)
        print(f"the die rolled a {risk_outcome}")
        if risk_outcome in risk_num:
            print("YOU WIN!!")
            print("will now recieve 2x your winnings of {winnings}")
            winnings *= 2
            balance += winnings
            print(f"your new balance is {balance}")
        else:
            print("you lost")
            balance -= winnings
    elif run_risk == "n":
        print("ok!")
    return balance
    
    

# Game stuff
print("ROCKET DICE V1.1.5")
print(f"Your starting balance is: {balance}")
while balance > 0:
    win = False
    bet_amount = round(float(input("Enter your bet amount: ")),2)
    bet_amount, balance, num, over_under = bet(bet_amount, balance)
    balance, win, winnings = run_game(bet_amount, balance, num, over_under)
    if win == True:
        risk(balance, winnings)
    
print("You are out of money! Game over.")




