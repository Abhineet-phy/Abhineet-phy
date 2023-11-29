#_______________________My First Game_______________________
#We'll create the snakes game
import pygame
import random
pygame.init()

#Colors
white=(255,255,255)
red=(140,0,0)
black=(0,0,0)
brown=(92,64,51)

#Creating Window
screen_width=1366
screen_height=768
# gameWindow=pygame.display.set_mode(FULLSCREEN)
# gameWindow=pygame.display.set_mode((screen_width,screen_height)) 

flags = pygame.FULLSCREEN
gameWindow = pygame.display.set_mode((screen_width, screen_height), flags, vsync=1)

# #Background Image
bgimg1=pygame.image.load("welc.jpg")
bgimg1=pygame.transform.scale(bgimg1,(screen_width,screen_height)).convert_alpha()
bgimg2=pygame.image.load("grass_final.jpg")
bgimg2=pygame.transform.scale(bgimg2,(screen_width,screen_height)).convert_alpha()

#Creating TitleS
pygame.display.set_caption("Snake-Game")
pygame.display.update()
clock=pygame.time.Clock() #importing time function from pygame
font1=pygame.font.SysFont("Lucida Console",80)
font2=pygame.font.SysFont("Lucida Console",20)
font3=pygame.font.SysFont("Lucida Console",50)
#font2=pygame.font.SysFont("Lucida Console",20)

fps=15

def text_screen1(text,color,x,y):
    screen_text=font1.render(text,True,color) #font.render is a function of pygame that is used for displaying our font
    gameWindow.blit(screen_text,[x,y]) #This is a function to update our screen
def text_screen3(text,color,x,y):
    screen_text=font3.render(text,True,color) #font.render is a function of pygame that is used for displaying our font
    gameWindow.blit(screen_text,[x,y]) #This is a function to update our screen

def text_screen2(text,color,x,y):
    screen_text=font2.render(text,True,color) #font.render is a function of pygame that is used for displaying our font
    gameWindow.blit(screen_text,[x,y]) #This is a function to update our screen


def plot_snake(gameWindow,color,snake_list,snake_size):    
    # print(snake_list)
    for x,y in snake_list:
        pygame.draw.rect(gameWindow,color,[x,y,snake_size,snake_size])

def welcome():
    exit_game=False
    while not exit_game:
        # gameWindow.fill((222,222,220))
        gameWindow.blit(bgimg1,(0,0))
        text_screen1("Welcome to Snakes",black,100,300)
        text_screen2("Press space to play",black,350,450)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    gameloop()
        pygame.display.update()
        clock.tick(fps)        


#Game Loop
def gameloop():
    
    #Control Variables
    exit_game=False
    game_over=False
    snake_x=screen_width/2
    snake_y=screen_height/2
    snake_size=food_size=50
    velocity_x=0
    velocity_y=0
    velocity_snake=snake_size/2
    snake_list=[]
    snake_length=1
    food_x=random.randint(80,screen_width-80)
    food_y=random.randint(80,screen_height-80)
    score=0
    with open("hiscore.txt","r") as f: #This is to read our hiscore file 
        hiscore=f.read()
    fps=15
    # fps=60

    while not exit_game:
        if game_over:
            with open("hiscore.txt","w") as f:
                f.write(str(hiscore))
            gameWindow.fill(black)
            text_screen3("Game Over! Press enter to Continue",white,screen_width/2-450,screen_height/2)

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        welcome()
                            

        else:    
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True

                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        velocity_x=velocity_snake
                        velocity_y=0

                    if event.key==pygame.K_LEFT:
                        velocity_x=-velocity_snake
                        velocity_y=0

                    if event.key==pygame.K_UP:
                        velocity_y=-velocity_snake
                        velocity_x=0 

                    if event.key==pygame.K_DOWN:
                        velocity_y=velocity_snake
                        velocity_x=0   

                    if event.key==pygame.K_q:
                        fps=10    

            snake_x+=velocity_x
            snake_y+=velocity_y

            if abs(snake_x-food_x)<35 and abs(snake_y-food_y)<35:
                score+=10
                fps+=2
                # # print(fps)
                if fps>=100:
                    fps=100
                
                # print("SCORE:",score*10)
                food_x=random.randint(80,screen_width-80)
                food_y=random.randint(80,screen_height-80)
                snake_length+=1 #after eating food the legth of snake increases 
                if score>int(hiscore):
                    hiscore=score


            # gameWindow.fill(white)  
            gameWindow.blit(bgimg2,(0,0))  
            
            pygame.draw.rect(gameWindow,red,[food_x,food_y,food_size,food_size])
            text_screen3("SCORE:"+str(score)+"  Hiscore:"+str(hiscore),brown,screen_width/2-300,30) #here the first arguement is the text that will be printed on our screen

            head=[] #when our game begins, head is the initial part of snake
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list)>snake_length:
                del snake_list[0]
            
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over=True

            if head in snake_list[:-1]:
                game_over=True
            plot_snake(gameWindow,black,snake_list,snake_size)
        pygame.display.update()
        clock.tick(fps) #a frame refers to 1 update of our screen so fps will make the program update 30 times


    pygame.quit()
    quit()    

#Calling gameloop function    
welcome()
