# -------------------
#
#   Date : 2023-12-25
#   Auteur : Lodjo28
#   Nom du fichier : Encryption
#   Version : 0.1
#
# -------------------

from tkinter import *

root = Tk()
root.config(bg="#939393")
root.title("Conversions RSA")
root.minsize(800, 512)
root.geometry("1920x1080")
root.iconbitmap("logo.ico")


center_frame = Frame(root, bg="#939393")
center_below_frame = Frame(root, bg="#939393")

Label_champ1 = Label(center_frame, text="Message :", bg="#939393", fg="white", font=("Courrier", 25))
Label_champ2 = Label(center_frame, text="Clé Publique :", bg="#939393", fg="white", font=("Courrier", 25))
Label_champ3 = Label(center_frame, text="Valeur de n :", bg="#939393", fg="white", font=("Courrier", 25))

message = StringVar()
champ = Entry(center_frame, textvariable=message, fg="white", bg="#939393", font=("Courrier", 25))
champ.focus()

PublicKey = StringVar()
champ2 = Entry(center_frame, textvariable=PublicKey, fg="white", bg="#939393", font=("Courrier", 25))

Nvalue = StringVar()
champ3 = Entry(center_frame, textvariable=Nvalue, fg="white", bg="#939393", font=("Courrier", 25))

value = StringVar()
reponseLab = Label(center_frame, textvariable=value, bg="#939393", fg="white", font=("Courrier", 15))

indicLabelReponse = Label(center_frame, text="Message encodé :", bg="#939393", fg="white", font=("Courrier", 25))

Label_champ1.grid(row=0, column=0)
champ.grid(row=0, column=1)

Label_champ2.grid(row=1, column=0)
champ2.grid(row=1, column=1)

Label_champ3.grid(row=2, column=0)
champ3.grid(row=2, column=1)

indicLabelReponse.grid(row=3, column=0)
reponseLab.grid(row=3, column=1)

Bouton = Button(center_below_frame, text="Décrypter", fg="white", bg="#006EB1", font=("Courrier", 25), command=lambda: encode(message.get(), PublicKey.get(), Nvalue.get()))
Bouton.pack()

def encode(message, PublicKey, Nvalue):

    PublicKey, Nvalue = int(PublicKey), int(Nvalue)

    message_encoded = [ord(c) for c in message]
    ciphertext = [pow(c, PublicKey, Nvalue) for c in message_encoded]

    value.set(ciphertext)
    print(ciphertext)


center_frame.pack(expand=YES)
center_below_frame.pack()

root.mainloop()