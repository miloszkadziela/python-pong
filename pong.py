import pygame, sys

black = (0, 0, 0);
white = (255, 255, 255)
pygame.init()
'''
INTORDUCING COUTER VARIABLE AND SETTING THE GAME SCREEN
'''
counter = 0 #implementing a variable responsible for storing the score
scr = pygame.display.set_mode((800, 600)) #declaring the size of window
win = scr.get_rect()
'''
DEFINING THE PADDLE AND THE BALL
'''
box1 = pygame.Rect(0, 0, 12, 12) #box1 is the ball. Size of the ball
box1.center = win.center #starting postition of the ball
platform1 = pygame.Rect(0, 0, 110, 10) #size of the paddle
platform1.midbottom = win.midbottom #starting position of the paddle
step = 8 #defines the movement of the paddle
'''
DEFINING A FUNCTION RESPONSIBLE FOR BALL AND PADDLE MOVEMENT
'''
def game_movement(box1_left, box1_right, box1_top, win_left,\
 win_right, win_top, platform1_left, platform1_right):
    if box1_left < win_left or box1_right > win_right:
        vec[0] = -vec[0]
    if box1_top < win_top:
        vec[1] = -vec[1]
    if platform1_left < win_left:
        platform1.left = win.left
    if platform1_right > win_right:
        platform1.right = win.right
'''
DEFINING A FUNCTION RESPONSIBLE FOR OBJECT COLLISION
'''
def object_collision(box1_bottom, platform1_top, box1_centerx,\
 platform1_centerx, box1_w, platform1_w, vec):
    global counter
    if box1_bottom > platform1_top and \
                    abs(box1_centerx - platform1_centerx)\
                     < (box1_w + platform1_w) / 2:
        vec[1] = -vec[1]
        counter = counter + 1
'''
DEFINING A FUNCTION RESPONSIBLE FOR DISPLAYING THE ON SCREEN MESSAGES
'''
def messages(display_msg, msg, msg_box, score, score_box, \
display_lost, lost, lost_box, gameover):
    if display_msg == True:
        scr.blit(msg, msg_box)
        scr.blit(score, score_box)
    if display_lost == True:
        display_msg = False
        scr.blit(lost, lost_box)
        return True
    else:
        return False
'''
DEFINING A FUNCTION RESPONSIBLE FOR END-GAME CONDITION
'''
def game_lost(box1_bottom, win_bottom):
    if box1_bottom > win_bottom:
        return True
    else:
        return False
'''
DECLARING ALL VARIABLES CONNECTED WITH MESSAGES (FONT, SIZE, COLOUR etc.)
'''
fps = pygame.time.Clock()
vec = [2, 2] #declaring the vector of the ball
myfont = pygame.font.Font('freesansbold.ttf', 12) #declaring the main_fnt
myfont_lost = pygame.font.Font('freesansbold.ttf', 38) #2nd font
msg = myfont.render("Pong", True, white) #declaring the parameters of msg
msg_box = msg.get_rect() 
msg_box.center = win.center
lost = myfont_lost.render("You lost!", True, white)
lost_box = msg.get_rect() #getting the space for msg box
lost_box.top = win.top #declaring the position of msg box
score = myfont.render("Score = {0}".format(counter), True, white)
score_box = score.get_rect() #getting the space for score msg box
score_box.topright = win.topright #declaring the position of msg box
display_lost = False #setting the boolean variable
display_msg = True #setting the boolean variable
gameover = False #setting the boolean variable
pygame.key.set_repeat(5, 5)
'''
MAIN LOOP
'''
while gameover == False:
    score = myfont.render("Score = {0}".format(counter), True, white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: #detecting paddle movement
                platform1 = platform1.move(-step, 0)
            if event.key == pygame.K_RIGHT: #detecting paddle movement
                platform1 = platform1.move(step, 0)

    '''
    CALLING ALL FUNCTIONS RESPONSIBLE FOR GAME FUNCTIONALITY
    '''
    box1 = box1.move(vec) #implementing the movement of the box1(ball)
    scr.fill(black) #filling the program background with black
    game_movement(box1.left, box1.right, box1.top, win.left, \
    win.right, win.top, platform1.left, platform1.right)
    object_collision(box1.bottom, platform1.top, box1.centerx, \
    platform1.centerx, box1.w, platform1.w, vec)
    display_lost = game_lost(box1.bottom, win.bottom) #displays lost msg
    gameover = messages(display_msg, msg, msg_box, score, \
    score_box, display_lost, lost, lost_box, gameover) #prints lost scr
    pygame.draw.rect(scr, white, box1) #drawing box1 (ball)
    pygame.draw.rect(scr, white, platform1) #drawing platform1 (paddle)
    pygame.display.flip()
    fps.tick(120) #setting the fps.tick rate
