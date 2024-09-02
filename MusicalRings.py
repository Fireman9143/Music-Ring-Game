import pygame, sys
from musicnotes import frequencies, notes
"""Develop a simple 2D interface with keyboard control.
Graphic will consist of 5 nonintersecting circles that can be color filled.
Each circle will be assigned a musical note whose pitch and duration can be 
selected by the user, a keyboard key to control it (these can be any 5 contiguous 
keys, such as ASDFG), and a starting color.  When the user presses a key, 
the color of the corresponding ball changes to the next color in the sequence 
(colors to include Red, Blue Yellow, Green, Orange and Purple) and plays the 
corresponding note."""
class RingGame:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.game_active = True
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1200, 800))
        self.bg_color = (0, 0, 0)
        pygame.display.set_caption('Musical Rings')
        self.BPM = 60
        self.ring_color = [(255, 255, 255), (255, 0, 0), (0, 0, 255), (255, 255, 0), (0, 255, 0), (255, 126, 19), (148, 0, 211)]
        self.ring_pressed = {1:0, 2:0, 3:0, 4:0, 5:0}
        self.rings = []
        self.notes = []
        
    def run(self):
        while self.game_active == True:
            self.check_events()
            self.update_screen()
            self.clock.tick(60)
        
    def check_events(self):
        """Checks for exit or for key presses.  Plays note on key press."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                pygame.mixer.quit()
                sys.exit()    
            elif event.type == pygame.KEYDOWN:
                self.check_keydown(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.check_collision(event)
            elif event.type == pygame.MOUSEBUTTONUP:
                self.assign_value(event)

    def check_keydown(self, event):
            if event.key == pygame.K_a:
                pygame.mixer.Sound(frequencies['A4']).play(loops=0, maxtime=notes['1/16'])
                if self.ring_pressed[1] <= 5:self.ring_pressed[1] += 1
            elif event.key == pygame.K_s:
                pygame.mixer.Sound(frequencies['C#4']).play(loops=0, maxtime=notes['1/8'])
                if self.ring_pressed[2] <= 5:self.ring_pressed[2] += 1
            elif event.key == pygame.K_d:
                pygame.mixer.Sound(frequencies['E4']).play(loops=0, maxtime=notes['1/4'])
                if self.ring_pressed[3] <= 5:self.ring_pressed[3] += 1
            elif event.key == pygame.K_f:
                pygame.mixer.Sound(frequencies['F#4']).play(loops=0, maxtime=notes['1/2'])
                if self.ring_pressed[4] <= 5:self.ring_pressed[4] += 1
            elif event.key == pygame.K_g:
                pygame.mixer.Sound(frequencies['B4']).play(loops=0, maxtime=notes['1/1'])
                if self.ring_pressed[5] <= 5:self.ring_pressed[5] += 1

    def check_collision(self, event):
        for box in self.notes:
            if box.collidepoint(pygame.mouse.get_pos()):
                box.center = pygame.mouse.get_pos()
            #check which box is clicked
            #assign box surf center to mouse.pos to drag and drop

    def assign_value(self, event):
        for note in self.notes:
            if note.collidepoint(ring for ring in self.rings):
                print(f'{note} assigned to {note.collidepoint}')
            else: None
            #check whick ring the note box is on and assign ring that value
            #ring value = note value

    def update_screen(self):
        """Fills background, draws rings, updates display"""
        self.screen.fill(self.bg_color)
        self.input_boxes()
        self.make_rings()
        pygame.display.flip()

    def make_rings(self):
        """Draws six colored circles evenly spaced on screen"""
        self.circle1 = pygame.draw.circle(self.screen, 
                           color = self.ring_color[self.ring_pressed[1]], 
                           center = ((self.screen.get_width()/6),(self.screen.get_height()/2)), 
                           radius = 100)#red
        self.rings.append(self.circle1)
        self.circle2 = pygame.draw.circle(self.screen, 
                            color = self.ring_color[self.ring_pressed[2]],
                            center = ((self.screen.get_width()/6)*2,(self.screen.get_height()/2)), 
                            radius = 100)#blue
        
        self.circle3 = pygame.draw.circle(self.screen, 
                            color = self.ring_color[self.ring_pressed[3]], 
                            center = ((self.screen.get_width()/6)*3,(self.screen.get_height()/2)), 
                            radius = 100)#yellow
        self.circle4 = pygame.draw.circle(self.screen, 
                            color = self.ring_color[self.ring_pressed[4]],
                            center = ((self.screen.get_width()/6)*4,(self.screen.get_height()/2)), 
                            radius = 100)#green
        self.circle5 = pygame.draw.circle(self.screen, 
                            color = self.ring_color[self.ring_pressed[5]], 
                            center = ((self.screen.get_width()/6)*5,(self.screen.get_height()/2)), 
                            radius = 100)#orange
        
    def input_boxes(self):
        font = pygame.font.SysFont('Arial', 80)
        
        box1 = pygame.draw.rect(self.screen, (100, 100, 100), ((self.screen.get_width()/13) - 5, 100, 80, 100))
        if box1 not in self.notes:self.notes.append(box1)
        a_surf = font.render('A', True, ('red'))
        self.screen.blit(a_surf, box1)

        box2  =pygame.draw.rect(self.screen, (100, 100, 100), (((self.screen.get_width()/13) - 5)*2, 100, 80, 100))
        if box2 not in self.notes:self.notes.append(box2)
        as_surf = font.render('A#', True, (240, 93, 14))
        self.screen.blit(as_surf, box2)

        box3 = pygame.draw.rect(self.screen, (100, 100, 100), (((self.screen.get_width()/13) - 5)*3, 100, 80, 100))
        if box3 not in self.notes:self.notes.append(box3)
        b_surf = font.render('B', True, ('orange'))
        self.screen.blit(b_surf, box3)

        box4 = pygame.draw.rect(self.screen, (100, 100, 100), (((self.screen.get_width()/13) - 5)*4, 100, 80, 100))
        if box4 not in self.notes:self.notes.append(box4)
        c_surf = font.render('C', True, (240, 168, 14))
        self.screen.blit(c_surf, box4)

        box5 = pygame.draw.rect(self.screen, (100, 100, 100), (((self.screen.get_width()/13) - 5)*5, 100, 80, 100))
        if box5 not in self.notes:self.notes.append(box5)
        cs_surf = font.render('C#', True, ('yellow'))
        self.screen.blit(cs_surf, box5)

        box6 = pygame.draw.rect(self.screen, (100, 100, 100), (((self.screen.get_width()/13) - 5)*6, 100, 80, 100))
        if box6 not in self.notes:self.notes.append(box6)
        d_surf = font.render('D', True, ('yellow green'))
        self.screen.blit(d_surf, box6)

        box7 = pygame.draw.rect(self.screen, (100, 100, 100), (((self.screen.get_width()/13) - 5)*7, 100, 80, 100))
        if box7 not in self.notes:self.notes.append(box7)
        ds_surf = font.render('D#', True, ('green'))
        self.screen.blit(ds_surf, box7)

        box8 = pygame.draw.rect(self.screen, (100, 100, 100), (((self.screen.get_width()/13) - 5)*8, 100, 80, 100))
        if box8 not in self.notes:self.notes.append(box8)
        e_surf = font.render('E', True, (14, 241, 76))
        self.screen.blit(e_surf, box8)

        box9 = pygame.draw.rect(self.screen, (100, 100, 100), (((self.screen.get_width()/13) - 5)*9, 100, 80, 100))
        if box9 not in self.notes:self.notes.append(box9)
        f_surf = font.render('F', True, ('blue'))
        self.screen.blit(f_surf, box9)

        box10 = pygame.draw.rect(self.screen, (100, 100, 100), (((self.screen.get_width()/13) - 5)*10, 100, 80, 100))
        if box10 not in self.notes:self.notes.append(box10)
        fs_surf = font.render('F#', True, ('indigo'))
        self.screen.blit(fs_surf, box10)

        box11 = pygame.draw.rect(self.screen, (100, 100, 100), (((self.screen.get_width()/13) - 5)*11, 100, 80, 100))
        if box11 not in self.notes:self.notes.append(box11)
        g_surf = font.render('G', True, ('violet'))
        self.screen.blit(g_surf, box11)

        box12 = pygame.draw.rect(self.screen, (100, 100, 100), (((self.screen.get_width()/13) - 5)*12, 100, 80, 100))
        if box12 not in self.notes:self.notes.append(box12)
        gs_surf = font.render('G#', True, ('black'))
        self.screen.blit(gs_surf, box12)

if __name__ == "__main__":
    rings = RingGame()
    rings.run()