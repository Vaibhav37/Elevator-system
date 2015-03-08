import pygame,sys,time
pygame.init()


width=1000
height=700
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Elevator model")
screen.fill((200,200,200))
class canvas():
    def __init__(self):                     # drawing lines and writing floor number.
        
        pygame.draw.line(screen,(0,0,0),(10,0),(10,700),2)
        pygame.draw.line(screen,(0,0,0),(70,0),(70,700),2)
        pygame.draw.line(screen,(0,0,0),(110,0),(110,700),2)
        pygame.draw.line(screen,(0,0,0),(170,0),(170,700),2)
        pygame.draw.line(screen,(0,0,0),(210,0),(210,700),2)
        pygame.draw.line(screen,(0,0,0),(270,0),(270,700),2)
        pygame.draw.line(screen,(0,0,0),(310,0),(310,700),2)
        pygame.draw.line(screen,(0,0,0),(370,0),(370,700),2)
        
        i=0
        y=70
        while i<10:
            j=0
            x=10
            i+=1
            while j<4:
                pygame.draw.line(screen,(0,0,0),(x,y),(x+60,y),2)
                j+=1
                x+=100
            font  = pygame.font.Font(None , 30)
            s= str(11-i)
            text = font.render(s,1,(250,0,0))
            screen.blit(text, (x-35,y-50))
            y+=70
        

        pygame.draw.rect(screen,(255,255,255),(579,279,180,150))
        pygame.draw.rect(screen,(255,255,255),(779,279,180,150))
        pygame.draw.rect(screen,(255,255,255),(579,479,180,150))
        pygame.draw.rect(screen,(255,255,255),(779,479,180,150))

        font  = pygame.font.Font(None , 30)
        s= str(1)
        text = font.render(s,1,(0,0,0))
        screen.blit(text, (660,460))

        font  = pygame.font.Font(None , 30)
        s= str(2)
        text = font.render(s,1,(0,0,0))
        screen.blit(text, (860,460))

        font  = pygame.font.Font(None , 30)
        s= str(3)
        text = font.render(s,1,(0,0,0))
        screen.blit(text, (660,260))

        font  = pygame.font.Font(None , 30)
        s= str(4)
        text = font.render(s,1,(0,0,0))
        screen.blit(text, (860,260))

        pygame.draw.rect(screen,(0,0,0),(600,500,40,20),1)
        pygame.draw.rect(screen,(0,0,0),(650,500,40,20),1)
        pygame.draw.rect(screen,(0,0,0),(700,500,40,20),1)
        pygame.draw.rect(screen,(0,0,0),(600,530,40,20),1)
        pygame.draw.rect(screen,(0,0,0),(650,530,40,20),1)
        pygame.draw.rect(screen,(0,0,0),(700,530,40,20),1)
        pygame.draw.rect(screen,(0,0,0),(600,560,40,20),1)
        pygame.draw.rect(screen,(0,0,0),(650,560,40,20),1)
        pygame.draw.rect(screen,(0,0,0),(700,560,40,20),1)
        pygame.draw.rect(screen,(0,0,0),(650,590,40,20),1)

        font  = pygame.font.Font(None , 30)
        s= str(1)
        text = font.render(s,1,(250,0,0))
        screen.blit(text, (610,501))

        font  = pygame.font.Font(None , 30)
        s= str(2)
        text = font.render(s,1,(250,0,0))
        screen.blit(text, (660,501))

        font  = pygame.font.Font(None , 30)
        s= str(3)
        text = font.render(s,1,(250,0,0))
        screen.blit(text, (710,501))

        font  = pygame.font.Font(None , 30)
        s= str(4)
        text = font.render(s,1,(250,0,0))
        screen.blit(text, (610,531))

        font  = pygame.font.Font(None , 30)
        s= str(5)
        text = font.render(s,1,(250,0,0))
        screen.blit(text, (660,531))

        font  = pygame.font.Font(None , 30)
        s= str(6)
        text = font.render(s,1,(250,0,0))
        screen.blit(text, (710,531))

        font  = pygame.font.Font(None , 30)
        s= str(7)
        text = font.render(s,1,(250,0,0))
        screen.blit(text, (610,561))

        font  = pygame.font.Font(None , 30)
        s= str(8)
        text = font.render(s,1,(250,0,0))
        screen.blit(text, (660,561))

        font  = pygame.font.Font(None , 30)
        s= str(9)
        text = font.render(s,1,(250,0,0))
        screen.blit(text, (710,561))

        font  = pygame.font.Font(None , 30)
        s= str(0)
        text = font.render(s,1,(250,0,0))
        screen.blit(text, (660,591))


        pygame.draw.rect(screen,(0,0,0),(800,500,40,20),1)
        pygame.draw.rect(screen,(0,0,0),(850,500,40,20),1)
        pygame.draw.rect(screen,(0,0,0),(900,500,40,20),1)
        pygame.draw.rect(screen,(0,0,0),(800,530,40,20),1)
        pygame.draw.rect(screen,(0,0,0),(850,530,40,20),1)
        pygame.draw.rect(screen,(0,0,0),(900,530,40,20),1)
        pygame.draw.rect(screen,(0,0,0),(800,560,40,20),1)
        pygame.draw.rect(screen,(0,0,0),(850,560,40,20),1)
        pygame.draw.rect(screen,(0,0,0),(900,560,40,20),1)
        pygame.draw.rect(screen,(0,0,0),(850,590,40,20),1)

        font  = pygame.font.Font(None , 30)
        s= str(1)
        text = font.render(s,1,(250,0,0))
        screen.blit(text, (810,501))

        font  = pygame.font.Font(None , 30)
        s= str(2)
        text = font.render(s,1,(250,0,0))
        screen.blit(text, (860,501))

        font  = pygame.font.Font(None , 30)
        s= str(3)
        text = font.render(s,1,(250,0,0))
        screen.blit(text, (910,501))

        font  = pygame.font.Font(None , 30)
        s= str(4)
        text = font.render(s,1,(250,0,0))
        screen.blit(text, (810,531))

        font  = pygame.font.Font(None , 30)
        s= str(5)
        text = font.render(s,1,(250,0,0))
        screen.blit(text, (860,531))

        font  = pygame.font.Font(None , 30)
        s= str(6)
        text = font.render(s,1,(250,0,0))
        screen.blit(text, (910,531))

        font  = pygame.font.Font(None , 30)
        s= str(7)
        text = font.render(s,1,(250,0,0))
        screen.blit(text, (810,561))

        font  = pygame.font.Font(None , 30)
        s= str(8)
        text = font.render(s,1,(250,0,0))
        screen.blit(text, (860,561))

        font  = pygame.font.Font(None , 30)
        s= str(9)
        text = font.render(s,1,(250,0,0))
        screen.blit(text, (910,561))

        font  = pygame.font.Font(None , 30)
        s= str(0)
        text = font.render(s,1,(250,0,0))
        screen.blit(text, (860,591))


        pygame.draw.rect(screen,(0,0,0),(600,300,40,20),1)
        pygame.draw.rect(screen,(0,0,0),(650,300,40,20),1)
        pygame.draw.rect(screen,(0,0,0),(700,300,40,20),1)
        pygame.draw.rect(screen,(0,0,0),(600,330,40,20),1)
        pygame.draw.rect(screen,(0,0,0),(650,330,40,20),1)
        pygame.draw.rect(screen,(0,0,0),(700,330,40,20),1)
        pygame.draw.rect(screen,(0,0,0),(600,360,40,20),1)
        pygame.draw.rect(screen,(0,0,0),(650,360,40,20),1)
        pygame.draw.rect(screen,(0,0,0),(700,360,40,20),1)
        pygame.draw.rect(screen,(0,0,0),(650,390,40,20),1)

        font  = pygame.font.Font(None , 30)
        s= str(1)
        text = font.render(s,1,(250,0,0))
        screen.blit(text, (610,301))

        font  = pygame.font.Font(None , 30)
        s= str(2)
        text = font.render(s,1,(250,0,0))
        screen.blit(text, (660,301))

        font  = pygame.font.Font(None , 30)
        s= str(3)
        text = font.render(s,1,(250,0,0))
        screen.blit(text, (710,301))

        font  = pygame.font.Font(None , 30)
        s= str(4)
        text = font.render(s,1,(250,0,0))
        screen.blit(text, (610,331))

        font  = pygame.font.Font(None , 30)
        s= str(5)
        text = font.render(s,1,(250,0,0))
        screen.blit(text, (660,331))

        font  = pygame.font.Font(None , 30)
        s= str(6)
        text = font.render(s,1,(250,0,0))
        screen.blit(text, (710,331))

        font  = pygame.font.Font(None , 30)
        s= str(7)
        text = font.render(s,1,(250,0,0))
        screen.blit(text, (610,361))

        font  = pygame.font.Font(None , 30)
        s= str(8)
        text = font.render(s,1,(250,0,0))
        screen.blit(text, (660,361))

        font  = pygame.font.Font(None , 30)
        s= str(9)
        text = font.render(s,1,(250,0,0))
        screen.blit(text, (710,361))

        font  = pygame.font.Font(None , 30)
        s= str(0)
        text = font.render(s,1,(250,0,0))
        screen.blit(text, (660,391))


        pygame.draw.rect(screen,(0,0,0),(800,300,40,20),1)
        pygame.draw.rect(screen,(0,0,0),(850,300,40,20),1)
        pygame.draw.rect(screen,(0,0,0),(900,300,40,20),1)
        pygame.draw.rect(screen,(0,0,0),(800,330,40,20),1)
        pygame.draw.rect(screen,(0,0,0),(850,330,40,20),1)
        pygame.draw.rect(screen,(0,0,0),(900,330,40,20),1)
        pygame.draw.rect(screen,(0,0,0),(800,360,40,20),1)
        pygame.draw.rect(screen,(0,0,0),(850,360,40,20),1)
        pygame.draw.rect(screen,(0,0,0),(900,360,40,20),1)
        pygame.draw.rect(screen,(0,0,0),(850,390,40,20),1)

        font  = pygame.font.Font(None , 30)
        s= str(1)
        text = font.render(s,1,(250,0,0))
        screen.blit(text, (810,301))

        font  = pygame.font.Font(None , 30)
        s= str(2)
        text = font.render(s,1,(250,0,0))
        screen.blit(text, (860,301))

        font  = pygame.font.Font(None , 30)
        s= str(3)
        text = font.render(s,1,(250,0,0))
        screen.blit(text, (910,301))

        font  = pygame.font.Font(None , 30)
        s= str(4)
        text = font.render(s,1,(250,0,0))
        screen.blit(text, (810,331))

        font  = pygame.font.Font(None , 30)
        s= str(5)
        text = font.render(s,1,(250,0,0))
        screen.blit(text, (860,331))

        font  = pygame.font.Font(None , 30)
        s= str(6)
        text = font.render(s,1,(250,0,0))
        screen.blit(text, (910,331))

        font  = pygame.font.Font(None , 30)
        s= str(7)
        text = font.render(s,1,(250,0,0))
        screen.blit(text, (810,361))

        font  = pygame.font.Font(None , 30)
        s= str(8)
        text = font.render(s,1,(250,0,0))
        screen.blit(text, (860,361))

        font  = pygame.font.Font(None , 30)
        s= str(9)
        text = font.render(s,1,(250,0,0))
        screen.blit(text, (910,361))

        font  = pygame.font.Font(None , 30)
        s= str(0)
        text = font.render(s,1,(250,0,0))
        screen.blit(text, (860,391))


        pygame.draw.rect(screen,(0,0,0),(580,280,180,150),1)
        pygame.draw.rect(screen,(0,0,0),(780,280,180,150),1)
        pygame.draw.rect(screen,(0,0,0),(580,480,180,150),1)
        pygame.draw.rect(screen,(0,0,0),(780,480,180,150),1)




        



class button():
    def __init__(self,n):
        self.n=n
        i=0
        y=20
        x=410
        up=pygame.image.load('up.jpg')
        down=pygame.image.load('down.jpg')
        while(i<self.n):
            screen.blit(up,(x,y))
            pygame.draw.rect(screen,(250,0,0),(x,y,32,32),2)
            screen.blit(down,(x+35,y))
            pygame.draw.rect(screen,(250,0,0),(x+35,y,32,32),2)
            i+=1
            y+=70
    def pressed(self,my):# y co-ordinates given to it, then it will return at which floor button is presed is pressed.
        if my>=20 and my<=51:
            return (10)
        elif my>=90 and my<=121:
            return (9)
        elif my>=160 and my<=191:
            return (8)
        elif my>=230 and my<=261:
            return (7)
        elif my>=300 and my<=331:
            return (6)
        elif my>=370 and my<=401:
            return (5)
        elif my>=440 and my<=471:
            return (4)
        elif my>=510 and my<=541:
            return (3)
        elif my>=580 and my<=611:
            return (2)
        elif my>=650 and my<=681:
            return (1)
        
    def pressed2(self,mx,my):
        if mx>=600 and mx<=640 and my>=500 and my<=520:
            return (1)
        elif mx>=650 and mx<=690 and my>=500 and my<=520:
            return (2)
        elif mx>=700 and mx<=740 and my>=500 and my<=520:
            return (3)
        elif mx>=600 and mx<=640 and my>=530 and my<=550:
            return(4)
        elif mx>=650 and mx<=690 and my>=530 and my<=550:
            return (5)
        elif mx>=700 and mx<=740 and my>=530 and my<=550:
            return(6)
        elif mx>=600 and mx<=640 and my>=560 and my<=580:
            return(7)
        elif mx>=650 and mx<=690 and my>=560 and my<=580:
            return (8)
        elif mx>=700 and mx<=740 and my>=560 and my<=580:
            return (9)
        elif mx>=650 and mx<=690 and my>=590 and my<=610:
            return (0)

    def pressed3(self,mx,my):
        if mx>=800 and mx<=840 and my>=500 and my<=520:
            return (1)
        elif mx>=850 and mx<=890 and my>=500 and my<=520:
            return (2)
        elif mx>=900 and mx<=940 and my>=500 and my<=520:
            return (3)
        elif mx>=800 and mx<=840 and my>=530 and my<=550:
            return(4)
        elif mx>=850 and mx<=890 and my>=530 and my<=550:
            return (5)
        elif mx>=900 and mx<=940 and my>=530 and my<=550:
            return(6)
        elif mx>=800 and mx<=840 and my>=560 and my<=580:
            return(7)
        elif mx>=850 and mx<=890 and my>=560 and my<=580:
            return (8)
        elif mx>=900 and mx<=940 and my>=560 and my<=580:
            return (9)
        elif mx>=850 and mx<=890 and my>=590 and my<=610:
            return (0)

    def pressed4(self,mx,my):
        if mx>=600 and mx<=640 and my>=300 and my<=320:
            return (1)
        elif mx>=650 and mx<=690 and my>=300 and my<=320:
            return (2)
        elif mx>=700 and mx<=740 and my>=300 and my<=320:
            return (3)
        elif mx>=600 and mx<=640 and my>=330 and my<=350:
            return(4)
        elif mx>=650 and mx<=690 and my>=330 and my<=350:
            return (5)
        elif mx>=700 and mx<=740 and my>=330 and my<=350:
            return(6)
        elif mx>=600 and mx<=640 and my>=360 and my<=380:
            return(7)
        elif mx>=650 and mx<=690 and my>=360 and my<=380:
            return (8)
        elif mx>=700 and mx<=740 and my>=360 and my<=380:
            return (9)
        elif mx>=650 and mx<=690 and my>=390 and my<=410:
            return (0)

    def pressed5(self,mx,my):
        if mx>=800 and mx<=840 and my>=300 and my<=320:
            return (1)
        elif mx>=850 and mx<=890 and my>=300 and my<=320:
            return (2)
        elif mx>=900 and mx<=940 and my>=300 and my<=320:
            return (3)
        elif mx>=800 and mx<=840 and my>=330 and my<=350:
            return(4)
        elif mx>=850 and mx<=890 and my>=330 and my<=350:
            return (5)
        elif mx>=900 and mx<=940 and my>=330 and my<=350:
            return(6)
        elif mx>=800 and mx<=840 and my>=360 and my<=380:
            return(7)
        elif mx>=850 and mx<=890 and my>=360 and my<=380:
            return (8)
        elif mx>=900 and mx<=940 and my>=360 and my<=380:
            return (9)
        elif mx>=850 and mx<=890 and my>=390 and my<=410:
            return (0)




  

class elevator():
    def __init__(self,no,by,x,y=632):              #no-> number of elevator (eg. 1,2,3,4,)
        self.y=y                                   #x->  x co-rdinate of elevator
        self.x=x                                   #y->  vertical position of elevator, initially at ground floor()
        self.no=no                                 #by->  vertical position of displaying board.used in ele_pos()
        self.by=by
    def show_elev(self,v_pos):
        self.v_pos=v_pos
        img=pygame.image.load('ele.jpg')
        imgx=self.x
        imgy=self.v_pos
        screen.blit(img,(imgx,imgy))
        font  = pygame.font.Font(None , 50)
        s= str(self.no)
        text = font.render(s,1,(250,250,250))
        screen.blit(text, ((self.x)+15,(self.v_pos)+20))
    
  
        
    
    def ele_pos(self,pos):# to display position of elevator
        self.pos=pos
        pygame.draw.rect(screen,(250,250,250),(530,self.by,140,30))
        pygame.draw.rect(screen,(0,0,0),(530-2,self.by-2,144,34),2)
        pygame.draw.line(screen,(0,0,0),(630,self.by),(630,self.by+30),2)

        font  = pygame.font.Font(None , 30)
        s= "Elevator "+str(self.no)
        text = font.render(s,1,(250,0,0))
        screen.blit(text, (530,self.by+5))

        if self.pos>=0 and self.pos<72:
            s1=str(10)
            t1=font.render(s1,1,(250,0,0))
            screen.blit(t1,(640,self.by+5))
        elif self.pos>=72 and self.pos<142:
            s1=str(9)
            t1=font.render(s1,1,(250,0,0))
            screen.blit(t1,(640,self.by+5))
        elif self.pos>=142 and self.pos<212:
            s1=str(8)
            t1=font.render(s1,1,(250,0,0))
            screen.blit(t1,(640,self.by+5))
        elif self.pos>=212 and self.pos<282:
            s1=str(7)
            t1=font.render(s1,1,(250,0,0))
            screen.blit(t1,(640,self.by+5))
        elif self.pos>=282 and self.pos<352:
            s1=str(6)
            t1=font.render(s1,1,(250,0,0))
            screen.blit(t1,(640,self.by+5))
        elif self.pos>=352 and self.pos<422:
            s1=str(5)
            t1=font.render(s1,1,(250,0,0))
            screen.blit(t1,(640,self.by+5))
        elif self.pos>=422 and self.pos<492:
            s1=str(4)
            t1=font.render(s1,1,(250,0,0))
            screen.blit(t1,(640,self.by+5))
        elif self.pos>=492 and self.pos<562:
            s1=str(3)
            t1=font.render(s1,1,(250,0,0))
            screen.blit(t1,(640,self.by+5))
        elif self.pos>=562 and self.pos<632:
            s1=str(2)
            t1=font.render(s1,1,(250,0,0))
            screen.blit(t1,(640,self.by+5))
        elif self.pos>=632 and self.pos<700:
            s1=str(1)
            t1=font.render(s1,1,(250,0,0))
            screen.blit(t1,(640,self.by+5))
def floor_top(p):
    if p==10:
        return 1
    elif p==9:
        return 74
    elif p==8: 
        return 142
    elif p==7:
        return 212
    elif p==6:
        return 283
    elif p==5:
        return 353
    elif p==4:
        return 422
    elif p==3:
        return 493
    elif p==2:
        return 562
    elif p==1: 
        return 632
            
        
            
        
                    
c=canvas()
but = button(10)
elv1=elevator(1,10,12)
elv2=elevator(2,70,112)
elv3=elevator(3,130,212)
elv4=elevator(4,190,312)
list_up=[0,0,0,0,0,0,0,0,0,0]
list_down=[0,0,0,0,0,0,0,0,0,0]
FPS = 50
pixmov =3
fpsTime = pygame.time.Clock()
i=0
curr1=0
curr2=0
imgy1=632
imgy2=632
imgy3=632
imgy4=632
imgy=632
st2 =-1
st3=-1
st4=-1
st5=-1
stop=0
t=-1
u=-1
dirtn=1
flag1=-1
flag2=-1
flag3=-1
flag4=-1
if curr1 == 0 and curr2==0:
        elv1.ele_pos(632)
        elv1.show_elev(632)
        elv2.ele_pos(632)
        elv2.show_elev(632)
        elv3.ele_pos(632)
        elv3.show_elev(632)
        elv4.ele_pos(632)
        elv4.show_elev(632)
while True:


    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
                mx,my=pygame.mouse.get_pos()
                st=but.pressed(my)
                st2=but.pressed2(mx,my)
                st3=but.pressed3(mx,my)
                st4=but.pressed4(mx,my)
                st5=but.pressed5(mx,my)
                
                if st>=1 and st<=10:
                    if mx>=410 and mx<=441:
                        list_up[st-1]=1
                        print st,"UP"
                        print list_up
                    
                    elif mx>=445 and mx<=477:
                        list_down[st-1]=1
                        print st,"Down"
                        print list_down
                    else:
                        print "CLICK PROPERLY!!!!!"
                    
    
    while i<10:
        if list_up[i]==1:
            curr1=i+1
            break
       
        i+=1
        
    i=9
    while i>=0:
        if list_down[i]==1:
            curr2=i+1
            break
       
        i-=1
        
    i=0

    
    
    if curr1>0:
        top1 = floor_top(curr1)
        
        screen.fill((200,200,200))
        c=canvas()
        but = button(10)



        a=(imgy1-top1)
        b=(imgy2-top1)
        c=(imgy3-top1)
        d=(imgy4-top1)
        e=[a,b,c,d]   
        first=min(filter(lambda x:x>=0,e))
        if first==(imgy1-top1) and (imgy1-top1)>=0:


            if imgy1 >=top1+3:
                imgy1 -=pixmov
                elv1.show_elev(imgy1)
                elv1.ele_pos(imgy1)
                elv2.show_elev(imgy2)
                elv2.ele_pos(imgy2)
                elv3.show_elev(imgy3)
                elv3.ele_pos(imgy3)
                elv4.show_elev(imgy4)
                elv4.ele_pos(imgy4)
                dirtn=1
            else:
            
                print 'haha'
                elv1.show_elev(imgy1)
                elv1.ele_pos(imgy1)
                elv2.show_elev(imgy2)
                elv2.ele_pos(imgy2)
                elv3.show_elev(imgy3)
                elv3.ele_pos(imgy3)
                elv4.show_elev(imgy4)
                elv4.ele_pos(imgy4)
                list_up[curr1-1]=0
                curr1=0
                flag1=1
                time.sleep(2)
                
                

        elif first==(imgy2-top1) and (imgy2-top1)>=0:
            if imgy2 >=top1+3:
                imgy2 -=pixmov
                elv1.show_elev(imgy1)
                elv1.ele_pos(imgy1)
                elv2.show_elev(imgy2)
                elv2.ele_pos(imgy2)
                elv3.show_elev(imgy3)
                elv3.ele_pos(imgy3)
                elv4.show_elev(imgy4)
                elv4.ele_pos(imgy4)
                dirtn=1
            else:
            
            
                elv1.show_elev(imgy1)
                elv1.ele_pos(imgy1)
                elv2.show_elev(imgy2)
                elv2.ele_pos(imgy2)
                elv3.show_elev(imgy3)
                elv3.ele_pos(imgy3)
                elv4.show_elev(imgy4)
                elv4.ele_pos(imgy4)
                list_up[curr1-1]=0
                curr1=0
                flag2=1
                time.sleep(2)
                
                

        elif first==(imgy3-top1) and (imgy3-top1)>=0:
            if imgy3 >=top1+3:
                imgy3 -=pixmov
                elv1.show_elev(imgy1)
                elv1.ele_pos(imgy1)
                elv2.show_elev(imgy2)
                elv2.ele_pos(imgy2)
                elv3.show_elev(imgy3)
                elv3.ele_pos(imgy3)
                elv4.show_elev(imgy4)
                elv4.ele_pos(imgy4)
                dirtn=1
            else:
            
            
                elv1.show_elev(imgy1)
                elv1.ele_pos(imgy1)
                elv2.show_elev(imgy2)
                elv2.ele_pos(imgy2)
                elv3.show_elev(imgy3)
                elv3.ele_pos(imgy3)
                elv4.show_elev(imgy4)
                elv4.ele_pos(imgy4)
                list_up[curr1-1]=0
                curr1=0
                flag3=1
                time.sleep(2)
                
                

        elif first==(imgy4-top1) and (imgy4-top1)>=0:
            if imgy4 >=top1+3:
                imgy4 -=pixmov
                elv1.show_elev(imgy1)
                elv1.ele_pos(imgy1)
                elv2.show_elev(imgy2)
                elv2.ele_pos(imgy2)
                elv3.show_elev(imgy3)
                elv3.ele_pos(imgy3)
                elv4.show_elev(imgy4)
                elv4.ele_pos(imgy4)
                dirtn=1
            else:
            
            
                elv1.show_elev(imgy1)
                elv1.ele_pos(imgy1)
                elv2.show_elev(imgy2)
                elv2.ele_pos(imgy2)
                elv3.show_elev(imgy3)
                elv3.ele_pos(imgy3)
                elv4.show_elev(imgy4)
                elv4.ele_pos(imgy4)
                list_up[curr1-1]=0
                curr1=0
                flag4=1 
                time.sleep(2)
      
    
    if st2>=0:
        top2 = floor_top(st2)
        if dirtn==1:
            screen.fill((200,200,200))
            c=canvas()
            but = button(10)
            if flag1==1:
                if imgy1>=top2+2:
                    imgy1 -=pixmov
                    elv1.show_elev(imgy1)
                    elv1.ele_pos(imgy1)
                    elv2.show_elev(imgy2)
                    elv2.ele_pos(imgy2)
                    elv3.show_elev(imgy3)
                    elv3.ele_pos(imgy3)
                    elv4.show_elev(imgy4)
                    elv4.ele_pos(imgy4)

                else:
            
                    elv1.show_elev(imgy1)
                    elv1.ele_pos(imgy1)
                    elv2.show_elev(imgy2)
                    elv2.ele_pos(imgy2)
                    elv3.show_elev(imgy3)
                    elv3.ele_pos(imgy3)
                    elv4.show_elev(imgy4)
                    elv4.ele_pos(imgy4)
                    st2=-1
                    flag1=0
                    time.sleep(2)

            elif flag2==1:
                if imgy2>=top2+2:
                    imgy2 -=pixmov
                    elv1.show_elev(imgy1)
                    elv1.ele_pos(imgy1)
                    elv2.show_elev(imgy2)
                    elv2.ele_pos(imgy2)
                    elv3.show_elev(imgy3)
                    elv3.ele_pos(imgy3)
                    elv4.show_elev(imgy4)
                    elv4.ele_pos(imgy4)

                else:
            
                    elv1.show_elev(imgy1)
                    elv1.ele_pos(imgy1)
                    elv2.show_elev(imgy2)
                    elv2.ele_pos(imgy2)
                    elv3.show_elev(imgy3)
                    elv3.ele_pos(imgy3)
                    elv4.show_elev(imgy4)
                    elv4.ele_pos(imgy4)
                    st2=-1
                    flag2=0
                    time.sleep(2)

            elif flag3==1:
                if imgy3>=top2+2:
                    imgy3 -=pixmov
                    elv1.show_elev(imgy1)
                    elv1.ele_pos(imgy1)
                    elv2.show_elev(imgy2)
                    elv2.ele_pos(imgy2)
                    elv3.show_elev(imgy3)
                    elv3.ele_pos(imgy3)
                    elv4.show_elev(imgy4)
                    elv4.ele_pos(imgy4)

                else:
            
                    elv1.show_elev(imgy1)
                    elv1.ele_pos(imgy1)
                    elv2.show_elev(imgy2)
                    elv2.ele_pos(imgy2)
                    elv3.show_elev(imgy3)
                    elv3.ele_pos(imgy3)
                    elv4.show_elev(imgy4)
                    elv4.ele_pos(imgy4)
                    st2=-1
                    flag3=0
                    time.sleep(2)

            elif flag4==1:
                if imgy4>=top2+2:
                    imgy4 -=pixmov
                    elv1.show_elev(imgy1)
                    elv1.ele_pos(imgy1)
                    elv2.show_elev(imgy2)
                    elv2.ele_pos(imgy2)
                    elv3.show_elev(imgy3)
                    elv3.ele_pos(imgy3)
                    elv4.show_elev(imgy4)
                    elv4.ele_pos(imgy4)

                else:
            
                    elv1.show_elev(imgy1)
                    elv1.ele_pos(imgy1)
                    elv2.show_elev(imgy2)
                    elv2.ele_pos(imgy2)
                    elv3.show_elev(imgy3)
                    elv3.ele_pos(imgy3)
                    elv4.show_elev(imgy4)
                    elv4.ele_pos(imgy4)
                    st2=-1
                    flag4=0
                    time.sleep(2)
            
        elif dirtn==-1:
            screen.fill((200,200,200))
            c=canvas()
            but = button(10)
            print 'vaibhav'
            if flag1==1:
                print 'singh'
                if imgy1<=top2+2:
                    print 'khokhar'
                    imgy1 +=pixmov
                    elv1.show_elev(imgy1)
                    elv1.ele_pos(imgy1)
                    elv2.show_elev(imgy2)
                    elv2.ele_pos(imgy2)
                    elv3.show_elev(imgy3)
                    elv3.ele_pos(imgy3)
                    elv4.show_elev(imgy4)
                    elv4.ele_pos(imgy4)

                else:
            
                    elv1.show_elev(imgy1)
                    elv1.ele_pos(imgy1)
                    elv2.show_elev(imgy2)
                    elv2.ele_pos(imgy2)
                    elv3.show_elev(imgy3)
                    elv3.ele_pos(imgy3)
                    elv4.show_elev(imgy4)
                    elv4.ele_pos(imgy4)
                    st2=-1
                    flag1=0
                    time.sleep(2)

            elif flag2==1:
                if imgy2<=top2+2:
                    imgy2 +=pixmov
                    elv1.show_elev(imgy1)
                    elv1.ele_pos(imgy1)
                    elv2.show_elev(imgy2)
                    elv2.ele_pos(imgy2)
                    elv3.show_elev(imgy3)
                    elv3.ele_pos(imgy3)
                    elv4.show_elev(imgy4)
                    elv4.ele_pos(imgy4)

                else:
            
                    elv1.show_elev(imgy1)
                    elv1.ele_pos(imgy1)
                    elv2.show_elev(imgy2)
                    elv2.ele_pos(imgy2)
                    elv3.show_elev(imgy3)
                    elv3.ele_pos(imgy3)
                    elv4.show_elev(imgy4)
                    elv4.ele_pos(imgy4)
                    st2=-1
                    flag2=0
                    time.sleep(2)

            elif flag3==1:
                if imgy3<=top2+2:
                    imgy3 +=pixmov
                    elv1.show_elev(imgy1)
                    elv1.ele_pos(imgy1)
                    elv2.show_elev(imgy2)
                    elv2.ele_pos(imgy2)
                    elv3.show_elev(imgy3)
                    elv3.ele_pos(imgy3)
                    elv4.show_elev(imgy4)
                    elv4.ele_pos(imgy4)

                else:
            
                    elv1.show_elev(imgy1)
                    elv1.ele_pos(imgy1)
                    elv2.show_elev(imgy2)
                    elv2.ele_pos(imgy2)
                    elv3.show_elev(imgy3)
                    elv3.ele_pos(imgy3)
                    elv4.show_elev(imgy4)
                    elv4.ele_pos(imgy4)
                    st2=-1
                    flag3=0
                    time.sleep(2)

            elif flag4==1:
                if imgy4<=top2+2:
                    imgy4 +=pixmov
                    elv1.show_elev(imgy1)
                    elv1.ele_pos(imgy1)
                    elv2.show_elev(imgy2)
                    elv2.ele_pos(imgy2)
                    elv3.show_elev(imgy3)
                    elv3.ele_pos(imgy3)
                    elv4.show_elev(imgy4)
                    elv4.ele_pos(imgy4)

                else:
            
                    elv1.show_elev(imgy1)
                    elv1.ele_pos(imgy1)
                    elv2.show_elev(imgy2)
                    elv2.ele_pos(imgy2)
                    elv3.show_elev(imgy3)
                    elv3.ele_pos(imgy3)
                    elv4.show_elev(imgy4)
                    elv4.ele_pos(imgy4)
                    st2=-1
                    flag4=0
                    time.sleep(2)



    if st3>=0:
        top2 = floor_top(st3)
        if dirtn==1:
            screen.fill((200,200,200))
            c=canvas()
            but = button(10)
            if flag1==1:
                if imgy1>=top2+2:
                    imgy1 -=pixmov
                    elv1.show_elev(imgy1)
                    elv1.ele_pos(imgy1)
                    elv2.show_elev(imgy2)
                    elv2.ele_pos(imgy2)
                    elv3.show_elev(imgy3)
                    elv3.ele_pos(imgy3)
                    elv4.show_elev(imgy4)
                    elv4.ele_pos(imgy4)

                else:
            
                    elv1.show_elev(imgy1)
                    elv1.ele_pos(imgy1)
                    elv2.show_elev(imgy2)
                    elv2.ele_pos(imgy2)
                    elv3.show_elev(imgy3)
                    elv3.ele_pos(imgy3)
                    elv4.show_elev(imgy4)
                    elv4.ele_pos(imgy4)
                    st3=-1
                    flag1=0
                    time.sleep(2)

            elif flag2==1:
                if imgy2>=top2+2:
                    imgy2 -=pixmov
                    elv1.show_elev(imgy1)
                    elv1.ele_pos(imgy1)
                    elv2.show_elev(imgy2)
                    elv2.ele_pos(imgy2)
                    elv3.show_elev(imgy3)
                    elv3.ele_pos(imgy3)
                    elv4.show_elev(imgy4)
                    elv4.ele_pos(imgy4)

                else:
            
                    elv1.show_elev(imgy1)
                    elv1.ele_pos(imgy1)
                    elv2.show_elev(imgy2)
                    elv2.ele_pos(imgy2)
                    elv3.show_elev(imgy3)
                    elv3.ele_pos(imgy3)
                    elv4.show_elev(imgy4)
                    elv4.ele_pos(imgy4)
                    st3=-1
                    flag2=0
                    time.sleep(2)

            elif flag3==1:
                if imgy3>=top2+2:
                    imgy3 -=pixmov
                    elv1.show_elev(imgy1)
                    elv1.ele_pos(imgy1)
                    elv2.show_elev(imgy2)
                    elv2.ele_pos(imgy2)
                    elv3.show_elev(imgy3)
                    elv3.ele_pos(imgy3)
                    elv4.show_elev(imgy4)
                    elv4.ele_pos(imgy4)

                else:
            
                    elv1.show_elev(imgy1)
                    elv1.ele_pos(imgy1)
                    elv2.show_elev(imgy2)
                    elv2.ele_pos(imgy2)
                    elv3.show_elev(imgy3)
                    elv3.ele_pos(imgy3)
                    elv4.show_elev(imgy4)
                    elv4.ele_pos(imgy4)
                    st3=-1
                    flag3=0
                    time.sleep(2)

            elif flag4==1:
                if imgy4>=top2+2:
                    imgy4 -=pixmov
                    elv1.show_elev(imgy1)
                    elv1.ele_pos(imgy1)
                    elv2.show_elev(imgy2)
                    elv2.ele_pos(imgy2)
                    elv3.show_elev(imgy3)
                    elv3.ele_pos(imgy3)
                    elv4.show_elev(imgy4)
                    elv4.ele_pos(imgy4)

                else:
            
                    elv1.show_elev(imgy1)
                    elv1.ele_pos(imgy1)
                    elv2.show_elev(imgy2)
                    elv2.ele_pos(imgy2)
                    elv3.show_elev(imgy3)
                    elv3.ele_pos(imgy3)
                    elv4.show_elev(imgy4)
                    elv4.ele_pos(imgy4)
                    st3=-1
                    flag4=0
                    time.sleep(2)
            
        elif dirtn==-1:
            screen.fill((200,200,200))
            c=canvas()
            but = button(10)
            print 'vaibhav'
            if flag1==1:
                print 'singh'
                if imgy1<=top2+2:
                    print 'khokhar'
                    imgy1 +=pixmov
                    elv1.show_elev(imgy1)
                    elv1.ele_pos(imgy1)
                    elv2.show_elev(imgy2)
                    elv2.ele_pos(imgy2)
                    elv3.show_elev(imgy3)
                    elv3.ele_pos(imgy3)
                    elv4.show_elev(imgy4)
                    elv4.ele_pos(imgy4)

                else:
            
                    elv1.show_elev(imgy1)
                    elv1.ele_pos(imgy1)
                    elv2.show_elev(imgy2)
                    elv2.ele_pos(imgy2)
                    elv3.show_elev(imgy3)
                    elv3.ele_pos(imgy3)
                    elv4.show_elev(imgy4)
                    elv4.ele_pos(imgy4)
                    st3=-1
                    flag1=0
                    time.sleep(2)

            elif flag2==1:
                if imgy2<=top2+2:
                    imgy2 +=pixmov
                    elv1.show_elev(imgy1)
                    elv1.ele_pos(imgy1)
                    elv2.show_elev(imgy2)
                    elv2.ele_pos(imgy2)
                    elv3.show_elev(imgy3)
                    elv3.ele_pos(imgy3)
                    elv4.show_elev(imgy4)
                    elv4.ele_pos(imgy4)

                else:
            
                    elv1.show_elev(imgy1)
                    elv1.ele_pos(imgy1)
                    elv2.show_elev(imgy2)
                    elv2.ele_pos(imgy2)
                    elv3.show_elev(imgy3)
                    elv3.ele_pos(imgy3)
                    elv4.show_elev(imgy4)
                    elv4.ele_pos(imgy4)
                    st3=-1
                    flag2=0
                    time.sleep(2)

            elif flag3==1:
                if imgy3<=top2+2:
                    imgy3 +=pixmov
                    elv1.show_elev(imgy1)
                    elv1.ele_pos(imgy1)
                    elv2.show_elev(imgy2)
                    elv2.ele_pos(imgy2)
                    elv3.show_elev(imgy3)
                    elv3.ele_pos(imgy3)
                    elv4.show_elev(imgy4)
                    elv4.ele_pos(imgy4)

                else:
            
                    elv1.show_elev(imgy1)
                    elv1.ele_pos(imgy1)
                    elv2.show_elev(imgy2)
                    elv2.ele_pos(imgy2)
                    elv3.show_elev(imgy3)
                    elv3.ele_pos(imgy3)
                    elv4.show_elev(imgy4)
                    elv4.ele_pos(imgy4)
                    st3=-1
                    flag3=0
                    time.sleep(2)

            elif flag4==1:
                if imgy4<=top2+2:
                    imgy4 +=pixmov
                    elv1.show_elev(imgy1)
                    elv1.ele_pos(imgy1)
                    elv2.show_elev(imgy2)
                    elv2.ele_pos(imgy2)
                    elv3.show_elev(imgy3)
                    elv3.ele_pos(imgy3)
                    elv4.show_elev(imgy4)
                    elv4.ele_pos(imgy4)

                else:
            
                    elv1.show_elev(imgy1)
                    elv1.ele_pos(imgy1)
                    elv2.show_elev(imgy2)
                    elv2.ele_pos(imgy2)
                    elv3.show_elev(imgy3)
                    elv3.ele_pos(imgy3)
                    elv4.show_elev(imgy4)
                    elv4.ele_pos(imgy4)
                    st3=-1
                    flag4=0
                    time.sleep(2)

    if st4>=0:
        top2 = floor_top(st4)
        if dirtn==1:
            screen.fill((200,200,200))
            c=canvas()
            but = button(10)
            if flag1==1:
                if imgy1>=top2+2:
                    imgy1 -=pixmov
                    elv1.show_elev(imgy1)
                    elv1.ele_pos(imgy1)
                    elv2.show_elev(imgy2)
                    elv2.ele_pos(imgy2)
                    elv3.show_elev(imgy3)
                    elv3.ele_pos(imgy3)
                    elv4.show_elev(imgy4)
                    elv4.ele_pos(imgy4)

                else:
            
                    elv1.show_elev(imgy1)
                    elv1.ele_pos(imgy1)
                    elv2.show_elev(imgy2)
                    elv2.ele_pos(imgy2)
                    elv3.show_elev(imgy3)
                    elv3.ele_pos(imgy3)
                    elv4.show_elev(imgy4)
                    elv4.ele_pos(imgy4)
                    st4=-1
                    flag1=0
                    time.sleep(2)

            elif flag2==1:
                if imgy2>=top2+2:
                    imgy2 -=pixmov
                    elv1.show_elev(imgy1)
                    elv1.ele_pos(imgy1)
                    elv2.show_elev(imgy2)
                    elv2.ele_pos(imgy2)
                    elv3.show_elev(imgy3)
                    elv3.ele_pos(imgy3)
                    elv4.show_elev(imgy4)
                    elv4.ele_pos(imgy4)

                else:
            
                    elv1.show_elev(imgy1)
                    elv1.ele_pos(imgy1)
                    elv2.show_elev(imgy2)
                    elv2.ele_pos(imgy2)
                    elv3.show_elev(imgy3)
                    elv3.ele_pos(imgy3)
                    elv4.show_elev(imgy4)
                    elv4.ele_pos(imgy4)
                    st4=-1
                    flag2=0
                    time.sleep(2)

            elif flag3==1:
                if imgy3>=top2+2:
                    imgy3 -=pixmov
                    elv1.show_elev(imgy1)
                    elv1.ele_pos(imgy1)
                    elv2.show_elev(imgy2)
                    elv2.ele_pos(imgy2)
                    elv3.show_elev(imgy3)
                    elv3.ele_pos(imgy3)
                    elv4.show_elev(imgy4)
                    elv4.ele_pos(imgy4)

                else:
            
                    elv1.show_elev(imgy1)
                    elv1.ele_pos(imgy1)
                    elv2.show_elev(imgy2)
                    elv2.ele_pos(imgy2)
                    elv3.show_elev(imgy3)
                    elv3.ele_pos(imgy3)
                    elv4.show_elev(imgy4)
                    elv4.ele_pos(imgy4)
                    st4=-1
                    flag3=0
                    time.sleep(2)

            elif flag4==1:
                if imgy4>=top2+2:
                    imgy4 -=pixmov
                    elv1.show_elev(imgy1)
                    elv1.ele_pos(imgy1)
                    elv2.show_elev(imgy2)
                    elv2.ele_pos(imgy2)
                    elv3.show_elev(imgy3)
                    elv3.ele_pos(imgy3)
                    elv4.show_elev(imgy4)
                    elv4.ele_pos(imgy4)

                else:
            
                    elv1.show_elev(imgy1)
                    elv1.ele_pos(imgy1)
                    elv2.show_elev(imgy2)
                    elv2.ele_pos(imgy2)
                    elv3.show_elev(imgy3)
                    elv3.ele_pos(imgy3)
                    elv4.show_elev(imgy4)
                    elv4.ele_pos(imgy4)
                    st4=-1
                    flag4=0
                    time.sleep(2)
            
        elif dirtn==-1:
            screen.fill((200,200,200))
            c=canvas()
            but = button(10)
            print 'vaibhav'
            if flag1==1:
                print 'singh'
                if imgy1<=top2+2:
                    print 'khokhar'
                    imgy1 +=pixmov
                    elv1.show_elev(imgy1)
                    elv1.ele_pos(imgy1)
                    elv2.show_elev(imgy2)
                    elv2.ele_pos(imgy2)
                    elv3.show_elev(imgy3)
                    elv3.ele_pos(imgy3)
                    elv4.show_elev(imgy4)
                    elv4.ele_pos(imgy4)

                else:
            
                    elv1.show_elev(imgy1)
                    elv1.ele_pos(imgy1)
                    elv2.show_elev(imgy2)
                    elv2.ele_pos(imgy2)
                    elv3.show_elev(imgy3)
                    elv3.ele_pos(imgy3)
                    elv4.show_elev(imgy4)
                    elv4.ele_pos(imgy4)
                    st4=-1
                    flag1=0
                    time.sleep(2)

            elif flag2==1:
                if imgy2<=top2+2:
                    imgy2 +=pixmov
                    elv1.show_elev(imgy1)
                    elv1.ele_pos(imgy1)
                    elv2.show_elev(imgy2)
                    elv2.ele_pos(imgy2)
                    elv3.show_elev(imgy3)
                    elv3.ele_pos(imgy3)
                    elv4.show_elev(imgy4)
                    elv4.ele_pos(imgy4)

                else:
            
                    elv1.show_elev(imgy1)
                    elv1.ele_pos(imgy1)
                    elv2.show_elev(imgy2)
                    elv2.ele_pos(imgy2)
                    elv3.show_elev(imgy3)
                    elv3.ele_pos(imgy3)
                    elv4.show_elev(imgy4)
                    elv4.ele_pos(imgy4)
                    st4=-1
                    flag2=0
                    time.sleep(2)

            elif flag3==1:
                if imgy3<=top2+2:
                    imgy3 +=pixmov
                    elv1.show_elev(imgy1)
                    elv1.ele_pos(imgy1)
                    elv2.show_elev(imgy2)
                    elv2.ele_pos(imgy2)
                    elv3.show_elev(imgy3)
                    elv3.ele_pos(imgy3)
                    elv4.show_elev(imgy4)
                    elv4.ele_pos(imgy4)

                else:
            
                    elv1.show_elev(imgy1)
                    elv1.ele_pos(imgy1)
                    elv2.show_elev(imgy2)
                    elv2.ele_pos(imgy2)
                    elv3.show_elev(imgy3)
                    elv3.ele_pos(imgy3)
                    elv4.show_elev(imgy4)
                    elv4.ele_pos(imgy4)
                    st4=-1
                    flag3=0
                    time.sleep(2)

            elif flag4==1:
                if imgy4<=top2+2:
                    imgy4 +=pixmov
                    elv1.show_elev(imgy1)
                    elv1.ele_pos(imgy1)
                    elv2.show_elev(imgy2)
                    elv2.ele_pos(imgy2)
                    elv3.show_elev(imgy3)
                    elv3.ele_pos(imgy3)
                    elv4.show_elev(imgy4)
                    elv4.ele_pos(imgy4)

                else:
            
                    elv1.show_elev(imgy1)
                    elv1.ele_pos(imgy1)
                    elv2.show_elev(imgy2)
                    elv2.ele_pos(imgy2)
                    elv3.show_elev(imgy3)
                    elv3.ele_pos(imgy3)
                    elv4.show_elev(imgy4)
                    elv4.ele_pos(imgy4)
                    st4=-1
                    flag4=0
                    time.sleep(2)

    if st5>=0:
        top2 = floor_top(st5)
        if dirtn==1:
            screen.fill((200,200,200))
            c=canvas()
            but = button(10)
            if flag1==1:
                if imgy1>=top2+2:
                    imgy1 -=pixmov
                    elv1.show_elev(imgy1)
                    elv1.ele_pos(imgy1)
                    elv2.show_elev(imgy2)
                    elv2.ele_pos(imgy2)
                    elv3.show_elev(imgy3)
                    elv3.ele_pos(imgy3)
                    elv4.show_elev(imgy4)
                    elv4.ele_pos(imgy4)

                else:
            
                    elv1.show_elev(imgy1)
                    elv1.ele_pos(imgy1)
                    elv2.show_elev(imgy2)
                    elv2.ele_pos(imgy2)
                    elv3.show_elev(imgy3)
                    elv3.ele_pos(imgy3)
                    elv4.show_elev(imgy4)
                    elv4.ele_pos(imgy4)
                    st5=-1
                    flag1=0
                    time.sleep(2)

            elif flag2==1:
                if imgy2>=top2+2:
                    imgy2 -=pixmov
                    elv1.show_elev(imgy1)
                    elv1.ele_pos(imgy1)
                    elv2.show_elev(imgy2)
                    elv2.ele_pos(imgy2)
                    elv3.show_elev(imgy3)
                    elv3.ele_pos(imgy3)
                    elv4.show_elev(imgy4)
                    elv4.ele_pos(imgy4)

                else:
            
                    elv1.show_elev(imgy1)
                    elv1.ele_pos(imgy1)
                    elv2.show_elev(imgy2)
                    elv2.ele_pos(imgy2)
                    elv3.show_elev(imgy3)
                    elv3.ele_pos(imgy3)
                    elv4.show_elev(imgy4)
                    elv4.ele_pos(imgy4)
                    st5=-1
                    flag2=0
                    time.sleep(2)

            elif flag3==1:
                if imgy3>=top2+2:
                    imgy3 -=pixmov
                    elv1.show_elev(imgy1)
                    elv1.ele_pos(imgy1)
                    elv2.show_elev(imgy2)
                    elv2.ele_pos(imgy2)
                    elv3.show_elev(imgy3)
                    elv3.ele_pos(imgy3)
                    elv4.show_elev(imgy4)
                    elv4.ele_pos(imgy4)

                else:
            
                    elv1.show_elev(imgy1)
                    elv1.ele_pos(imgy1)
                    elv2.show_elev(imgy2)
                    elv2.ele_pos(imgy2)
                    elv3.show_elev(imgy3)
                    elv3.ele_pos(imgy3)
                    elv4.show_elev(imgy4)
                    elv4.ele_pos(imgy4)
                    st5=-1
                    flag3=0
                    time.sleep(2)

            elif flag4==1:
                if imgy4>=top2+2:
                    imgy4 -=pixmov
                    elv1.show_elev(imgy1)
                    elv1.ele_pos(imgy1)
                    elv2.show_elev(imgy2)
                    elv2.ele_pos(imgy2)
                    elv3.show_elev(imgy3)
                    elv3.ele_pos(imgy3)
                    elv4.show_elev(imgy4)
                    elv4.ele_pos(imgy4)

                else:
            
                    elv1.show_elev(imgy1)
                    elv1.ele_pos(imgy1)
                    elv2.show_elev(imgy2)
                    elv2.ele_pos(imgy2)
                    elv3.show_elev(imgy3)
                    elv3.ele_pos(imgy3)
                    elv4.show_elev(imgy4)
                    elv4.ele_pos(imgy4)
                    st5=-1
                    flag4=0
                    time.sleep(2)
            
        elif dirtn==-1:
            screen.fill((200,200,200))
            c=canvas()
            but = button(10)
            print 'vaibhav'
            if flag1==1:
                print 'singh'
                if imgy1<=top2+2:
                    print 'khokhar'
                    imgy1 +=pixmov
                    elv1.show_elev(imgy1)
                    elv1.ele_pos(imgy1)
                    elv2.show_elev(imgy2)
                    elv2.ele_pos(imgy2)
                    elv3.show_elev(imgy3)
                    elv3.ele_pos(imgy3)
                    elv4.show_elev(imgy4)
                    elv4.ele_pos(imgy4)

                else:
            
                    elv1.show_elev(imgy1)
                    elv1.ele_pos(imgy1)
                    elv2.show_elev(imgy2)
                    elv2.ele_pos(imgy2)
                    elv3.show_elev(imgy3)
                    elv3.ele_pos(imgy3)
                    elv4.show_elev(imgy4)
                    elv4.ele_pos(imgy4)
                    st5=-1
                    flag1=0
                    time.sleep(2)

            elif flag2==1:
                if imgy2<=top2+2:
                    imgy2 +=pixmov
                    elv1.show_elev(imgy1)
                    elv1.ele_pos(imgy1)
                    elv2.show_elev(imgy2)
                    elv2.ele_pos(imgy2)
                    elv3.show_elev(imgy3)
                    elv3.ele_pos(imgy3)
                    elv4.show_elev(imgy4)
                    elv4.ele_pos(imgy4)

                else:
            
                    elv1.show_elev(imgy1)
                    elv1.ele_pos(imgy1)
                    elv2.show_elev(imgy2)
                    elv2.ele_pos(imgy2)
                    elv3.show_elev(imgy3)
                    elv3.ele_pos(imgy3)
                    elv4.show_elev(imgy4)
                    elv4.ele_pos(imgy4)
                    st5=-1
                    flag2=0
                    time.sleep(2)

            elif flag3==1:
                if imgy3<=top2+2:
                    imgy3 +=pixmov
                    elv1.show_elev(imgy1)
                    elv1.ele_pos(imgy1)
                    elv2.show_elev(imgy2)
                    elv2.ele_pos(imgy2)
                    elv3.show_elev(imgy3)
                    elv3.ele_pos(imgy3)
                    elv4.show_elev(imgy4)
                    elv4.ele_pos(imgy4)

                else:
            
                    elv1.show_elev(imgy1)
                    elv1.ele_pos(imgy1)
                    elv2.show_elev(imgy2)
                    elv2.ele_pos(imgy2)
                    elv3.show_elev(imgy3)
                    elv3.ele_pos(imgy3)
                    elv4.show_elev(imgy4)
                    elv4.ele_pos(imgy4)
                    st5=-1
                    flag3=0
                    time.sleep(2)

            elif flag4==1:
                if imgy4<=top2+2:
                    imgy4 +=pixmov
                    elv1.show_elev(imgy1)
                    elv1.ele_pos(imgy1)
                    elv2.show_elev(imgy2)
                    elv2.ele_pos(imgy2)
                    elv3.show_elev(imgy3)
                    elv3.ele_pos(imgy3)
                    elv4.show_elev(imgy4)
                    elv4.ele_pos(imgy4)

                else:
            
                    elv1.show_elev(imgy1)
                    elv1.ele_pos(imgy1)
                    elv2.show_elev(imgy2)
                    elv2.ele_pos(imgy2)
                    elv3.show_elev(imgy3)
                    elv3.ele_pos(imgy3)
                    elv4.show_elev(imgy4)
                    elv4.ele_pos(imgy4)
                    st5=-1
                    flag4=0
                    time.sleep(2)

     

                
            
            
    
    if curr2>0: 
        
        top1 = floor_top(curr2)
        screen.fill((200,200,200))
        c=canvas()
        but = button(10)
        
        a=(imgy1-top1)
        b=(imgy2-top1)
        c=(imgy3-top1)
        d=(imgy4-top1)
        e=[a,b,c,d]   
        first=max(filter(lambda x:x<=0,e))
        if first==(imgy1-top1) and (imgy1-top1)<=0:
        
            
            if imgy1 <top1-2 :
                print '1'
                imgy1 +=pixmov
                elv1.show_elev(imgy1)
                elv1.ele_pos(imgy1)
                elv2.show_elev(imgy2)
                elv2.ele_pos(imgy2)
                elv3.show_elev(imgy3)
                elv3.ele_pos(imgy3)
                elv4.show_elev(imgy4)
                elv4.ele_pos(imgy4)
                dirtn=-1

            else:
            
            
                elv1.show_elev(imgy1)
                elv1.ele_pos(imgy1)
                elv2.show_elev(imgy2)
                elv2.ele_pos(imgy2)
                elv3.show_elev(imgy3)
                elv3.ele_pos(imgy3)
                elv4.show_elev(imgy4)
                elv4.ele_pos(imgy4)
                list_down[curr2-1]=0
                curr2=0
                dirtn = -1
                flag1=1
                time.sleep(2)

        elif first==(imgy2-top1) and (imgy2-top1)<=0:

            if imgy2 <top1-2 :
                print '2'
                imgy2 +=pixmov
                elv1.show_elev(imgy1)
                elv1.ele_pos(imgy1)
                elv2.show_elev(imgy2)
                elv2.ele_pos(imgy2)
                elv3.show_elev(imgy3)
                elv3.ele_pos(imgy3)
                elv4.show_elev(imgy4)
                elv4.ele_pos(imgy4)
                dirtn=-1

            else:
            
            
                elv1.show_elev(imgy1)
                elv1.ele_pos(imgy1)
                elv2.show_elev(imgy2)
                elv2.ele_pos(imgy2)
                elv3.show_elev(imgy3)
                elv3.ele_pos(imgy3)
                elv4.show_elev(imgy4)
                elv4.ele_pos(imgy4)
                list_down[curr2-1]=0
                curr2=0
                dirtn = -1
                flag2=1
                time.sleep(2)

        elif first==(imgy3-top1) and (imgy3-top1)<=0:
            if imgy3 <top1-2 :
                print '3'
                imgy3 +=pixmov
                elv1.show_elev(imgy1)
                elv1.ele_pos(imgy1)
                elv2.show_elev(imgy2)
                elv2.ele_pos(imgy2)
                elv3.show_elev(imgy3)
                elv3.ele_pos(imgy3)
                elv4.show_elev(imgy4)
                elv4.ele_pos(imgy4)
                dirtn=-1

            else:
            
            
                elv1.show_elev(imgy1)
                elv1.ele_pos(imgy1)
                elv2.show_elev(imgy2)
                elv2.ele_pos(imgy2)
                elv3.show_elev(imgy3)
                elv3.ele_pos(imgy3)
                elv4.show_elev(imgy4)
                elv4.ele_pos(imgy4)
                list_down[curr2-1]=0
                curr2=0
                dirtn = -1
                flag3=1
                time.sleep(2)

        elif first==(imgy4-top1) and (imgy4-top1)<=0:

            if imgy4 <top1-2:
                print '4'
                imgy4 +=pixmov
                elv1.show_elev(imgy1)
                elv1.ele_pos(imgy1)
                elv2.show_elev(imgy2)
                elv2.ele_pos(imgy2)
                elv3.show_elev(imgy3)
                elv3.ele_pos(imgy3)
                elv4.show_elev(imgy4)
                elv4.ele_pos(imgy4)
                dirtn=-1
                print imgy4-top1
            else:
            
                print 'reached'
                elv1.show_elev(imgy1)
                elv1.ele_pos(imgy1)
                elv2.show_elev(imgy2)
                elv2.ele_pos(imgy2)
                elv3.show_elev(imgy3)
                elv3.ele_pos(imgy3)
                elv4.show_elev(imgy4)
                elv4.ele_pos(imgy4)
                list_down[curr2-1]=0
                curr2=0
                dirtn = -1
                flag4=1
                time.sleep(2)
        


        
    pygame.display.update()
    fpsTime.tick(FPS)
