import urllib.request#needed to reference the wordlist
import sys
#program loops until stopped by the user

while True:
    wordlist = urllib.request.urlopen("https://raw.githubusercontent.com/AFrasc/7letter-words-en/main/7letter-words-en.txt")
    if not wordlist:
        sys.exit("~~Word list empty")#check if the list loaded correctly
    
    letters = input("Enter '7' letters: ").upper()
    if len(letters) != 7:
        sys.exit("~~Entry must be seven letters~~")#checks for 7 letters
        
    word_count = 0 #number returned
        
    with wordlist: 
        for line in wordlist:#accounts for each word
            temp_letters = list(letters) #allows us to check-off letters without losing them
            lttr_cnt = 0 #checks if all letters are present
            prev_cnt = 0 #checks if a letter is not present
            fline = line.strip().decode()#cleans up the word from file for comparison
            for character in fline:
                for letter in temp_letters:
                    prev_cnt = lttr_cnt
                    if character == letter:
                        lttr_cnt += 1
                        temp_letters.remove(letter)#don't want to compare same letter twice
                        break
                if prev_cnt == lttr_cnt:#letter not present, moves on to next word
                    break
                if lttr_cnt == len(fline):#all letters accounted for, print word
                        print('\n', fline)
                        word_count += 1
        
    print(f"Possible Iterations of Letter Input: {word_count}")   
    print("~~Task Done~~")
    choice = input("Run again? (y/n): ")
    if choice.lower() == 'n':
        break
    elif choice.lower() == 'y':
        continue
sys.exit()
