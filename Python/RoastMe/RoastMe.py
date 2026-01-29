import Questions
import random

roast_points = 0
still_roasting = True

def ask_questions():
    random_question = random.randint(1,6)
    if random_question not in (3, 4):
        answer = input(Questions.question_bank[random_question]).lower()
        roast(random_question,answer)
    else:
        try:
            answer = int(input(Questions.question_bank[random_question]))
            roast(random_question,answer)
        except ValueError:
            print('WOW Genious that SUCH a Big BRAIN You Have There')
    
# Roast by Question Numbers lol

def roast(question_num,answer):
    global roast_points
    if question_num ==1:
        if answer == 'nothing' or answer == 'i wont say ':
            roast_points+=4
            print("Good Keep it that way [World hunger Dropping Rapidly (●'◡'●)]")
        elif answer=='hmmmmmm' or answer == 'i dont remember' or answer == 'idk' or answer == ' ':
            roast_points+=8
            print('OK Think Like You Do At Your Workplace... Keep Thinking')
        else:
            roast_points+=3
            print(f"OFCOURSE I could tell You Smell like {answer} (。_。)")
    elif question_num == 2:
        if answer == 'yes' or answer == 'yep' or answer == 'maybe':
            roast_points+=10
            print('This World is full of LIARS. Well do You know What... Nevermind no matter what you study you will never be employed')
        else:
            roast_points+=4
            print('I Know I Know Escaping is all You know! Atleast You are honest... ')
    elif question_num == 3:
            if answer == 0:
                roast_points+=4
                print('Yea if You did You wouldnt be Wasting Your Time here... Shameless ◑﹏◐')
            elif answer <= 4:
                roast_points+=6
                print("Really Now! dont worry i dont trust you (just like your parents) (●'◡'●)")
            elif answer <= 6:
                    roast_points+=2
                    print('Bruh Who Do You Think You are Fooling: Stop the Cap 🧢 IF only... you could Your Parents Would be Proud (IF Only)')
            else:
                roast_points+=10
                print('Well I wont Argue With A Liar Congratz you are the Next Chat GPT ( ˘︹˘ ) WELL? i dont care')
    elif question_num == 4:
        if answer> 0:
            roast_points+=5
            print('Sure Bud Everyone has A dream they cant achieve! but you are deliusional')
        else:
            roast_points+=14
            print('Cant you Face it? Go hide behind Your virtual GF/BF')
    elif question_num == 5:
        if answer == 'yes' or answer == ' ':
            roast_points+=1
            print('No Im not gonna judge you this time For real Unless you Lied Which i know you DID')
        else:
            roast_points+=9
            print('What can i Expect from You anyways! Your Workplace doesnt either oh you dont have a job or will have')
    elif question_num == 6:
        if answer == 'yes':
            roast_points+=2
            print('Keep Going Good Luck !!! No matter what you say i know you are dumb anyways ')
        elif answer == 'no':
            roast_points+=4
            print('SmartAss huh i mean go ahead touch some grass and never show your face Again Dumbshit')
        else :
            roast_points+=9
            print('I understand you are dumb i thought you could answer in Yes or No but well... Fuck you ￣へ￣')
    else:
        roast_points+=30 
        print('You ARE so ugly my Code broke the moment you opened it GET OUTTT')
    return roast_points
    
def check_meter():
    if roast_points < 19:
        print(Questions.random_roast[random.randint(1,6)])
    elif roast_points < 20:
        print('Get A Life Congratulations You Leveled Up in Proving You are Shameless')
    elif roast_points == 50:
        print('Stubburn Kid Quit Already')
    elif roast_points == 90:
        print('Unemployment, Shameles, No Life, Masochist, Choose one OH Fuck You Already are all of these')
    elif roast_points > 100:
        print('Unemployment Final Boss. Fine You Are the most loser person i have seen !! I QUIT.')
        global still_roasting
        still_roasting = False
    else:
        print('DumbASS')
    
while still_roasting:
    ask_questions()
    check_meter()
    