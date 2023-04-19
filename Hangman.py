import random
def execute(n):
    if n==0:
        print("------------")
        print("             |")
        print("             |")
        print("             |")
        print("             |")
        print("             |")
        print("             |")
        print("             |")
        print("             |")
        print("             |")
        print("             |")
        print("             |")
        print("             |")
    elif n==1:
        print("------------")
        print("     |       |")
        print("     |       |")
        print("     |       |")
        print("             |")
        print("             |")
        print("             |")
        print("             |")
        print("             |")
        print("             |")
        print("             |")
        print("             |")
        print("             |")
    elif n==2:
        print("------------")
        print("     |       |")
        print("     |       |")
        print("     |       |")
        print("   _______   |")
        print("  ( @  @)  |")
        print("   LLLLI   |")
        print("             |")
        print("             |")
        print("             |")
        print("             |")
        print("             |")
        print("             |")
        print("             |")
        print("             |")
    elif n==3:
        print("------------")
        print("     |       |")
        print("     |       |")
        print("     |       |")
        print("   _______   |")
        print("  ( @  @)  |")
        print("   LLLLI   |")
        print("     |       |")
        print("    |||      |")
        print("     |       |")
        print("     |       |")
        print("             |")
        print("             |")
        print("             |")
        print("             |")
    elif n==4:
        print("------------")
        print("     |       |")
        print("     |       |")
        print("     |       |")
        print("   _______   |")
        print("  ( @  @)  |")
        print("   LLLLI   |")
        print("o    |    o  |")
        print(" \__|||__/   |")
        print("     |       |")
        print("     |       |")
        print("             |")
        print("             |")
        print("             |")
        print("             |")
    elif n==5:
        print("------------")
        print("     |       |")
        print("     |       |")
        print("     |       |")
        print("   _______   |")
        print("  ( @  @)  |")
        print("   LLLLI   |")
        print("o    |    o  |")
        print(" \__|||__/   |")
        print("     |       |")
        print("     |       |")
        print("    _^_     |")
        print("  /     \   |")
        print(" 0       0 |")
        print("             |")
    else:
        exit()
print("Hello! Welcome to this interesting Hangman Game coded by Parishkrat.")
print("Enter 0 to exit or any other number to continue.")
choice1=int(input())
if choice1!=0:
    print("\nRULES:\nI am sure you must be familiar with the rules of the game. Try to guess my word alphabet by alphabet, if you can.")
    print("You will get several chances to guess my 5-letter word. If you guess a letter correct, the corresponding character of default word '@#$%&'\nwill be replaced by your letter at its correct position.\nBut if you guess it wrong..... a total of 6 times..... Hangman shall be dead!!!")
    print("You are assured that your word will not be something very unusual, for your word will surely be one of the 350 most used 5-letter words!(I know only 350 five-letter words :< )")
    strofall=open("words.py")
    stringofall=strofall.read()
    listofall=stringofall.split()
    print("You will get 2 hints, you will have to type any number for hint during any chance of guessing. I suggest you to use the hints in the beginning of the game to avoid getting the same letter you have already entered before as hint.")
    print("Ready?")
    mych=listofall[random.randrange(0,336)]
    print("Ok, so, umm, let me choose my word...... Okie! I have chosen it. Type 0 to end the game or any other number to continue.")
    choice2=int(input())
    mystr="@#$%&"
    copymych=mych
    cwrong=0
    i=0
    hint=0
    count=0
    used=""
    if choice2!=0:
        while cwrong!=6:
            i=i+1
            print()
            print("Your Chance No.", i, "-->\nEnter a letter of your choice in lowercase or a number for hint")
            ch=input()
            used=used+ch+","
            if len(ch)==1:
                ispresent=mych.find(ch)
                if ispresent==-1 and ord(ch)>=97:
                    print("Sorry, your alphabet is not present in my word, or you have guessed the same letter twice ;)")
                    print("Save him if you dare to!! Huihuihui")
                    print("Used characters:",used)
                    execute(cwrong)
                    cwrong = cwrong + 1
                    if cwrong==6:
                        break
                elif ord(ch)>=48 and ord(ch)<=57:
                    if hint<2:
                        hint=hint+1
                        print("Ok, so you are already needing a hint? Here it is:\nHINT number ",hint)
                        rand2=random.randrange(1,5)
                        print("My word has the letter '",copymych[rand2],"' in it.")
                    else:
                        print("Don't try to act oversmart with me, I know you have used your hint :>")
                else:
                    c=mych.count(ch)
                    count=count+1
                    index=0
                    print("Your alphabet is present in my letter", c, "time/s")
                    for j in range(0,c):#enter e
                        pres=mych.find(ch,index)#e,0=0, e,1=3
                        index=pres+1#1, 4
                        mystr=mystr.replace(mystr[pres],ch)#e@#%&, e@#e$
                        mych=mych.replace(mych[pres]," ")#" "nter, " "nt" "r
                    print("Your word now becomes", mystr)#
                    if mystr==copymych:
                        print("I'm impressed, you guessed my word in",i,"tries with only",(i-5),"wrong guesses!\nHangman saved. I'll catch hold of you next time. Till then bye-bye. UwU")
                        exit()
            else:
                print("Told you to enter 1 letter at a time, Play the game all over again if you want to display at least some resistance.")
                exit()
        print("\nGAME OVER\nYou guessed the letter wrong 6 times. My word was",copymych,". You were able to guess",count,"letters of my word in",(count+cwrong),"tries.\nHangman's dead, so shall you be someday. Come again if you wanna lose. UwU")
    else:
        exit()
else:
    exit()