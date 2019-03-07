import random


def getAnswer(answerNumber):

    if answerNumber == 1:
        return "It is certain"
    elif answerNumber == 2:
        return "Perhaps indeed"
    elif answerNumber == 3:
        return "Oh INDEED"
    elif answerNumber == 4:
        return "And so on."

#
# r = random.randint(1,4)
#
# fortune = getAnswer(r)
#
# print(fortune)

print(getAnswer(random.randint(1,9)))