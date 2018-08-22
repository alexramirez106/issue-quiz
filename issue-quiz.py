userScore = 0

# Question 1 - Barbara Mikulski
question_1 = input("Was Barbara Mikulski the first woman endorsed by EMILY's List? If yes, please write 'Y'. If no, please write 'N'. : ")
if question_1 == "Y":
	userScore = userScore + 1
	print("Correct! Your score is " + str(userScore) + "!")
else:
	print("Sorry! That is incorrect. Your score is " + str(userScore) + ".")

while question_1 == "N":
    print("Try again!")
    question_1 = input("Was Barbara Mikulski the first woman endorsed by EMILY's List? If yes, please write 'Y'. If no, please write 'N'. : ")
    if question_1 == "Y":
	    userScore = userScore + 1
	    print("Correct! Your score is " + str(userScore) + "!")
    else:
	    print("Sorry! That is incorrect. Your score is " + str(userScore) + ".")

# Question 2 - Menfolk
question_2 = input("Does EMILY's List endorse or fundraise for pro-choice Democratic men? If yes, please write 'Y'. If no, please write 'N'. : ")
if question_2 == "N":
    userScore = int(userScore) + 1
    print("Correct! Your score is " + str(userScore) + "!")
else:
    print("Sorry! That is incorrect. Your score is " + str(userScore) + ".")

while question_2 == "Y":
    print("Try again!")
    question_2 = input("Does EMILY's List endorse or fundraise for pro-choice Democratic men? If yes, please write 'Y'. If no, please write 'N'. : ")
    if question_2 == "N":
        userScore = int(userScore) + 1
        print("Correct! Your score is " + str(userScore) + "!")
    else:
        print("Sorry! That is incorrect. Your score is " + str(userScore) + ".")

# Question 3 - Text 47717
question_3 = input("Does EMILY's List raise money through SMS/text? If yes, please write 'Y'. If no, please write 'N'. : ")
if question_3 == "Y":
    userScore = int(userScore) + 1
    print("Correct! Text JOIN to 47717! Your final score is " + str(userScore) + "!")
else:
    print("Sorry! That is incorrect.")

while question_3 == "N":
    print("Try again!")
    question_3 = input("Does EMILY's List raise money through SMS/text? If yes, please write 'Y'. If no, please write 'N'. : ")
    if question_3 == "Y":
        userScore = int(userScore) + 1
        print("Correct! Text JOIN to 47717! Your final score is " + str(userScore) + "! Great job!")
    else:
        print("Sorry! That is incorrect.")
