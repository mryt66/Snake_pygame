import pygame
import random
pygame.init()
okno=pygame.display.set_mode((500,500))
pygame.display.set_caption('snake')
okno.fill('black')
speed=10
grub=10
a=250
b=250
#potrzebne rzeczy nie ingerować
czas=pygame.time.Clock()
kordy=[]
l1=[]
startw=0
starts=0
starta=0
startd=0
zero=0
zmiennax=0
zmiennay=0
dłweza=1
blokadax=0
blokaday=0
def kordychlopa(a,b):
    kordy.append([a,b])
def update():
    pygame.display.update()
def rng(n,m):
    return random.randint(n,m)
def prostokatcurrently(a,b):
    return pygame.draw.rect(okno,'white',(a,b,10,10))
def printablica(x,y):
    return pygame.draw.rect(okno,'red',(x,y,10,10))
#
# pierwsza czerwona
x = rng(8, 492)
y = rng(8, 492)
printablica(x,y)
#
l1.append([x,y])
kordychlopa(a,b)
prostokatcurrently(a,b)
koniec=1
while koniec==1:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            koniec=0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and blokaday==0:
                zmiennax = 0
                zmiennay=-speed
            elif event.key==pygame.K_a and blokadax==0:
                zmiennax=-speed
                zmiennay=0
            elif event.key==pygame.K_d and blokadax==0:
                zmiennax=speed
                zmiennay=0
            elif event.key==pygame.K_s and blokaday==0:
                zmiennax = 0
                zmiennay=speed
    a+=zmiennax/2
    b+=zmiennay/2
    if zmiennax!=0:
        blokadax=1
        blokaday=0
    elif zmiennay!=0:
        blokadax=0
        blokaday=1
    if a>=495 or a<=-1 or b>=495 or b<=-1:
        koniec=0
        okno.fill('black')
        print("koniec")
    if l1[0][0]<=a+((grub/3)*2+2) and l1[0][0]>=a-((grub/3)*2+2) and l1[0][1]<=b+((grub/3)*2+2) and l1[0][1]>b-((grub/3)*2+2):
        l1=[]
        x=rng(8,492)
        y=rng(8,492)
        l1.append([x,y])
        dłweza+=1
    okno.fill('black')
    printablica(x,y)
    dłkord = len(kordy)
    kordychlopa(a, b)
    for i in range(dłweza):
        prostokatcurrently(kordy[dłkord-i-1][0],kordy[dłkord-i-1][1])
        if a == kordy[dłkord - i - 1][0] and b == kordy[dłkord - i - 1][1] and (zmiennay!=0 or zmiennax!=0):
            koniec=0
            print("koniec")
    update()
    czas.tick(30)






