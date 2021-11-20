import socket
import threading
from tkinter import *
from tkinter import scrolledtext
# Connecting To Server
user = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
user.connect(('127.0.0.1', 5010))

def recevoir():
    while True:
        try:
            
            message = user.recv(1024).decode('ascii')
            if message == 'ps':
                user.send(userup.cget("text").encode('ascii'))
            else:
                listmessage.insert(END,message)
        except:
            
            user.close()
            break

def ecrire():
    message = '{}: {}'.format(userup.cget("text"), entry.get())
    user.send(message.encode('ascii'))
    entry.delete(0,END)


def getpseudo():    
    username=entry.get() 
    if(username!=''):
        
        userup.config(text=username)
        btn.config(text='Envoyer',command=ecrire)
        label.config(text='Saisir votre Message :')
        entry.config(width=50)
        entry.delete(0,END)
        receive_thread = threading.Thread(target=recevoir)
        receive_thread.start()


fenetre=Tk()
fenetre.title("CHAT")
fenetre.geometry('1000x700')
fenetre.resizable(False,False)
fenetre.iconbitmap('C:/Users/Sos/Desktop/image_projet/chat.ico')
title=Label(fenetre,text='LaZa CHAT',fg='#008B8B',bg='#6495ED')
title.config(font=('times',20,'bold'))
title.pack(fill=X)

userup=Label(fenetre,text=' ',fg='#008B8B',bg='#6495ED')
userup.config(font=('times',20,'bold'))
userup.place(x=10,y=0)

userframe=Frame(fenetre)
userframe.pack(pady=10)

vide=Label(userframe,text='',fg='#008B8B',bg='#6495ED',width=1000,height=8)
vide.pack()


label=Label(userframe,text='Saisir votre pseudo :',fg='#008B8B',bg='#6495ED')
label.config(font=('times',14,'bold'))
label.place(x=20,y=40)

entry= Entry(userframe,width=30,fg='#008B8B',bg='white')
entry.config(font=('times',14,'bold'))
entry.place(x=250,y=40) 


btn=Button(userframe,text='Confirmer',command=getpseudo ,bg='#008B8B',fg='#6495ED')
btn.config(font=('times',14,'bold'))
btn.place(x=800,y=35)

messageframe=Frame(fenetre)
messageframe.pack()

scroll=Scrollbar(messageframe,orient=VERTICAL)
listmessage=Listbox(messageframe,width=1000,height=30,bg='#F0FFFF',yscrollcommand=scroll.set)

scroll.config(command=listmessage.yview)
scroll.pack(side=RIGHT,fill=Y)

listmessage.pack()


#listmessage=scrolledtext.ScrolledText( fenetre,width=1000,height=30,bg='gray')
#listmessage.place(x=0,y=180)

fenetre.mainloop()
