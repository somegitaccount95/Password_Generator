from urllib.request import urlopen
import random
import string

running = True

random_chars = r"0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
response = urlopen(word_site)
txt = response.read()
words = txt.splitlines()

insec_pass_site = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt"
response = urlopen(insec_pass_site)
txt = response.read()
insec_passes = txt.splitlines()

      
def make_pass(security):

    # level 1
    gen = random.sample(insec_passes, 1)
    password_1 = (b''.join(gen)).decode('utf-8')
    
    # level 2

    int_1 = random.randint(0, 9999)
    int_2 = random.randint(0, 9999)
    
    word_1 = words[int_1].decode('utf-8')
    word_2 = words[int_2].decode('utf-8')

    password_2 = word_1 + word_2 + str(int_1)
    password_2.replace("a", "@")

    
    # level 3
    
    choosen_chars = random.sample(random_chars, 16)
    password_3 = ''.join(choosen_chars)


    if security == "1":
        return password_1
    elif security == "2":
        return password_2
    elif security == "3":
        return password_3
    elif security == "all":
        return f" 1: {password_1}\n 2: {password_2}\n 3: {password_3}"
    else:
        print("        Invalid security level!")
        return "null"
    
    


def init_text():
    print(
        '''
        ------------------------------------------------------------------
        Welcome to the password generator!                                
        There are 3 security levels:                                      
        1 - meh | 2 - secure | 3 - super secure | all - for all 3
        Type "new" for new password.                                      
        Type "exit" to quit                                               
        ------------------------------------------------------------------
        '''
        )


init_text()


while running:
    user_input = input("        :>")
    if user_input == "new":
        
        security = input("        Security level:")
        num = input("        How many passwords do you want?:")

        for i in range(int(num)):
            new_pass = make_pass(security)
            print('        ' + new_pass)
        
    if user_input == "exit":
        quit()
        
        
    
