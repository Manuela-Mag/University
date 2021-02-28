import pygame


class button:
    # colours for button and text
    button_col = (255, 0, 0)
    hover_col = (75, 225, 255)
    click_col = (50, 150, 255)
    text_col = (0, 0, 0)
    width = 180
    height = 70

    # define colours
    bg = (204, 102, 0)
    red = (255, 0, 0)
    black = (0, 0, 0)
    white = (255, 255, 255)

    def __init__(self, x, y, text, screen, font):
        self.x = x
        self.y = y
        self.text = text
        self.screen = screen
        self.font = font

    def draw_button(self):

        global clicked
        action = False

        # get mouse position
        pos = pygame.mouse.get_pos()

        # create pygame Rect object for the button
        button_rect = pygame.Rect(self.x, self.y, self.width, self.height)

        # check mouseover and clicked conditions
        if button_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                clicked = True
                pygame.draw.rect(self.screen, self.click_col, button_rect)
            elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
                clicked = False
                action = True
            else:
                pygame.draw.rect(self.screen, self.hover_col, button_rect)
        else:
            pygame.draw.rect(self.screen, self.button_col, button_rect)

        # add shading to button
        pygame.draw.line(self.screen, self.white, (self.x, self.y), (self.x + self.width, self.y), 2)
        pygame.draw.line(self.screen, self.white, (self.x, self.y), (self.x, self.y + self.height), 2)
        pygame.draw.line(self.screen, self.black, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
        pygame.draw.line(self.screen, self.black, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)

        # add text to button
        text_img = self.font.render(self.text, True, self.text_col)
        text_len = text_img.get_width()
        self.screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 25))
        return action