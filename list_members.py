#!/usr/bin/python

# Get Twitter list's members and write them to a txt file

from twython import Twython
import time
from twython import exceptions
import pickle


keys_file='keys'
with open(keys_file) as f:
    APP_KEY = f.readline().strip("\n")
    APP_SECRET = f.readline().strip("\n")
    OAUTH_TOKEN = f.readline().strip("\n")
    OAUTH_TOKEN_SECRET = f.readline().strip("\n")

def get_members_list(list,owner):
    next_cursor=-1
    c=[]
    while(next_cursor):
        print 'Nombre de la lista :',list
        try:
            print 'connecting'
            print 'Creador :'+owner
            search = t.get_list_members(slug=list, owner_screen_name= owner, cursor=next_cursor)
            c=c+search['users']
            print 'Miembros: ',len(c)
            next_cursor = search["next_cursor"]
            if next_cursor:
                print 'Waiting for 60s'
                time.sleep(60)
        except exceptions.TwythonRateLimitError as e:
            print e
            print 'Waiting for 60s'
            time.sleep(60)
        except exceptions.TwythonError as e:
            print e
            print 'Waiting for 60s'
            time.sleep(60)
    return c

t = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

# Introducir nombre de la lista y usuario propietario
name = 'old_drys'
owner = 'democraciareal'
miembros = get_members_list(name,owner)

# Output: lista_miembros, list con nombres de usuario
lista_miembros = []
for item in miembros:
    lista_miembros += [str(item['screen_name'])]

# Guardar output en archivo txt
with open('round2/%s_members.txt' % (name),'wb') as f:
    pickle.dump(lista_miembros,f)
