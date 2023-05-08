#KBC game
import gtts
import playsound
import random
print("-----------Welcome to KBC------------")
name=input("Enter you name:")
# welcome=str(f"Welcome {name} to KBC.")
# sound = gtts.gTTS(welcome,lang="en")
# sound.save("welocme_note.mp3")
# playsound.playsound("welcome_note.mp3")
print(f"Welcome {name} to KBC.")
print("----------------Welcome to selection round--------------------")
print("Which is the highest Mountain in World?")
print("Options are: ")
print("a) Mt.Everest\t\t\t\tb) Lhotse\nc)Mount K2\t\t\t\td) Kanchanga")
a1=input("Enter your answer:")
if a1=='a':
    print(f'Congratulations {name}, You are selected for the game.')
    print("--------------------Let's begin the game,Your first question prize is 1000 ---------------")
else:
    print("Opps! you are not selected for the next round")
    exit()

#Questions ,Options and Answers are listed below:
questions=[{"question":"1)What is the capital city of Nepal?",
             "options":["A. Illam\t\t B. Biratnagar\nC. Kathmandu\t\t D.Dang\n"],
             "answer":"C"},
        { "question":"2)What is the capital city of India?",
            "options":["A. Illam\t\t B. Biratnagar\nC. Kathmandu\t\t D.New Delhi\n"],
            "answer":"D"},
        {"question":  "3)For which purpose the first computer was introduced in Nepal?" ,
            "options":["A. Entertaintment\t\t B. Census\nC. Hospitals\t\t\t D. Research\n"],
            "answer":"B" },]
#to identify whether 50-50 option is used or not!         
#displaying questions,options:
def display_quest(question):
  
    print(question["question"])
    for option in question["options"]:
        print(option)
    #check if 50-50 option is used or not?

#checking whether the answers is corect or not
def check_ans(question,answer):
    return question["answer"]== answer

#main part
def run_kbc(questions):
    prize=0
    for question in questions:
        display_quest(question)
        answer=input(("Choose your final answer:"))
        answer=answer.upper()
        # if answer.lower()==answer.upper():
        #     print(answer)
            # pass
        if check_ans(question,answer):
            print("----------------------------------------")
            prize+=1000
            print("Congratulations you gave the correct answer, you won Rs.\t", prize)
            print("-----------------------------------------")
        else:
            print("Opps! Your Answer is incorrect.\n")
            break
#function calling
run_kbc(questions)


