from zoodb import *
from debug import *
from pbkdf2 import PBKDF2 
import hashlib
import random

def newtoken(db, cred):
    hashinput = "%s%.10f" % (cred.password, random.random()) #exercise 5   
    cred.token = hashlib.md5(hashinput).hexdigest()
    db.commit()
    return cred.token

def login(username, password):               #exercise 5
    db = cred_setup()
    cred = db.query(Cred).get(username)
    if not cred:
        return None
    #if cred.password == password:
    if cred.password == PBKDF2(password, cred.salt).hexread(32):   #exercise 6
        return newtoken(db, cred)
    else:
        return None

def register(username, password):             #exercise 5
    db = person_setup()
    cred_db = cred_setup()  

    person = db.query(Person).get(username)
    if person:
        return None

    #Create Person
    newperson = Person()
    newperson.username = username

    #Creat Cred
    newcred = Cred()
    newcred.username = username

    #exercise 6
    salt = os.urandom(8).encode('base-64')
    newcred.salt = salt 
    password = PBKDF2(password, newcred.salt).hexread(32)
    newcred.password = password

    #Add
    db.add(newperson)
    cred_db.add(newcred)

    #Commit
    db.commit()
    cred_db.commit()
    return newtoken(cred_db, newcred)

def check_token(username, token):        #exercise 5
    db = cred_setup()
    cred = db.query(Cred).get(username)
    if cred and cred.token == token:
        return True
    else:
        return False

