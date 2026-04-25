import pygame
import math
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    current_color = (255, 0, 0) 
    mode = 'pen' 
    
    shapes = [] 
    drawing = False
    start_pos = None
    last_pos = None 

    while True:
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_r: current_color = (255, 0, 0)
                if event.key == pygame.K_g: current_color = (0, 255, 0)
                if event.key == pygame.K_b: current_color = (0, 0, 255)
                if event.key == pygame.K_w: current_color = (255, 255, 255)
                
                
                if event.key == pygame.K_1: mode = 'pen'
                if event.key == pygame.K_2: mode = 'rect'
                if event.key == pygame.K_3: mode = 'circle'
                if event.key == pygame.K_4: mode = 'eraser'

            if event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True
                start_pos = event.pos
                last_pos = event.pos 

            if event.type == pygame.MOUSEBUTTONUP:
                
                if drawing and mode in ['rect', 'circle']:
                    shapes.append((mode, current_color, start_pos, event.pos, 2))
                drawing = False

            if event.type == pygame.MOUSEMOTION and drawing:
                if mode == 'pen' or mode == 'eraser':
                    
                    color = (0, 0, 0) if mode == 'eraser' else current_color
                    thick = 20 if mode == 'eraser' else 2
                    shapes.append(('line', color, last_pos, event.pos, thick))
                    last_pos = event.pos 

        screen.fill((0, 0, 0))
        
        
        for s_type, color, start, end, thick in shapes:
            draw_shape(screen, s_type, color, start, end, thick)

        
        if drawing and mode in ['rect', 'circle']:
            draw_shape(screen, mode, current_color, start_pos, mouse_pos, 1)

        pygame.display.flip()
        clock.tick(60)

def draw_shape(surface, s_type, color, start, end, thickness):
    x1, y1 = start
    x2, y2 = end

    if s_type == 'rect':
        rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2-x1), abs(y2-y1))
        pygame.draw.rect(surface, color, rect, thickness)
    elif s_type == 'circle':
        radius = int(math.sqrt((x2 - x1)**2 + (y2 - y1)**2))
        pygame.draw.circle(surface, color, start, radius, thickness)
    elif s_type == 'line':
        pygame.draw.line(surface, color, start, end, thickness)

main()