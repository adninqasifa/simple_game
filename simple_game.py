# Created by Adnin Qasifa
# make Simple Game

import pygame
pygame.init()

win = pygame.display.set_mode((852,480)) # This line creates a window of 852 width, 480 height
pygame.display.set_caption("Simple Game by Adnin Qasifa")

# This goes outside the while loop, near the top of the program
walkRight = [pygame.image.load(r'D:\my_exercise_programming\python_workspace\simple_game\R1.png'), pygame.image.load(r'D:\my_exercise_programming\python_workspace\simple_game\R2.png'),
pygame.image.load(r'D:\my_exercise_programming\python_workspace\simple_game\R3.png'), pygame.image.load(r'D:\my_exercise_programming\python_workspace\simple_game\R4.png'),
pygame.image.load(r'D:\my_exercise_programming\python_workspace\simple_game\R5.png'), pygame.image.load(r'D:\my_exercise_programming\python_workspace\simple_game\R6.png'),
pygame.image.load(r'D:\my_exercise_programming\python_workspace\simple_game\R7.png'), pygame.image.load(r'D:\my_exercise_programming\python_workspace\simple_game\R8.png'),
pygame.image.load(r'D:\my_exercise_programming\python_workspace\simple_game\R9.png')]

walkLeft = [pygame.image.load(r'D:\my_exercise_programming\python_workspace\simple_game\L1.png'), pygame.image.load(r'D:\my_exercise_programming\python_workspace\simple_game\L2.png'),
pygame.image.load(r'D:\my_exercise_programming\python_workspace\simple_game\L3.png'), pygame.image.load(r'D:\my_exercise_programming\python_workspace\simple_game\L4.png'),
pygame.image.load(r'D:\my_exercise_programming\python_workspace\simple_game\L5.png'), pygame.image.load(r'D:\my_exercise_programming\python_workspace\simple_game\L6.png'),
pygame.image.load(r'D:\my_exercise_programming\python_workspace\simple_game\L7.png'), pygame.image.load(r'D:\my_exercise_programming\python_workspace\simple_game\L8.png'),
pygame.image.load(r'D:\my_exercise_programming\python_workspace\simple_game\L9.png')]

bg = pygame.image.load(r'D:\my_exercise_programming\python_workspace\simple_game\bg.jpg') # background don't use .png
logo = pygame.image.load(r'D:\my_exercise_programming\python_workspace\simple_game\my_logo.png') # logo don't use .png
logo = pygame.transform.scale(logo, (50,50)) # picturew scale (x,y)
char = pygame.image.load(r'D:\my_exercise_programming\python_workspace\simple_game\standing.png')

clock = pygame.time.Clock() # for the game velocity

#bulletSound = pygame.mixer.Sound(r"D:\my_exercise_programming\python_workspace\simple_game\bullet1.wav")
#hitSound = pygame.mixer.Sound(r"D:\my_exercise_programming\python_workspace\simple_game\hit1.wav")

#music = pygame.mixer.music.load(r"D:\my_exercise_programming\python_workspace\simple_game\music.mp3")
#pygame.mixer.music.play(-1) # -1 will ensure the song keeps looping

score = 0


class player(object):
    def __init__(self,x,y,width,height): # Initialization
        self.x         = x               # four main character
        self.y         = y               # four main character
        self.width     = width           # four main character
        self.height    = height          # four main character
        self.vel       = 8               # velocity of figure/player
        self.isJump    = False
        self.left      = False
        self.right     = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing  = True
        self.hitbox    = (self.x + 17, self.y + 11, 29, 52)

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if not (self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount +=1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x + 20, self.y, 28, 60) # The elements in the hitbox are (top left x, top left y, width, height)
        #pygame.draw.rect(win, (255,0,0), self.hitbox, 2) # To draw the hit box around the player/batas daerah player

    def hit(self):

        self.x         = 100 # We are resetting the player position
        self.y         = 410
        self.isJump0   = False # Fixing Bugs
        self.jumpCount = 10 # Fixing Bugs
        self.walkCount = 0
        font1 = pygame.font.SysFont('comicsans', 100)
        text  = font1.render('-5', 1, (255,0,0))
        win.blit(text, (420 - (text.get_width()/2),200)) # Posisi Score
        pygame.display.update()
        i = 0
        while i < 200:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 201
                    pygame.quit()
        # After we are hit we are going to display a message to the screen for a certain period of time

class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x      = x
        self.y      = y
        self.radius = radius
        self.color  = color
        self.facing = facing
        self.vel    = 8 * facing

    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


class enemy(object):
    # We will place these lists inside of a class enemy(object)
    walkRight = [pygame.image.load(r'D:\my_exercise_programming\python_workspace\simple_game\R1E.png'), pygame.image.load(r'D:\my_exercise_programming\python_workspace\simple_game\R2E.png'),
    pygame.image.load(r'D:\my_exercise_programming\python_workspace\simple_game\R3E.png'), pygame.image.load(r'D:\my_exercise_programming\python_workspace\simple_game\R4E.png'),
    pygame.image.load(r'D:\my_exercise_programming\python_workspace\simple_game\R5E.png'), pygame.image.load(r'D:\my_exercise_programming\python_workspace\simple_game\R6E.png'),
    pygame.image.load(r'D:\my_exercise_programming\python_workspace\simple_game\R7E.png'), pygame.image.load(r'D:\my_exercise_programming\python_workspace\simple_game\R8E.png'),
    pygame.image.load(r'D:\my_exercise_programming\python_workspace\simple_game\R9E.png'), pygame.image.load(r'D:\my_exercise_programming\python_workspace\simple_game\R10E.png'),
    pygame.image.load(r'D:\my_exercise_programming\python_workspace\simple_game\R11E.png')]

    walkLeft = [pygame.image.load(r'D:\my_exercise_programming\python_workspace\simple_game\L1E.png'), pygame.image.load(r'D:\my_exercise_programming\python_workspace\simple_game\L2E.png'),
    pygame.image.load(r'D:\my_exercise_programming\python_workspace\simple_game\L3E.png'), pygame.image.load(r'D:\my_exercise_programming\python_workspace\simple_game\L4E.png'),
    pygame.image.load(r'D:\my_exercise_programming\python_workspace\simple_game\L5E.png'), pygame.image.load(r'D:\my_exercise_programming\python_workspace\simple_game\L6E.png'),
    pygame.image.load(r'D:\my_exercise_programming\python_workspace\simple_game\L7E.png'), pygame.image.load(r'D:\my_exercise_programming\python_workspace\simple_game\L8E.png'),

    pygame.image.load(r'D:\my_exercise_programming\python_workspace\simple_game\L9E.png'), pygame.image.load(r'D:\my_exercise_programming\python_workspace\simple_game\L10E.png'),
    pygame.image.load(r'D:\my_exercise_programming\python_workspace\simple_game\L11E.png')]

    # Goes inside the enemy class
    def __init__(self, x, y, width, height, end):
        self.x         = x
        self.y         = y
        self.width     = width
        self.height    = height
        self.path      = [x, end]  # This will define where our enemy starts and finishes their path.
        self.walkCount = 0
        self.vel       = 3
        self.hitbox    = (self.x + 17, self.y + 2, 31, 57)
        self.health    = 10
        self.visible   = True

    def draw(self,win): # almost same with player(object)
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 33: # Since we have 11 images for each animtion our upper bound is 33. We will show each image for 3 frames. 3 x 11 = 33
                self.walkCount = 0

            if self.vel > 0: # If we are moving to the right we will display our walkRight images
                win.blit(self.walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            else:  # Otherwise we will display the walkLeft images
                win.blit(self.walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            # health bar
            pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10)) # (255,0,0) = color red bar
            pygame.draw.rect(win, (0,255,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10)) # (0,255,0) = color green
            self.hitbox = (self.x + 17, self.y + 2, 31, 57)
            #pygame.draw.rect(win, (255,0,0), self.hitbox,2) # To draws the hit box around the enemy/Batas daerah enemy

    def move(self):
        if self.vel > 0:  # If we are moving right
            if self.x < self.path[1] + self.vel: # If we have not reached the furthest right point on our path.
                self.x += self.vel
            else: # Change direction and move back the other way
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 1
        else: # If we are moving left
            if self.x > self.path[0] - self.vel: # If we have not reached the furthest left point on our path
                self.x += self.vel
            else:  # Change direction
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0

    def hit(self):  # This will display when the enemy is hit
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
        print("hit")


# Draw the Bullets.
def redrawGameWindow():
    win.blit(bg, (0,0)) # This will draw our background image at (0,0)
    win.blit(logo, (800,0)) # logo position (x,y)
    text = font.render("Score: " + str(score), 2, (0,0,0)) # Arguments are: text, anti-aliasing, color
    win.blit(text, (390, 10))
    man.draw(win)
    goblin.draw(win)
    for bullet in bullets:
        bullet.draw(win)

    pygame.display.update()

#mainloop
font      = pygame.font.SysFont("comicsans", 30, True) # The first argument is the font, next is size, and then True to make our font bold
man       = player(200, 410, 64, 64)   # figure. x = 100 (batas kiri player berdiri)
goblin    = enemy(30, 410, 64, 64, 786) # enemy. x=30 (batas kiri ogblin berjalan), end = 786 (batas kanan goblin berjalan)
shootLoop = 0
bullets   = [] # This step is to create a list which will store all of our bullet objects. This goes right above the while loop.
run       = True
while run:
    clock.tick(27) # for the game velocity (27)

    if goblin.visible == True:
        if man.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblin.hitbox[1]:
            if man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0] and man.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
                man.hit()
                score -= 5

    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Collision/tumbukan/batas daerah figure
    for bullet in bullets:
        if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]: # Checks x coordnats
            if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]: # Checks y coordinats
                #hitSound.play()
                goblin.hit() # calls enemy hit method
                score += 1
                bullets.pop(bullets.index(bullet)) # removes bullet from bullet list

        if bullet.x < 840 and bullet.x > 0:
            bullet.x += bullet.vel # Moves the bullet by its vel
        else:
            bullets.pop(bullets.index(bullet)) # This will remove the bullet if it is off the screen.

    keys = pygame.key.get_pressed() # This will give us a dictionary where each key has a value of 1 or 0. Where 1 is pressed and 0 is not pressed.

    # Goes inside the while loop, under keys = ...
    # This will create a bullet starting at the middle of the character.
    if keys[pygame.K_SPACE] and shootLoop == 0:
        #bulletSound.play()
        if man.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 5: # This will make sure we cannot exceed 5 bullets on the screen.We have 10 bullets.
            bullets.append(projectile(round(man.x + man.width //2), round(man.y + man.height//2), 6, (0,0,0), facing))

    if keys[pygame.K_LEFT] and man.x > man.vel: # Making sure the top left position of our character is greater than our vel so we never move off the screen.
        man.x -= man.vel
        man.left     = True
        man.right    = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < 840 - man.width - man.vel:  # Making sure the top right corner of our character is less than the screen width - its width.
        man.x += man.vel
        man.right    = True
        man.left     = False
        man.standing = False
    else:
        man.standing  = True
        man.walkCount = 0

    if not(man.isJump):
        if keys[pygame.K_UP]:   # key for jump
            man.isJump    = True
            man.right     = False
            man.left      = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg # (y -= (jumpCount * abs(jumpCount)) * 0.5)
            man.jumpCount -= 1
        else: # This will execute if our jump is finished
            man.isJump    = False
            man.jumpCount = 10

    redrawGameWindow()


pygame.quit()

# TODO Side Scrolling Game
