from data import data
from art import logo, vs

def game(data):
    score = 0
    game_over = False

    while not game_over:
        for item in range(len(data) - 1):
            A = data[item]
            B = data[item + 1]
            
            print(f"A: {A['name']}, a {A['description']}, from {A['country']}, with {A['follower_count']}M followers.")
            print(vs)
            print(f"B: {B['name']}, a {B['description']}, from {B['country']}, with {B['follower_count']}M followers.\n")

            
            guess = input("🔮 Who has more followers? Type 'A' or 'B': ").lower()
            
            if guess not in ['a', 'b']:
                print("❗ Invalid input. Please type 'A' or 'B'.")
                continue

            if (guess == 'a' and A['follower_count'] > B['follower_count']) or (guess == 'b' and B['follower_count'] > A['follower_count']):
                score += 1
                print(f"✅ You're right! Current score: {score} 🎉\n")
            else:
                print(f"❌ Sorry, that's wrong. Final score: {score} 😞")
                game_over = True
                break

            # Prepare for the next comparison
            item += 1
            A = B
            if item + 1 < len(data):
                B = data[item + 1]
            else:
                print("🏆 You've completed all comparisons! Final score: {score} 🎉")
                game_over = True
                break


# Start the game
print(logo)
print("Welcome to the Higher Lower Game!")
print("Can you guess which celebrity has more followers on Instagram? 🤔\n")

game(data)