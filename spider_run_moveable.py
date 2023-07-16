
import os, pygame, sys


class Player:

    def __init__(self, xlocation, ylocation, xvel, yvel, is_left, gravity, score):
        self.xlocation = xlocation
        self.ylocation = ylocation
        self.xvel = xvel
        self.yvel = yvel
        self.is_left = is_left
        self.gravity = gravity
        self.score = score

class Enemy:
     def __init__(self, xlocation,ylocation, xvel):
          self.xlocation = xlocation
          self.ylocation = ylocation
          self.xvel = xvel        


is_main_menu = True
is_game = False
is_over = False
main_menu = None
play_button = None
play_button_rect = None
high_score = 0
is_left = None
is_right = None

#paths to files
AUDIO_PATH = 'C:\\Users\\Brian\\Desktop\\reaper_run\\audio'
IMAGE_PATH = 'C:\\Users\\Brian\\Desktop\\reaper_run\\images'
FONT_PATH = 'C:\\Users\\Brian\\Desktop\\reaper_run\\fonts'



pygame.init()
#load audio
jump1 = pygame.mixer.Sound(os.path.join(AUDIO_PATH, 'jump1.mp3'))
jump1.set_volume(0.5)

hit1 = pygame.mixer.Sound(os.path.join(AUDIO_PATH, 'hit1.mp3'))
hit1.set_volume(0.7)

point = pygame.mixer.Sound(os.path.join(AUDIO_PATH, 'point.mp3'))
point.set_volume(0.7)

click = pygame.mixer.Sound(os.path.join(AUDIO_PATH, 'click.mp3'))
click.set_volume(1)
#score font
sf = pygame.font.Font('spiderman.ttf', 100)



def create_main_menu():
    
    global main_menu, play_button, play_button_rect, quit_button, quit_button_rect, is_game, high_score
    is_game = False
    pygame.mixer.music.load(os.path.join(AUDIO_PATH, 'pausemusic1.mp3'))
    pygame.mixer.music.set_volume(1)    
    pygame.mixer.music.play()
    main_menu = pygame.image.load(os.path.join(IMAGE_PATH, 'menu_background.jpg')).convert_alpha()
    play_button = pygame.image.load(os.path.join(IMAGE_PATH,'play_button.jpg')).convert_alpha()
    quit_button = pygame.image.load(os.path.join(IMAGE_PATH, 'quit_text.jpg'))


    play_button_rect = play_button.get_rect(topleft =(650, 400))
    quit_button_rect = quit_button.get_rect(topleft = (650, 600))

   

    screen.blit(main_menu, (0, 0))
    screen.blit(play_button,(play_button_rect))
    screen.blit(quit_button, (quit_button_rect))
  

         
    # pygame.draw.rect(screen, 'Red', button1)
    pass

def create_game():
        global p1, e1, sf, is_game, is_main_menu, enemy1, high_score, hit1, point, click, p_surface, p1_rect, is_left, is_right

        #highschore alogrithm
        if high_score <= player1.score:
             high_score = player1.score
      
                #movmenet player
        player1.gravity+=1
        p1_rect.x+=player1.xvel
        p1_rect.bottom+=player1.gravity

                #player collision with window
        if p1_rect.bottom >= WINDOW_HEIGHT:
            p1_rect.bottom = 1080
          
            screen.blit(p_surface, p1_rect)
        if p1_rect.bottom < 1081:
             animation()   
            
            
            
        if p1_rect.left <=0:
                p1_rect.left = 0
        if p1_rect.right >= WINDOW_WIDTH:
                p1_rect.right = WINDOW_WIDTH

            
        #movement enemy1
        e1_rect.x+=enemy1.xvel
        enemy_animation()

        #enemy player collision
        if p1_rect.colliderect(e1_rect):
              hit1.play()
              player1.score = 0
              p1_rect.x = 100
              p1_rect.y = WINDOW_HEIGHT - 400
              #default speed
              enemy1.xvel = -6
              e1_rect.x = WINDOW_WIDTH
              is_game = False
                         
              is_main_menu = True
        #enemy respawn
        if e1_rect.left <= 0:
             e1_rect.x = WINDOW_WIDTH
             player1.score+=1
             point.play()
          #ememy speed increase
        if player1.score >= 2:
             enemy1.xvel = -10
        if player1.score >= 4:
             p1_rect.x = 200

        if player1.score >= 6:
             enemy1.xvel = -12

        if player1.score >= 8:
             enemy1.xvel = -14
             p1_rect.x = 300
        
        if player1.score >= 10:
             enemy1.xvel = -16
        if player1.score >= 12:
             enemy1.xvel = -18
             p1_rect.x = 400
        if player1.score >= 14:
             enemy1.xvel = -20
        if player1.score >= 16:
            enemy1.xvel = -22
        if player1.score >= 18:
            enemy1.xvel = -24
            p1_rect.x = 500
        if player1.score >= 20:
            p1_rect.x = 600
            enemy1.xvel = -26
        if player1.score >=22:
             enemy1.xvel = -28
        if player1.score >=24:
             enemy1.xvel = -30
        if player1.score >=26:
             enemy1.xvel = -32
        if player1.score >=28:
             enemy1.xvel = -34
        if player1.score >=30:
             enemy1.xvel = -36






        #refresh screen
        screen.fill('Black')
        screen.blit(background, (0, 0))
                    



            #score
        score_font = sf.render(f'Score: {player1.score}', None, 'Black')
        high_score_font = sf.render(f'High Score: {high_score}', None, 'Red')

        screen.blit(score_font, (WINDOW_WIDTH / 2 - 300, 100))
        screen.blit(high_score_font, (WINDOW_WIDTH / 2 - 300, 0))



        screen.blit(p_surface, (p1_rect))
        screen.blit(e_surface, (e1_rect))

#window dimensions
WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080
WINDOW_TITLE = 'Spider Run'
is_running = False


#clock controls FPS
clock = pygame.time.Clock()


screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption(WINDOW_TITLE)




#player1
player1 = Player(100, WINDOW_HEIGHT - 200, 6, 3, True, 0, 0)




p_walk2 = pygame.image.load(os.path.join(IMAGE_PATH, 'player2.png')).convert_alpha()
p_walk3 = pygame.image.load(os.path.join(IMAGE_PATH, 'player3.png')).convert_alpha()
p_walk4 = pygame.image.load(os.path.join(IMAGE_PATH, 'player4.png')).convert_alpha()
p_walk5 = pygame.image.load(os.path.join(IMAGE_PATH, 'player5.png')).convert_alpha()
p_walk6 = pygame.image.load(os.path.join(IMAGE_PATH, 'player6.png')).convert_alpha()

p_walk = [p_walk2, p_walk3, p_walk4, p_walk5, p_walk6]

p_jump = pygame.image.load(os.path.join(IMAGE_PATH, 'jump.png')).convert_alpha()
player_index = 0


p_surface = p_walk[player_index]

p1_rect =p_surface.get_rect(center=(player1.xlocation, player1.ylocation))




           
    
def animation():
    
     global p_surface, p_jump, p1_rect, is_left, is_right, player_index
     
     if p1_rect.bottom < 1080:
          p_surface = p_jump
          if not player1.is_left:
               player1.is_left = True
          
     
     else:
          player_index+=0.1
          if player_index >=5: player_index = 0
          p_surface = p_walk[int(player_index)]

          # p_surface = p_surface = p_walk[player_index]
          if not player1.is_left:
               p_surface = pygame.transform.flip(p_surface, True, False)


def enemy_animation():
      global e_index, e_surface, e_walk

      if e1_rect.bottom >= WINDOW_HEIGHT:
           print('worked')

           e_index+=0.1
           if e_index >=3:
                e_index = 0
           e_surface = e_walk[int(e_index)]

#ENEMY 1
enemy1 = Enemy(1920, WINDOW_HEIGHT, -6)


e1 = pygame.image.load(os.path.join(IMAGE_PATH, 'ghost1.png')).convert_alpha()
e2 = pygame.image.load(os.path.join(IMAGE_PATH, 'ghost2.png')).convert_alpha()
e3 = pygame.image.load(os.path.join(IMAGE_PATH, 'ghost3.png')).convert_alpha()
e_index = 0
e_walk = [e1, e2, e3]
e_surface = e_walk[e_index]

e1_rect =e_surface.get_rect(midbottom=(enemy1.xlocation, enemy1.ylocation))




#images
background = pygame.image.load(os.path.join(IMAGE_PATH, 'background.jpg')).convert_alpha()


def start():
    global p1_rect, p_walk1, is_main_menu, is_game, is_over, main_menu, play_button, play_button_rect, qui, e1, e1_rect, click, p_surface, p_walk
    is_running = True

    while is_running:
            
           
            

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
                    sys.exit(0)
                    break
       
                if event.type == pygame.KEYDOWN:

                  if event.key == pygame.K_a:
                        

                    player1.xvel = 6
                    player1.xvel*=-1

                    if player1.is_left:
                        p_surface = pygame.transform.flip(p_surface, True, False)
                        player1.is_left = False


                  if event.key == pygame.K_d:
                        

                        player1.xvel = -6
                        player1.xvel*=-1

                        if not player1.is_left:
                            p_surface = pygame.transform.flip(p_surface, True, False)
                            player1.is_left = True

                  if event.key == pygame.K_SPACE:
                        if p1_rect.bottom == WINDOW_HEIGHT:
                    
                            player1.gravity = - 27
                            player1.is_left = False
                            

                            
                            
                            
                         
                            jump1.play()
                           

                            
                            


                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:

                        player1.xvel= 0


                    if event.key == pygame.K_d:

                        player1.xvel= 0
                    if event.key == pygame.K_ESCAPE:

                         if is_game:
                              is_game = False
                              is_main_menu = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                     if play_button_rect.collidepoint(pygame.mouse.get_pos()):
                          click.play()     
                          pygame.mixer.music.unload()
                          pygame.mixer.music.load(os.path.join(AUDIO_PATH, 'gamemusic1.mp3'))
                          pygame.mixer.music.set_volume(1)
                          pygame.mixer.music.play()

                          is_game = True



                     if quit_button_rect.collidepoint(pygame.mouse.get_pos()):
                          
                          is_running = False
     
                          
                #if the game state is ON GAME THEN DRAW EVERYTHING
            if is_game:
                
                    create_game()

                
            
            elif  is_main_menu:
                   is_main_menu = False
                   if not is_main_menu:
                    create_main_menu()
                    

                
            pygame.display.update()
            clock.tick(60)

   



start()



