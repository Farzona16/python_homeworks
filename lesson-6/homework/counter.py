import os
from collections import Counter
my_file='sample.txt'
new_file='word_count_report.txt'
if not os.path.exists(my_file):
    open(my_file, 'w').close()
def add_text():
    with open(my_file,'a') as f:
        new_text=input("enter your text here: ")
        f.write(new_text+'\n')
def count_words():
    with open(my_file, 'r') as f:
        text = f.read()
        n=int(input("Enter the number of most common words: "))
        a=str(n)
        words=text.lower().split()
        cleaned_words=[word.strip('.,!?') for word in words]
        word_count = str(len(cleaned_words)) 
        word_counts=Counter(cleaned_words)
        most_common=word_counts.most_common(n)
    with open(new_file,'w') as n:
        print(f"Total words: {word_count}")
        print(f"The {a} most common words: ")
        for word, count in most_common:
           print(f"{word}-{count} time(s)")
        n.write(f"\n Total words: {word_count}")
        n.write(f"\n The {a} most common words: ")
        for word, count in most_common:
            n.write(f"\n {word}-{count}")
def text_available():
    with open(my_file,'r') as f:
        text=f.read()
        you_want=input(f"This is the text from sample.txt file: {text}"
                '''\n1.count words
2.add additional text
3.exit program
enter your choice: ''')
    if you_want=='1':
        count_words()
    elif you_want=='2':
        add_text()
    elif you_want=='3':
        print("Exiting program")
        exit()
    else:
        print("you entered incorrect number. please try again ")
def main():
    while True:
        with open(my_file,'r') as f:
            text=f.read()
            if not text.strip():
                my_choice=input('''there is not text. 
                you must add by the press "1" button
                or you can exit the program by pressing the "2"
                what is your choice: ''')
                if my_choice=='1':
                    add_text()
                elif my_choice=='2':
                    print("Exiting program")
                    break
                else:
                    print("you entered incorrect number. please try again ")
            else:
                text_available()



if __name__=="__main__":
    main()