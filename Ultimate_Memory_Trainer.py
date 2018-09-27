"""REMEMBERING NUMBERS GAME
for Doc Volz's Magical Memory System - goes from white, to yellow, orange, green, blue,
brown, black belts in each individual memory skill
The Peg system for remembering numbers:
- It does it ten numbers at a time - First teaches you the first ten one at a time
and asks you to remember something to peg the number to the word. Visual and emotional
- Once you have taken some time to memorize the 1st ten numbers it does a multiple choice
game where you have to pick out the correct peg word
- Once you can get them 100% correct you go on to the fill-in-the-blanks version of the game
- Once you get that 100% correct you qualify to go on to the next block of 10 numbers
    taught one at a time
    then multiple choice
    then fill in the blanks
    then multiple choice with all 20
    when 100% fill in the blanks with all 20
    then next 10... etc.
    until you are all the way up to all 100 numbers and then beat that level
    that would be like a brown belt when you can do it 3 days in a row
then you go to being flashed different numbers of different digit length
    and have to tell the computer what a four digit number was...
    and then 8... and then 10
    Once you can do a certain number like 10 in a row you get black belt

Game will remind you of which letters represent which numbers.
Then it will show you numbers and four choices of words one of which is the
code word/image for that number and the player must pick which one is correct.
It will do that ten times.
Next it will show you a word and you have to type in the correct number that
goes with that word.
Game will give you a final score out of 20.
Later it will start timing you for how long it takes you to figure out the
word or the number.
Later still it can give you a progressively longer string of numbers for
a decreasing length of time and you gain points.
Next it will store your scores to see how you do over time.
Finally it will integrate with your phone book and you can start memorizing
people's phone numbers
future games can include remembering names and faces
Basically turn all of Harry Lorraine's book into a memory game suite!
- Later games can include pictures/people names - most important people
done first with constant reinforcement.  Others can be random for common names
and then latter gotten from facebook.
- Market this to therapists who are working with alzheimer's patients - either
free, get a grant, or at a discount.
- black belts should be able to memorize a list of 10 phone numbers in 10 seconds and repeat them back 30 minutes later(?)
Something outrageous like that
"""

#DO - BUG FIXES
# - the list in multiple choice game 1 sometimes doesn't insert the correct answer and leaves one blank?!


##########################################################################################################################
#DEFINITION OF FUNCTIONS
##########################################################################################################################


#bring in random integer generator from random and tkinter for GUI later

from random import randint
from tkinter import *

score=0
attempts= 0
used_numbers=[]
global choice
choice=["skip","a","f","b","g","c","h","d","i","e","j"]
player_guess=""



#establish a list variable for numbers 1-100
number = [ii for ii in range(1,101)]

#establish a list variable for the peg words for 1-100
peg =["zoo","tie","Noah","Moe","rye","law","shoe","cow","ivy","bee","toes","tot","tin","time","tire","towel","dish","tack","dove","tub","nose","knot","nun","name","Nero","nail","notch","neck","knife","knob","mouse","mat","moon","mummy","mower","mule","match","mike(microphone)","movie","map","rose","rod","rain","ram","rower","roll","roach","rock","roof","rope","lace","lot","lion","lamb","lure","lilly","leech","log","lava","lip","cheese","sheet","chain","chum","cherry","shell","choo choo","shack","chef","ship","kiss","kite","coin","comb","car","coal","cash","cake","cave","cape","fuzz","fit","vine","foam","fur","file","fish","fog","fife","fob","bus","bat","bean","beam","bear","bell","beach","book","puff","pipe","disease"]

#for ii in range(1,100):
 #   print("{} is {}".format(number[ii],peg[ii]))   # to test


def get_rand():
    #picks a random number from 1-100
    rand=randint(1,100)
    return rand

def unique_number():
    #generates a random number we haven't used yet and adds to list of used numbers
    global used_numbers
    while True:
        num=get_rand()
        if num not in used_numbers:     
            used_numbers.append(num)   #if it isn't add it to the list 
            break                       #and use this random number
    return num

def gen_10_rnd_words(unique_num):
    #makes up 10 multiple choice words where one is correct
    #generates a list of 9 random words then inserts unique_num into random spot
    global rnd_word_list
    global rnd_position
    rnd_word_list=[""]
    ii=1
    while ii<10:
        rnd1=get_rand()
        if unique_num != rnd1:
            rnd_word_list.append(peg[rnd1])
            ii+=1
    rnd_position=randint(0,9)
    rnd_word_list.insert(rnd_position,peg[unique_num])

def print_10_rnd_words(rnd_word_list):
    for ii in range(1,10,2):
        print("{}: {}".format(choice[ii],rnd_word_list[ii]),"\t\t\t","{}: {}".format(choice[ii+1],rnd_word_list[ii+1]))




##########################################################################################################################
#GAME INTRODUCTION
##########################################################################################################################
for ii in range(10):
    print("\n")

intro_text="DOC VOLZ'S MAGICAL MEMORY MENTAL MAGNIFIER! \n\nWelcome to a new concept in classical memory training.\n"
intro_text=intro_text+"For thousands of years monks, bards, and generally super-clever people spent years training their memory.\n"
intro_text=intro_text+"It enabled them to give long speeches with confidence, reproduce long sections of religious works before the\n"
intro_text=intro_text+"printing press, learn ballads, impress members of the opposite sex, get phone numbers and remember them\n"
intro_text=intro_text+"once they did.\n\nIn todays day and age you might wonder why we need such memory tools when we can look things\n"
intro_text=intro_text+"up so easily.  And you are right insofar as we live in the information age and practically speaking we may not\n"
intro_text=intro_text+"need a finely tuned memory machine inside of our heads.  But we also live in an age where lifespans out live our\n"
intro_text=intro_text+"mental acuity.  As with any muscle the memory gets stronger when it is worked out and saggy and weak when it is\n"
intro_text=intro_text+"neglected.  There is a growing body of research showing than those who work on problem solving and memory \n"
intro_text=intro_text+"training techniques can reduce or improve or at least slow down the symptoms of alzheimers.  Spaced retrieval\n"
intro_text=intro_text+"especially has been shown to be helpful.\n\n"
intro_text=intro_text+"And although our educational system may be headed towards more problem-solving and less memorization, there\n"
intro_text=intro_text+"are still plenty of teachers that want you to remember this or that.\n\n"
intro_text=intro_text+"There are also many professions that can benefit from a well-trained mind.  What if you are a police officer and you\n"
intro_text=intro_text+"witness a perptrator commit a crime?  How helpful would it be to be able to instantly remember a licence plate at a \n"
intro_text=intro_text+"glance?  Or you single people - seriously how cool would it be to remember a person's phone number at the beach when\n"
intro_text=intro_text+"you don't have a phone or a pen?  There are plenty of good reasons to improve your memory and that's why I have put\n"
intro_text=intro_text+"this little game together.  If you like it I will make more becasue there is sooooo much more we can do.\n\n"
intro_text=intro_text+"Honestly though... I made this primarily for me.  I have always had a lousy memory and I think it's kind of cool to\n"
intro_text=intro_text+"be able to snub your nose at genetics and strengthen what we are weak in.  'If I can't I must' is a great old adage\n"
intro_text=intro_text+"after all.  If I get good enough at this it will make a great party trick - along with remembering names which I will\n"
intro_text=intro_text+"be working on next!\n\nFinally, before I begin I would like to say thanks to Harry Lorayne and Jerry Lucas for their\n"
intro_text=intro_text+"text 'The Memory Book' without which this and future games would not be possible.\n\n"

mental_training_explain="This is a game to help you learn how to remember numbers using what is called the peg system.  Normally remembering \n"
mental_training_explain=mental_training_explain+"numbers is difficult because they are somewhat abstract posessing no meaning and holding no emotions for\n"
mental_training_explain=mental_training_explain+"us.  So a great way to change that is to change the numbers into words that have meaning and attach emotions\n"
mental_training_explain=mental_training_explain+"to them.  The brain remembers things with emotions attached.  So this part of the game is about memorizing\n"
mental_training_explain=mental_training_explain+"a system of letters for numbers.  That will give you something to picture.  And when you can picture the\n"
mental_training_explain=mental_training_explain+"numbers that is what we call a 'peg'.  For instance every time I see or hear the number 11 I thinkg 'tot' \n"
mental_training_explain=mental_training_explain+"like tater tot.  That reminds me of the taste and a favorite restaunt of mine and times friends and I have\n"
mental_training_explain=mental_training_explain+"gone there.  It's clear in my mind.  If I combine that picture with others it becomes something memorable\n"
mental_training_explain=mental_training_explain+"and I can remember longer digit numbers.\n\n"
mental_training_explain=mental_training_explain+"That is the basic idea.  However it takes practice.  REAL practice!\n\nHave you seen the new Sherlock Holmes\n"
mental_training_explain=mental_training_explain+"series?  Remember when he talked about going to his 'mind palace' where he could remember so many details?\n"
mental_training_explain=mental_training_explain+"Well - that stuff is real.  And that's what we are working on.  It is not something you will achieve overnight\n"
mental_training_explain=mental_training_explain+"I think to get really good at just this one technique you should practice it diligently for a solid month!'n"
mental_training_explain=mental_training_explain+"It is not easy!  But by making it a game I hope to make it easiER.  \n\nThink of it like getting your black\n"
mental_training_explain=mental_training_explain+"belt in your martial arts.  But instead of breaking bricks you will be blowing minds.  Good luck!\n\n"

number_peg_explain="Here are the pegs for the digits 0-9:\n\n0='S' or'Z' sound\n1='T' or 'D' sound (remember it only has one stick in the letter)\n"
number_peg_explain=number_peg_explain+"2 = the 'N' sound (it has two sticks in the letter)\n3 = the 'M' sound (the letter has 3 sticks)\n"
number_peg_explain=number_peg_explain+"4 = the 'R' sound (looks kinda like an R if you stretch the imagination\n5 = the 'L' sound (like the Roman "
number_peg_explain=number_peg_explain+"letter L = 50).\n6 = the 'sh' or 'ch' sound (kind looks like a cross between a s and a g - but not the hard g\n"
number_peg_explain=number_peg_explain+"sound - it's like cherry or sheep)\n7 = the 'G' or 'K' sound (looks kinda like K if you flip it around and squint\n"
number_peg_explain=number_peg_explain+"8 = the 'F' sound (looks like a cursive F)\nand 9 = the 'P' or 'b' sound (looks like those letters if you juggle\n"
number_peg_explain=number_peg_explain+"it.\n  Now that you know that you can make words from them.  Like 10 is a one and zero or a T and an S sound.  \n"
number_peg_explain=number_peg_explain+"a T and an S can spell Toes.  So 10 = 'toes'.  75 is the K and the L sound so it can be the word 'Coal'.  See\n"
number_peg_explain=number_peg_explain+"what I mean?n\n\This first game will help you pick the word out that represents the 2-digit number.  You will \n"
number_peg_explain=number_peg_explain+"be able to work out what they are but more importantly to really be able to do this you have to MEMORIZE them.\n"
number_peg_explain=number_peg_explain+"Yes - all 100 of them!  That's what the game is for - to go from working them out to picturing each one to \n"
number_peg_explain=number_peg_explain+"REMEMBERING them.  Once you can remember all the two digit numbers and they come to your mind quickly then you\n"
number_peg_explain=number_peg_explain+"are set up to be AMAZING!  An 8-digit number becomes just four pictures that you can put together in a silly and\n"
number_peg_explain=number_peg_explain+"easily memorable way.  Trust me - we will get to that later on.  Just have fun seeing how much better you can\n"
number_peg_explain=number_peg_explain+"get each day and then after a month it will become second nature.\n\n HAVE FUN!!!"

start_of_game_text = [intro_text,mental_training_explain,number_peg_explain]

len_text=len(start_of_game_text)

for ii in range(3):
    print(start_of_game_text[ii])
    if ii <2:
        input("\npress enter to continue\n\n\n")
    else:
        input("\n\n\nPress enter to Begin Your Game\n\n\n")




##########################################################################################################################
#START OF GAME
##########################################################################################################################       

#Multiple choice GAME BEGINS - make into a function later

while len(used_numbers)<101 and player_guess != "z":
    print("\n")
    present_number=unique_number() #call function to creat a unique number for this quiz q
    present_peg=peg[present_number] #this is the word for this quiz number
    gen_10_rnd_words(present_number) #this GENERATES the 10 multiple choice question list
    print_10_rnd_words(rnd_word_list) #this PRINTS the multiple choice question list
    print("")
    print("press <z> at any time to end game")
    player_guess = input("Which of these is a peg word for {}?\n".format(present_number))
    if player_guess == choice[rnd_position]:
        print("CORRECT!!  WELL DONE!!!\n\n")
        score+=1
    else:
        print("Incorrect.  The correct peg for {} is {}".format(present_number,present_peg),"\n\n")
    attempts+=1

print("Game Over - You scored {} out of {} tries.  Great job - keep at it!".format(score,attempts),"\n\n")



#For testing only
#print("\n\n") #\n prints a new line and \t prints a tab character
#print("memory number is {} and peg word is {}".format(present_number,present_peg))    





#if we have done all 100 print you have done all 100 and your score is ___


#print in two columns with numbers from 1-10 left of them

#get player input whth quiz_number = _____ peg word

#if correct print WELL DONE! and add one to score

#if incorrect print WRONG! The correct answer is _____

#ask if again y/n

 


