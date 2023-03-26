import random
import time

questions = {
    "How many times do muslims pray a day?": "5",
    "What is the Muslim holiday that entails fasting for 30 months?": "Ramadan",
    "What does 'Asalam wa alaikum' mean in english?": "May peace be upon you",
    "According to Muslims, who is the final Prophet (PBUH)?": "Muhammad",
    "What language was the quran delivered in?": "Arabic"
}

def play_game():
    max_guesses = 3
    time_limit = 10
    score = 0
    for question in random.sample(list(questions.keys()), len(questions)):
        print(question)
        for i in range(max_guesses):
            print("You have", time_limit, "seconds to answer.")
            start_time = time.time()
            answer = input("Guess #" + str(i + 1) + ": ")
            elapsed_time = time.time() - start_time
            if answer.lower() == questions[question].lower() and elapsed_time <= time_limit:
                print("Correct! You answered in", round(elapsed_time, 2), "seconds.")
                score += 1
                break
            elif elapsed_time > time_limit:
                print("Time's up!")
                break
            else:
                print("Incorrect. You have " + str(max_guesses - i - 1) + " guesses and", round(time_limit - elapsed_time, 2), "seconds left.")
    print("Your final score is:", score)

play_game()
