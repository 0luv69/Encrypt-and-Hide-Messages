import random
import os
import string
def encrept(word):    
    number = len(word) 
    
    if number <=3:    
        reverse = word[number::-1]   
        return reverse   
    else:
        letter =list(word)
        saver = letter[0]
        letter.pop(0)   
        update_letter = "".join(letter)
        random_words = "".join((random.choice(string.ascii_letters) for x in range(3))) 
        update_letter2 = f"{random_words}{update_letter}{saver}{random_words[0:2]}"
        return update_letter2    

def decrept(word):
    number = len(word)
    if number <=3:    
        reverse = word[number::-1]   
        return reverse   
    else:
        letter = list(word)
        sou = number-2
        up_letter= letter[3:sou]
        newnum = (len(up_letter))-1
        saver = up_letter[newnum]
        up_letter.pop(newnum)
        up_letter ="".join(up_letter)
        return (f"{saver}{up_letter}")
        
print("Welcome to this platform")
need = int(input("What do you want to do if Unhide then press \"1\" and for Hide press \"0\"\t"))
decoded_words = []
coded_words = []
CurrentLocation=(os.path.dirname(__file__)).replace("\\","/")

if need == 1:
    Sentence = input("Enter your sentence to Unhide \t")
    each_word=Sentence.split()
    for i in range (len(each_word)):
        coded = decrept(each_word[i])
        coded_words.append(coded) 
    coded_sentece = " ".join(coded_words)
    print(f"\nThe unhidden sentence is:    {coded_sentece} \n\n\t\tof this sentence     \"{Sentence}\" ")
    f = open(f"{CurrentLocation}/hidden_msg.txt","a").write(f"\n{coded_sentece}\t|\t{Sentence}") 
    
elif need == 0:
    Sentence = input("Enter your sentence to Hide \t")
    each_word=Sentence.split()
    for i in range (len(each_word)):
        Decoded = encrept(each_word[i])
        decoded_words.append(Decoded) 
    decoded_sentece = " ".join(decoded_words)    
    print(f"\nThe Hidden sentence is:   {decoded_sentece} \n\n\t\tfor this   \"{Sentence}\"")
    f = open(f"{CurrentLocation}/hidden_msg.txt","a").write(f"\n{Sentence}\t|\t{decoded_sentece}") 

else:
    print("Sorry you have entered wrong input")


input('press Enter to End:\t')