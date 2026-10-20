from datetime import datetime ;
import random
import secrets
import string

def get_current_time():
    return datetime.now()

def gen_dice_values(start, end):
    dice1 =random.randint(start, end) # (int)( random() * (end - start) + start ) #generate a random number between start and end
    dice2 =  random.randint(start, end) # (int)( random() * (end - start) + start ) #generate a random number between start and end
    return dice1, dice2

def gen_password(string_length=12):
    alphabet =string.ascii_letters+string.digits+string.punctuation
    password = ""
    for _ in range(string_length):
        password += secrets.choice(alphabet)
    return password

def read_file(path):
    try :
        with open(path,'r') as file:
            content = file.read()
            return content
    except:
        return "Not found" # "file not found please check the filepath is correct."