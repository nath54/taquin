#coding:utf-8
import random,pygame,numpy
from pygame.locals import *

def melangeometre(taquin):
    m=0
    nb=[]
    for x in range(taquin.shape[0]):
        for y in range(taquin.shape[1]):
            if taquin[x,y]!=0: nb.append(taquin[x,y])
    odt=[]
    for n in nb:
        for nn in nb:
            if n!=nn and not [n,nn].sort() in odt:
                odt.append([n,nn].sort())
                if n>nn and nb.index(n)<nb.index(nn): m+=1
    return m


def verif_gagne(taquin):
    cond=True
    nbs=[]
    for x in range(taquin.shape[0]):
        for y in range(taquin.shape[1]):
            nbs.append(taquin[x,y])
    for n in nbs:
        if n!=0 and n!=nbs.index(n)+1:
            cond=False
    return cond

def get_pos0(taquin):
    pos0=None
    for x in range(taquin.shape[0]):
        for y in range(taquin.shape[1]):
            if taquin[x,y]==0:
                pos0=[x,y]
                break
    return pos0

def move_taquin(taquin,dep):
    pos0=get_pos0(taquin)
    if dep=="up":
        if pos0!=None:
            if pos0[1]!=taquin.shape[1]-1:
                taquin[pos0[0],pos0[1]]=taquin[pos0[0],pos0[1]+1]
                taquin[pos0[0],pos0[1]+1]=0
        else: print("error")
    elif dep=="down":
        if pos0!=None:
            if pos0[1]!=0:
                taquin[pos0[0],pos0[1]]=taquin[pos0[0],pos0[1]-1]
                taquin[pos0[0],pos0[1]-1]=0
        else: print("error")
    elif dep=="left":
        if pos0!=None:
            if pos0[0]!=taquin.shape[0]-1:
                taquin[pos0[0],pos0[1]]=taquin[pos0[0]+1,pos0[1]]
                taquin[pos0[0]+1,pos0[1]]=0
        else: print("error")
    elif dep=="right":
        if pos0!=None:
            if pos0[0]!=0:
                taquin[pos0[0],pos0[1]]=taquin[pos0[0]-1,pos0[1]]
                taquin[pos0[0]-1,pos0[1]]=0
        else: print("error")
    return taquin
    
def gen_taquin(tx,ty):
    taquin=numpy.zeros([tx,ty],dtype=int)
    nbs=[1]
    while len(nbs)<tx*ty-1: nbs.append(nbs[len(nbs)-1]+1)
    nbs.append(0)
    n=0
    for x in range(taquin.shape[0]):
        for y in range(taquin.shape[1]):
            taquin[x,y]=nbs[n]
            n+=1
    for w in range(random.randint(1,2)):
        taquin=move_taquin(taquin,random.choice(["up","down","left","right"]))
    return taquin



def aff_pygame(taquin,tex,tey,fenetre,font):
    fenetre.fill((0,0,0))
    tcx=tex/taquin.shape[0]
    tcy=tey/taquin.shape[1]
    xx,yy=0,0
    nbs=[]
    for x in range(taquin.shape[0]):
        for y in range(taquin.shape[1]):
            nbs.append(taquin[x,y])
    for nb in nbs:
            if nb!=0:
                cl=(150,150,150)
                if nb==nbs.index(nb)+1:
                    cl=(0,150,0)
                pygame.draw.rect(fenetre,cl,(xx,yy,tcx,tcy),0)
                pygame.draw.rect(fenetre,(20,20,20),(xx,yy,tcx,tcy),2)
                fenetre.blit(font.render(str(nb),25,(255,255,255)),[xx+tcx/4,yy+tcy/4])
            xx+=tcx
            if xx>=tex: xx,yy=0,yy+tcy
    pygame.display.update()

def main_pygame():
    tex,tey=400,500
    pygame.init()
    fenetre=pygame.display.set_mode([tex,tey])
    pygame.display.set_caption("TAQUIN")
    tx,ty=10,10
    font=pygame.font.SysFont("Serif",int((tey/ty)/2))
    taquin=gen_taquin(tx,ty)
    print(taquin)
    encour=True
    needtoaff=True
    dc=None
    mt=melangeometre(taquin)
    while encour:
        for event in pygame.event.get():
            if event.type==QUIT: exit()
            elif event.type==KEYDOWN:
                if event.key==K_q: encour=False
                elif event.key==K_UP: taquin=move_taquin(taquin,"left")
                elif event.key==K_DOWN: taquin=move_taquin(taquin,"right")
                elif event.key==K_LEFT: taquin=move_taquin(taquin,"up")
                elif event.key==K_RIGHT: taquin=move_taquin(taquin,"down")
                needtoaff=True
            elif event.type==MOUSEBUTTONDOWN:
                dc=pygame.mouse.get_pos()
            elif event.type==MOUSEBUTTONUP:
                if dc!=None:
                    pos=pygame.mouse.get_pos()
                    dx=pos[0]-dc[0]
                    dy=pos[1]-dc[1]
                    if dx>0 and abs(dx)>abs(dy): taquin=move_taquin(taquin,"down")
                    if dx<0 and abs(dx)>abs(dy): taquin=move_taquin(taquin,"up") 
                    if dy>0 and abs(dy)>abs(dx): taquin=move_taquin(taquin,"right") 
                    if dy<0 and abs(dy)>abs(dx): taquin=move_taquin(taquin,"left")  
                    dc=None
                    needtoaff=True
        if needtoaff:
            mt=melangeometre(taquin)
            aff_pygame(taquin,tex,tey,fenetre,font)
            needtoaff=False
        if verif_gagne(taquin):
            encour=False
            print("Vous avez gagné")

def aff_texte(taquin):
    pass

def main_texte():
    tx,ty=2,2
    taquin=gen_taquin(tx,ty)
    gagne=False
    while not gagne:
        mt=melangeometre(taquin)
        aff_texte(taquin)
        if verif_gagne(taquin): gagne=True
    if gagne: print("Vous avez gagné!")


main_pygame()


















