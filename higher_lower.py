import art3,random
from game_data import data

def formate_data(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name},a {account_description},from {account_country} "

def answer(option,followers_1,follower_2):
    if followers_1 > follower_2:
        return option == "a"
    else:
        return option == "b"

print(art3.logo)
score = 0
account_b = random.choice(data)

while True:
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A:{formate_data(account_a)}")
    print(art3.vs)
    print(f"Compare B:{formate_data(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    print("_" *100)

    follower_a = account_a["follower_count"]
    follower_b = account_b["follower_count"]

    check_answer = answer(guess,follower_a,follower_b)
    if check_answer:
        score += 1
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        break







