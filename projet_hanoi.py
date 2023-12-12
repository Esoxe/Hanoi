import copy
import time
import pickle
import datetime

#Variable globales 
suivant=False #Variable qui active le coup suivant
nb_coup=0
scoreopen=False #Ouverture ou non de la fenetre score
autosolution=False #Solution automatique utiliser ou non
tempsopen=False #Ouverture ou non de la fenetre classement temps
reflexionopen=False #Ouverture ou non de la fenetre reflexion moyenne


#Partie A : plateau de jeu et Listes

def init(n) :
    plateau=[[],[],[]]
    i=n
    while i>0 :
        plateau[0].append(i)
        i-=1
    return plateau






def nbDisques(plateau,numtour):
    return len(plateau[numtour])




def disqueSup(plateau,numtour):
    if len(plateau[numtour])!=0 :
        return plateau[numtour][len(plateau[numtour])-1]
    else :
        return -1




def posdisque(plateau,numdisque):
    i=0
    while i<len(plateau) :
        j=0
        while j <len(plateau[i]) :
            if plateau[i][j] == numdisque :
                return i
            j+=1
        i+=1




def verifDepl(plateau,nt1,nt2) :
    if disqueSup(plateau,nt1) == -1 :
        return False
    elif disqueSup(plateau,nt2)==-1 or disqueSup(plateau,nt1)<disqueSup(plateau,nt2):
        return True
    else :
        return False
       




def verifVictoire(plateau,n) :
    for i in range(len(plateau)-1) :
        if len(plateau[i]) !=0 :
            return False
    for i in range(len(plateau[-1])-1) :
        if plateau[-1][i]<plateau[-1][i+1] :
            return False
    return True




# 3 PARTIE B : graphisme avec turtle
import turtle as tl
# 1)








def laBase_reset(n):
    tl.fillcolor('yellow')
    tl.begin_fill()
    tl.up()
    tl.goto(-300,-100)
    tl.down()
    tl.forward((40+30*(n))*3+(4*20))
    tl.left(90)
    tl.forward(20)
    tl.left(90)
    tl.forward((40+30*(n))*3+(4*20))
    tl.left(90)
    tl.forward(20)
    tl.end_fill()
    tl.right(180)
    tl.forward(20)
    tl.right(90)








def poteaux_reset(n):
    tl.fillcolor('yellow')
    tl.begin_fill()
    for i in range(1):
        tl.forward(((40+30*(n))/2)+20-3)
        tl.left(90)
        tl.forward(n*20+40)
        tl.right(90)
        tl.forward(6)
        tl.right(90)
        tl.forward(n*20+40)
        tl.left(90)
    for i in range(2):
        tl.forward(((40+30*(n)))+20-6)
        tl.left(90)
        tl.forward(n*20+40)
        tl.right(90)
        tl.forward(6)
        tl.right(90)
        tl.forward(n*20+40)
        tl.left(90)
    tl.end_fill()




def laBase(n):
    tl.fillcolor('brown')
    tl.begin_fill()
    tl.up()
    tl.goto(-300,-100)
    tl.down()
    tl.forward((40+30*(n))*3+(4*20))
    tl.left(90)
    tl.forward(20)
    tl.left(90)
    tl.forward((40+30*(n))*3+(4*20))
    tl.left(90)
    tl.forward(20)
    tl.end_fill()
    tl.right(180)
    tl.forward(20)
    tl.right(90)




def poteaux(n):
    tl.fillcolor('brown')
    tl.begin_fill()
    for i in range(1):
        tl.forward(((40+30*(n))/2)+20-3)
        tl.left(90)
        tl.forward(n*20+40)
        tl.right(90)
        tl.forward(6)
        tl.right(90)
        tl.forward(n*20+40)
        tl.left(90)
    for i in range(2):
        tl.forward(((40+30*(n)))+20-6)
        tl.left(90)
        tl.forward(n*20+40)
        tl.right(90)
        tl.forward(6)
        tl.right(90)
        tl.forward(n*20+40)
        tl.left(90)
    tl.end_fill()






def dessinePlateau(n):
    tl.bgcolor("yellow")
    tl.up()
    tl.goto(-250,180)
    tl.write('Les tours de Hanoï', font=('arial black', 40))
    tl.goto(-460,370)
    tl.write('CAILLE Daniel, PERRET Florian ', font=('arial', 15))
    tl.down()
    tl.speed(1000000)
    tl.shapesize(0.1)
    laBase(n)
    poteaux(n)
    tl.up()
    tl.goto(-4000,-300)






# dessinePlateau(3)


# 2)




def place(nd,plateau):
    i=0
    tr=0
   
    while i<len(plateau) and tr==0:
        if nd in plateau[i]:
            tr=1
        i+=1
   
    i=i-1
    y=0
    somme=0
    while y<len(plateau[i]):
        if plateau[i][y]>nd:
            somme+=1
        y+=1


    return somme,i+1
   


def dessineDisque(nd,plateau,n):




    tl.speed(1000000)
    x,b=place(nd,plateau)
    tl.up()
    tl.goto(-300,-80)
    tl.backward((40+30*n)/2)
    tl.forward((40+(30*n)+20)*b)
    tl.backward((40+(30*(nd-1)))/2)
    tl.left(90)
    tl.forward(20*x)
    tl.right(90)
    tl.down()
    tl.fillcolor('blue')
    tl.begin_fill()
    for i in range (2):
        tl.forward(40+(30*(nd-1)))
        tl.left(90)
        tl.forward(20)
        tl.left(90)
    tl.end_fill()






# 3)
def effaceDisque(nd, plateau, n):


    tl.color('yellow')
    tl.speed(1000000)
    x,b=place(nd,plateau)
    tl.up()
    tl.goto(-300,-80)
    tl.backward((40+30*n)/2)
    tl.forward((40+(30*n)+20)*b)
    tl.backward((40+(30*(nd-1)))/2)
    tl.left(90)
    tl.forward(20*x)
    tl.right(90)
    tl.down()
    tl.fillcolor('yellow')
    tl.begin_fill()
    for i in range (2):
        tl.forward(40+(30*(nd-1)))
        tl.left(90)
        tl.forward(20)
        tl.left(90)
    tl.end_fill()
    tl.color('black')






# 4)




def dessineConfig(plateau, n):
    dessinePlateau(n)
    nd=n
    while nd>=1:                     # on dessine les disque dans l'ordre décroissant (pour donner un effet réel)
        dessineDisque(nd,plateau,n)
        nd-=1






# 5)
def effaceTout(plateau, n):
    nd=1
    while nd<=n:
        effaceDisque(nd,plateau,n)   # on efface les disque dans l'ordre croissant (pour donner un effet réel)
        nd+=1
   
    dessinePlateau(n)




#Partie C : interactions avec le joueur




#1)
def lireCoords(plateau):
    n_tour_depart=int(tl.numinput("départ ?","Entre 1 et 3"))
    test=False
    while not(test)  :
        if n_tour_depart ==-1:
            sur=tl.textinput("tu souhaite abandonner ?","(oui/non)")
            if sur== "oui" :
                return -1,None
            else :
                n_tour_depart=int(tl.numinput("départ ?","Entre 1 et 3"))
        elif 0<n_tour_depart<4 :
            if len(plateau[n_tour_depart-1])!=0:
                for i in range(len(plateau)):
                    if i!=n_tour_depart-1 :
                       if verifDepl(plateau,n_tour_depart-1,i) :
                           test=True
                if test==False :
                    print("Aucun deplacement possible a partir de cette tour choissier en une autre")          
                    n_tour_depart=int(tl.numinput("départ ?","Entre 1 et 3"))                               
            else :
                print("La tour numéro ",n_tour_depart,"est vide choissiser en une autre. ")
                n_tour_depart=int(tl.numinput("départ ?","Entre 1 et 3"))
        else :
            n_tour_depart=int(tl.numinput("départ ?","Entre 1 et 3"))
        if test==True :
            test2=False
            n_tour_arrivee=int(tl.numinput("arrivee ? :","entre 1 et 3"))
            while not(test2)  :
                if 0<n_tour_arrivee<4 :
                    test2=verifDepl(plateau,n_tour_depart-1,n_tour_arrivee-1)
                    if test2==False :
                        print("Deplacement impossible disque plus petit déja present sur cette tour")
                        test2==True
                        n_tour_depart=int(tl.numinput("départ ?","Entre 1 et 3"))
                        n_tour_arrivee=int(tl.numinput("arrivee ? :","entre 1 et 3"))
                else :
                 n_tour_arrivee=int(tl.numinput("arrivee ? :","entre 1 et 3"))
    return n_tour_depart,n_tour_arrivee






def jouerUnCoup(plateau,n):
    tour_depart,tour_arrivee=lireCoords(plateau)
    if tour_depart==-1 :
        return -1
    effaceDisque(plateau[tour_depart-1][-1],plateau,n)
    plateau[tour_arrivee-1].append(plateau[tour_depart-1][-1])
    del plateau[tour_depart-1][-1]
    dessineDisque(plateau[tour_arrivee-1][-1],plateau,n)
    tl.speed(1000000)
    dessineConfig(plateau,n)
    return 0








def boucleJeu(n) :
    max=10
    global nb_coup
    while not(verifVictoire(plateau,n)) and nb_coup<=max :
        tl.color("black")
        tl.write((""), font=('arial black', 10))
        global suivant
        test=suivant
        if test :
            nb_coup+=1
            i=jouerUnCoup(plateau,n)
            coups[nb_coup]=copy.deepcopy(plateau)
            efface_text(290,-230)
            tl.up()
            tl.goto(300,-250)
            tl.down()
            tl.write(("Nombre de coup "), font=('arial black', 10))
            tl.up()
            tl.goto(500,-250)
            tl.down()
            tl.write((nb_coup), font=('arial black', 10))
            suivant=False
        if nb_coup==-1 :
            return nb_coup,"abandonne",plateau
    if not(verifVictoire(plateau,n)) :
        return nb_coup,"defaite",plateau
    else :
        return nb_coup,"Victoire",plateau
   
   
   


# Partie D : annulation de coups




def dernierCoup(coups) :
    tour_depart=coups[0][0]
    tour_arrivee=coups[1][1]
    dernier_plateau=coups[len(coups)-1]
    av_dernier_plateau=coups[len(coups)-2]
    for i in range(len(dernier_plateau)) :
        if len(dernier_plateau[i])>len(av_dernier_plateau[i]):
            tour_arrivee=i
        elif len(dernier_plateau[i])<len(av_dernier_plateau[i]):
            tour_depart=i
    return tour_depart,tour_arrivee








def annulerDernierCoup(coups,plateau):
    tour_depart,tour_arrivee=dernierCoup(coups)
    effaceDisque(coups[len(coups)-1][tour_arrivee][-1],coups[len(coups)-1],n)
    del coups[len(coups)-1]
    dessineDisque(coups[len(coups)-1][tour_depart][-1],coups[len(coups)-1],n)
    dessineConfig(coups[len(coups)-1],n)
    tl.up()
    return copy.deepcopy(coups[len(coups)-1])
    




#Partie E : comparaison des scores et temps de jeu




def sauvScore(nom,n,nb_coup,date,timer) :
    score[len(score)+1]=[nom,n,nb_coup,date,timer]








def affichage_ordre_croissant(score_copy) :
    space=50
    for i in range(len(score_copy)) :
            min=list(score_copy.keys())[0]
            for partie in score_copy :
                if score_copy[partie][2]<score_copy[min][2]:
                    min=partie
            tl.goto(-250,-180-space)
            tl.write(score_copy[min][0]+"                  "+str(score_copy[min][1])+'                          ' +str(score_copy[min][2])+'               '+str(score_copy[min][3]), font=('arial black', 12))    
            del score_copy[min]
            space+=50    
 
def afficheScore(score,n=0):
    if len(score)!=0 :
        score_copy=copy.deepcopy(score)
        meilleur_score_3={}
        space=50
        tl.up()
        tl.goto(-250,-180)
        tl.write('NOM        NOMBRE DE DISQUE    NOMBRE DE COUP          DATE', font=('arial black', 10))
        if n==0:
            if len(score)>3 :
                for i in range(0,3) :
                    min=list(score_copy.keys())[0]
                    for partie in score_copy:
                        if score_copy[partie][2]<score_copy[min][2] :
                            min=partie
                    meilleur_score_3[i]=score_copy[min]
                    del score_copy[min]
                affichage_ordre_croissant(meilleur_score_3)
            else :
                affichage_ordre_croissant(score_copy)    
        else :
            for i in range(1,len(score)+1) :
                if score_copy[i][1]!=n:
                    del score_copy[i]
            affichage_ordre_croissant(score_copy)
        tl.down()

def affichage_ordre_croissant_Temps(score_copy):
    space=50
    for i in range(len(score_copy)) :
            min=list(score_copy.keys())[0]
            for partie in score_copy :
                if score_copy[partie][2]<score_copy[min][2]:
                    min=partie
            tl.goto(-250,-180-space)
            tl.write(score_copy[min][0]+"                "+str(score_copy[min][1])+'                 ' +str(score_copy[min][4])+'             '+str(score_copy[min][3]), font=('arial black', 12))    
            del score_copy[min]
            space+=50  


def afficheChronos(score,n=0):
    if len(score)!=0 :
        score_copy=copy.deepcopy(score)
        meilleur_score_3={}
        space=50
        tl.up()
        tl.goto(-250,-180)
        tl.write('NOM        NOMBRE DE DISQUE    TEMPS(s)                DATE', font=('arial black', 10))
        if n==0:
            if len(score)>3 :
                for i in range(0,3) :
                    min=list(score_copy.keys())[0]
                    for partie in score_copy:
                        if score_copy[partie][4]<score_copy[min][4] :
                            min=partie
                    meilleur_score_3[i]=score_copy[min]
                    del score_copy[min]
                affichage_ordre_croissant_Temps(meilleur_score_3)
            else :
                affichage_ordre_croissant_Temps(score_copy)    
        else :
            for i in range(1,len(score)+1) :
                if score_copy[i][1]!=n:
                    del score_copy[i]
            affichage_ordre_croissant_Temps(score_copy)
        tl.down()

def reflexionMoy():
    liste_noms=[]
    temps_moyen={}
    somme_coups=0
    somme_temps=0
    
    if len(score)!=0 :
        for partie in score :
            if not(score[partie][0] in liste_noms) :
                liste_noms.append(score[partie][0])
        for nom in liste_noms :
            somme_coups=0
            somme_temps=0
            for partie in score :
                if score[partie][0]==nom :
                    somme_coups+=score[partie][2]
                    somme_temps+=score[partie][4]
            temps_moyen[nom]=somme_temps/somme_coups
        affichage_joueurs_vitesse(temps_moyen)

def affichage_joueurs_vitesse(temps_moyen) : #Affichage clasement temps de jeu par coups
    tl.up()
    tl.goto(-250,-180)
    tl.write('NOM        TEMPS REFLEXION PAR COUP', font=('arial black', 10))
    temps_moyen_copy=dict(temps_moyen)
    space=50
    i=0
    while i<3 and i<len(temps_moyen) :
            min=list(temps_moyen_copy.keys())[0]
            for nom in temps_moyen_copy :
                if temps_moyen[nom]<temps_moyen[min] :
                    min=nom
            tl.goto(-250,-180-space)
            tl.write(min+"                "+str(temps_moyen_copy[min]), font=('arial black', 12))    
            del temps_moyen_copy[min]
            space+=50  
            i+=1


def efface_text(x,y): #Efface un texte a la position x,y
    tl.up()
    tl.goto(x,y)
    tl.down()
    tl.color("yellow")
    tl.fillcolor("yellow")
    tl.begin_fill()
    for i in range(4):
        tl.forward(500)
        tl.right(90)
    tl.end_fill()
    tl.color("black")
    tl.up()
    tl.goto(-1000,-160)
    tl.down()

def button(number,buttontxt,font=15,x=-550) : #Permet l'affichage d'un bouton avec comme parametre hauteur,snom,taille,position
    tl.up()
    tl.goto(x,200-number*60)
    tl.down()
    for i in range(2):
        tl.fillcolor('purple')
        tl.begin_fill()
        tl.forward(200)
        tl.left(90)
        tl.forward(50)
        tl.left(90)
        tl.end_fill()
    tl.up()
    tl.goto(x+10,210-number*60)
    tl.write(buttontxt,font=('arial black',font))

def interface(): #Affichage de l'emsemble des boutons de l'interface
    button(0,"ABANDONNER")
    button(1,"ANNULER DERNIER COUP",10)
    button(2,"SCORE")
    button(0,"COUP SUIVANT",x=350)
    button(3,"SOLUTION")
    button(4,"CLASSEMENT TEMPS",11)
    button(5,"REFLEXION MOYENNE",11)

def efface_score(): #Efface l'afficage du score
    tl.up()
    tl.goto(-250,-350)
    tl.down()
    tl.color("yellow")
    tl.fillcolor("yellow")
    tl.begin_fill()
    for i in range (2):
        tl.forward(500)
        tl.left(90)
        tl.forward(200)
        tl.left(90)
    tl.end_fill()

def buttonClick(x,y): #liée a l'evenement onscreenClick elle permet de gerer les cliques de l'utilisateur sur les différents boutons de l'interface
    global n
    global nb_coup
    global plateau
    global rejouer
    global autosolution
    global tempsopen
    global reflexionopen
    if rejouer=="oui" : 
        if -550<x<-250 and 200<y<250 : #Bouton Abandon
            nb_coup=-1
        if -550<x<-250 and 140<y<190 : #Bouton annulerDernierCoup
            plateau=annulerDernierCoup(coups,plateau)
            nb_coup-=1
            efface_text(290,-230)
            tl.up()
            tl.goto(300,-250)
            tl.down()
            tl.write(("Nombre de coup "), font=('arial black', 10))
            tl.up()
            tl.goto(500,-250)
            tl.down()
            tl.write((nb_coup), font=('arial black', 10))
            tl.up()
        if -550<x<-250 and 80<y<130 : #Bouton Score
            global scoreopen
            if scoreopen :
                efface_score()
                scoreopen = False
            else :
                efface_score()
                tl.color("black")
                afficheScore(score)
                tl.up()
                scoreopen = True
                tempsopen=False
                reflexionopen=False
        if -550<x<-250 and 20<y<70 : #Bouton solution
            if nb_coup == 0 :
                autosolution=True
                resolutionauto(plateau,n)
        if 350<x<550 and 200<y<250 :  #Bouton Coup suivant
            global suivant
            suivant=True
        if -550<x<-250 and -40<y<10 : #Bouton classement temps
            if tempsopen :
                efface_score()
                tempsopen=False
            else:
                efface_score()
                tl.color("black")
                afficheChronos(score)
                tl.up()
                tempsopen=True
                scoreopen=False
                reflexionopen=False
        if -550<x<-250 and -100<y<-50 : #Bouton reflexion moyenne
            if reflexionopen :
                efface_score()
                reflexionopen=False
            else:
                efface_score()
                tl.color("black")
                reflexionMoy()
                tl.up()
                reflexionopen=True
                scoreopen=False
                tempsopen=False

#Partie F

def hanoi(n, source, target, auxiliary, moves=[]):
    if n > 0:
        # Déplacer n-1 disques de la source vers le poteau auxiliaire
        hanoi(n-1, source, auxiliary, target, moves)
        
        # Déplacer le n-ème disque de la source vers la cible
        moves.append((source, target))
        
        # Déplacer les n-1 disques du poteau auxiliaire vers la cible
        hanoi(n-1, auxiliary, target, source, moves)

    return moves


def resolutionauto(plateau,n) : #Animation de la solution automatique par la fonction hanoi, dans turtle
    mouvements=hanoi(n,1,3,2)
    for depart,arrivee in mouvements :
        effaceDisque(plateau[depart-1][-1],plateau,n)
        plateau[arrivee-1].append(plateau[depart-1][-1])
        del plateau[depart-1][-1]
        dessineDisque(plateau[arrivee-1][-1],plateau,n)
        tl.speed(1000000)
        dessineConfig(plateau,n)
    tl.up()



#Programme principal
tl.setup(1920,1080)
rejouer="oui"
with open('score.txt','rb') as f1 : #Recuperation des scores déja enregistré
    score=pickle.load(f1)
while rejouer=="oui":  # cette boucle while permet de recommencer une partie
    nb_coup=0
    score_copy=copy.deepcopy(score)
    coups={}
    n=int(tl.numinput("nombre de disque ?","nombre >0 "))
    while n<=0 :
        n=int(tl.numinput("nombre de disque ?","nombre > 0 "))
    timer1=time.time()
    
    plateau=init(n)
    tl.onscreenclick(buttonClick,1) #Gestion des cliques
    tl.listen()
    tl.speed(1000000)
    coups[0]=copy.deepcopy(plateau)
    dessineConfig(plateau,n)
    interface()
    coup,etat,p=boucleJeu(n)



    if etat=="Victoire"  and not(autosolution):
        temps=round(time.time()-timer1,1)
        efface_text(-250,-160)
        nom=tl.textinput("Quelle est votre nom ?","nom")
        if autosolution==False :
            sauvScore(nom,n,coup,datetime.date.today(),temps)
            afficheScore(score)


    plateau=p             # on utilise p (le plateau return) qui est dans le fonction boucleJeu 
    time.sleep(2)
    effaceTout(plateau, n)  # effacer l'ensemble des disques et le plateau pour pouvoir recommencer une partie
    tl.color("yellow")
    laBase_reset(n)
    poteaux_reset(n)
    efface_text(290,-230)
    tl.color("black")
    tl.up()
    tl.goto(-10000,-80)
    tl.down()
    efface_text(-250,-160)
    tl.up()
    tl.goto(-150,0)
    tl.down()
    tl.write('Veux tu rejouer ?', font=('arial black', 25))
    interface()
    rejouer=tl.textinput("Veux tu rejouer ?","(oui/non)")
    efface_text(-160,50)


dessineConfig([[1,2,3,4,5]], 5)
tl.color("black")
tl.up()
tl.goto(-150,130)
tl.write("Partie Terminer",font=("arial black",25))
afficheScore(score)
with open('score.txt',"wb") as f1: #Enregistre les valeurs des nouvelles parties dans le fichier
    pickle.dump(score,f1)
tl.done()