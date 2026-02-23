import pygame
import sys

pygame.init()

window = pygame.display.set_mode((500, 300))
pygame.display.set_caption("Temperature Converter")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
FONT = pygame.font.SysFont(None, 32)

input_box = pygame.Rect(50, 50, 140, 32)
convert_button = pygame.Rect(300, 50, 100, 32)
ftoc_button = pygame.Rect(50, 100, 200, 32)
ctof_button = pygame.Rect(50, 140, 200, 32)

active_input = False
temperature_text = ""
conversion = "FtoC"
result_text = ""

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos):
                active_input = True
            else:
                active_input = False
            if ftoc_button.collidepoint(event.pos):
                conversion = "FtoC"
            if ctof_button.collidepoint(event.pos):
                conversion = "CtoF"
            if convert_button.collidepoint(event.pos):
                try:
                    t = float(temperature_text)
                    if conversion == "FtoC":
                        result_text = f"{t}°F = {(t-32)/(9/5):.2f}°C"
                    else:
                        result_text = f"{t}°C = {t*9/5+32:.2f}°F"
                except:
                    result_text = "Ingresa un número válido"
        if event.type == pygame.KEYDOWN and active_input:
            if event.key == pygame.K_BACKSPACE:
                temperature_text = temperature_text[:-1]
            elif event.key == pygame.K_RETURN:
                try:
                    t = float(temperature_text)
                    if conversion == "FtoC":
                        result_text = f"{t}°F = {(t-32)/(9/5):.2f}°C"
                    else:
                        result_text = f"{t}°C = {t*9/5+32:.2f}°F"
                except:
                    result_text = "Ingresa un número válido"
            else:
                temperature_text += event.unicode

    window.fill(WHITE)

    pygame.draw.rect(window, BLACK, input_box, 2)
    txt_surface = FONT.render(temperature_text, True, BLACK)
    window.blit(txt_surface, (input_box.x+5, input_box.y+5))

    pygame.draw.rect(window, BLACK if conversion=="FtoC" else BLUE, ftoc_button)
    ftoc_text = FONT.render("Fahrenheit a Celsius", True, WHITE)
    window.blit(ftoc_text, (ftoc_button.x+5, ftoc_button.y+5))

    pygame.draw.rect(window, BLACK if conversion=="CtoF" else BLUE, ctof_button)
    ctof_text = FONT.render("Celsius a Fahrenheit", True, WHITE)
    window.blit(ctof_text, (ctof_button.x+5, ctof_button.y+5))

    pygame.draw.rect(window, BLACK, convert_button)
    convert_text = FONT.render("Convertir", True, WHITE)
    window.blit(convert_text, (convert_button.x+5, convert_button.y+5))

    result_surface = FONT.render(result_text, True, BLUE)
    window.blit(result_surface, (50, 200))

    pygame.display.flip()
    