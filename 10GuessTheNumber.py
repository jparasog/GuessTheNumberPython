import random
pc=random.randint(0,100)
guess=150
i=0
while guess !=pc:
    i=i+1
    guess=int(input("guess"))
    if guess>pc:
        print("Κατέβα")
    elif guess<pc:
        print("Ανέβα")
    else:
        print("Σωστά")
        print("Tο βρήκες σε", i,"προσπάθειες")
        if i<5:
            print("Μπράβο")
        elif i<=10:
            print("Μπορούσες καλύτερα")
        else:
            print("Καλύτερη τύχη την επόμενη φορά")