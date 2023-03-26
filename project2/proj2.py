def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("Correct Answer")
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("Sorry Wrong Answer, try again")
            attempt = attempt + 1
    if attempt == 3:
        print("The Correct answer is ",answer )
    
score = 0
print("Islamic Quiz: Increase your knowldge during the holy month!")
guess1 = input("How many time do muslims pray a day? ")
check_guess(guess1, "5")
guess2 = input("What is the Muslim holiday that entails fasting for 30 months? ")
check_guess(guess2, "Ramadan")
guess3 = input("What does 'Asalam wa alaikum' mean in english? ")
check_guess(guess3, "May peace be upon you")
guess4 = input("According to Muslims, who is the final Prophet (PBUH)?")
check_guess(guess4, "Muhammad")
guess5 = input("What language was the quran delivered in?")
check_guess(guess5, "Arabic")
print("Your Score is "+ str(score))
