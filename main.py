# импорт библиотек
import random
import time

import pygame


class End_Screen(pygame.sprite.Sprite):#создание окна game over
    def __init__(self, sprite):
        super().__init__(sprite)
        self.image = pygame.image.load('end_screen.png')
        self.image = pygame.transform.scale(self.image, (1920, 1080))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, -1080

    def update(self):# анимация движения окна
        if self.rect.y != 0:
            self.rect.y += 12

    def proove(self): # проверка на расположение окна
        if self.rect.y == 0:
            return 1


class End_Buttons(pygame.sprite.Sprite):# создание кнопок restar и exit
    def __init__(self, sprite, id):
        super().__init__()
        self.id = id
        if id == 1:
            self.image = pygame.image.load('restart_button.png')
            self.image = pygame.transform.scale(self.image, (600, 500))
            self.rect = self.image.get_rect()
            self.rect.x, self.rect.y = 300, 550
        if id == 2:
            self.image = pygame.image.load('Back_button.png')
            self.image = pygame.transform.scale(self.image, (400, 250))
            self.rect = self.image.get_rect()
            self.rect.x, self.rect.y = 1100, 710
        self.add(sprite)

    def update(self, *args): #определение нажатие кнопки
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            if self.id == 1:
                return 1
            return 2


class Arrow(pygame.sprite.Sprite):# создание стрелку указывающая на колоду карт
    def __init__(self, sprite):
        super().__init__()
        self.image = pygame.image.load("ar.png")
        self.image = pygame.transform.scale(self.image, (350, 300))
        self.image = pygame.transform.flip(self.image, True, True)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 1250, 400
        self.add(sprite)
        self.mn = 2

    def update(self):# анимация движения кнопки
        self.rect.y += self.mn
        if self.rect.y == 426:
            self.mn = -2
        if self.rect.y == 400:
            self.mn = 2


class Board(pygame.sprite.Sprite):  # спрайт доски
    def __init__(self, sprite):
        super().__init__()
        self.image = pygame.image.load("board.png")
        self.image = pygame.transform.scale(self.image, (1448, 255))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 236, 750
        self.add(sprite)


class Buttons(pygame.sprite.Sprite):# создание кнопок при начале игры
    image_off = pygame.image.load("play_button_off.png")
    image_off = pygame.transform.scale(image_off, (500, 490))
    image = pygame.image.load("Button_play_on.png")

    def __init__(self, sprite, id):  # создание кнопок начального окна
        super().__init__()
        self.id = id
        if self.id == 1:  # Создание кнопки играть
            self.image = Buttons.image
            self.image = pygame.transform.scale(self.image, (500, 300))
            self.rect = self.image.get_rect()
            self.rect.x, self.rect.y = 700, 500
        if self.id == 2:  # создание кнопки выход
            self.image = pygame.image.load("Back_button.png")
            self.image = pygame.transform.scale(self.image, (400, 300))
            self.rect = self.image.get_rect()
            self.rect.x, self.rect.y = 750, 750
        self.add(sprite)

    def update(self, *args):  # отображение нажатии кнопки
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            if self.id == 1:
                self.image = Buttons.image_off
                return 1
        return 2


class Pig(pygame.sprite.Sprite):  # создание свиньи
    def __init__(self, sprite):
        super().__init__()
        self.image = pygame.image.load("pig.png")
        self.image = pygame.transform.scale(self.image, (1448, 1080))
        self.rect = self.image.get_rect()
        self.rect.x = 236
        self.add(sprite)

    def change_emojy(self, emojy):# изменение спрайтов свина
        if emojy == 'give card':
            self.image = pygame.image.load("give_card_to_player.png")
            self.image = pygame.transform.scale(self.image, (1448, 1080))
            flip(False)
        elif emojy == 'usual':
            self.image = pygame.image.load('pig.png')
            self.image = pygame.transform.scale(self.image, (1448, 1080))
            flip(False)
        elif emojy == 'see card':
            self.image = pygame.image.load('give_card_to_pig.png')
            self.image = pygame.transform.scale(self.image, (1448, 1080))
            flip(False)
        elif emojy == 'take card':
            self.image = pygame.image.load('pig_take_card.png')
            self.image = pygame.transform.scale(self.image, (1448, 1080))
            flip(False)
        elif emojy == 'take_card_pig':
            self.image = pygame.image.load('not_happy_pig_take_card.png')
            self.image = pygame.transform.scale(self.image, (1448, 1080))
            flip(False)


class Deck_Of_Card(pygame.sprite.Sprite):  # содание колоды карт
    def __init__(self, sprite):
        super().__init__()
        self.image = pygame.image.load("deck_of_cards.png")
        self.image = pygame.transform.scale(self.image, (200, 100))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 1350, 650
        self.add(sprite)


def flip(q): # смена кадра
    pygame.display.flip()
    all_sprites.draw(screen)
    if not q:
        pygame.draw.rect(screen, (0, 0, 0), rect_of_font)
        screen.blit(text, text.get_rect(center=rect_of_font.center))
    pygame.display.flip()
    time.sleep(0.5)


def draw_the_cards():# рисовка карт
    cords = 300
    for card in player_cards:
        if card != 'J' and card != 'Q' and card != 'K' and card != 'T':
            for y in range(1, player_cards[card] + 1):
                rect_of_cards[int(card) - 2].x, rect_of_cards[int(card) - 2].y = cords, 800 - y * 10
                screen.blit(sprites_of_cards[int(card) - 2], rect_of_cards[int(card) - 2])
        elif card == 'J':
            for y in range(1, player_cards[card] + 1):
                rect_of_cards[9].x, rect_of_cards[9].y = cords, 800 - y * 10
                screen.blit(sprites_of_cards[9], (cords, 800 - y * 10))
        elif card == 'Q':
            for y in range(1, player_cards[card] + 1):
                rect_of_cards[10].x, rect_of_cards[10].y = cords, 800 - y * 10
                screen.blit(sprites_of_cards[10], (cords, 800 - y * 10))
        elif card == 'K':
            for y in range(1, player_cards[card] + 1):
                rect_of_cards[11].x, rect_of_cards[11].y = cords, 800 - y * 10
                screen.blit(sprites_of_cards[11], (cords, 800 - y * 10))
        else:
            for y in range(1, player_cards[card] + 1):
                rect_of_cards[12].x, rect_of_cards[12].y = cords, 800 - y * 10
                screen.blit(sprites_of_cards[12], (cords, 800 - y * 10))
        cords += 170


# иницилизация pygame
pygame.init()

#создание стрелки
ar_sp = pygame.sprite.Group()
arrow = Arrow(ar_sp)

# создание окна
clock = pygame.time.Clock()
size = wigth, height = 1920, 1020
screen = pygame.display.set_mode(size)

# создания счётчиков сундучков
count_player = 4
count_pig = 8

#создание текста для подсчёта количества сундучков
counts = pygame.font.Font(None, 45)
rect_of_counts1 = pygame.Rect(0, 100, 200, 100)
text_of_counts1 = counts.render("", True, (255, 255, 255), (0, 0, 0))
rect_of_counts2 = pygame.Rect(1700, 100, 200, 100)
text_of_counts2 = counts.render("", True, (255, 255, 255), (0, 0, 0))

# загрузка музыки
music = 'music_game.mp3'
pygame.mixer.music.load(music)
pygame.mixer.music.play()

# создание свиньи
running = True
all_sprites = pygame.sprite.Group()
pig = Pig(all_sprites)

# создание кнопок
all_buttons = pygame.sprite.Group()
play_button = Buttons(all_buttons, 1)
back_button = Buttons(all_sprites, 2)

# создание спрайта для мышки
mouse_on = pygame.image.load("arrow.png")
pygame.mouse.set_visible(False)

while running:  # стартовое окно
    screen.fill([0, 0, 0])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # выход из игры
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in all_buttons:
                if button.update(event) == 1:  # если нажали кнопку играть
                    running = False
                if button.update(event) == 2:  # если нажали кнопку выход
                    pygame.quit()

    all_sprites.draw(screen)  # рисовка свина
    all_buttons.draw(screen)  # рисовка кнопок
    screen.blit(mouse_on, pygame.mouse.get_pos())  # обновление позиции мышки
    pygame.display.flip()
    clock.tick(30)

running = False

all_cards = [str(i) for i in range(2, 11)] * 4 + [i for i in ['J', 'Q', 'K', 'T']] * 4
pig_cards = {}
player_cards = {}
for i in range(7):# распределение карт свину и игроку
    card = random.choice(all_cards)
    if card not in pig_cards:
        pig_cards[card] = 1
    elif card in pig_cards:
        pig_cards[card] += 1
    all_cards.remove(card)
    card = random.choice(all_cards)
    if card not in player_cards:
        player_cards[card] = 1
    elif card in player_cards:
        player_cards[card] += 1
    all_cards.remove(card)

board = Board(all_sprites) # загрузка спрайтов карт
two_cards = pygame.image.load("2_card.png")
three_cards = pygame.image.load("3_card.png")
four_cards = pygame.image.load("4_card.png")
five_cards = pygame.image.load("5_card.png")
six_cards = pygame.image.load("6_card.png")
seven_cards = pygame.image.load("7_card.png")
eight_cards = pygame.image.load("8_card.png")
nine_cards = pygame.image.load("9_card.png")
ten_cards = pygame.image.load("10_card.png")
J_cards = pygame.image.load("J_card.png")
Q_cards = pygame.image.load("Q_card.png")
K_cards = pygame.image.load("K_card.png")
T_cards = pygame.image.load("TUZ_card.png")
rect_of_cards = [two_cards.get_rect(), three_cards.get_rect(), four_cards.get_rect(), five_cards.get_rect(),
                 six_cards.get_rect(), seven_cards.get_rect(), eight_cards.get_rect(), nine_cards.get_rect(),
                 ten_cards.get_rect(), J_cards.get_rect(), Q_cards.get_rect(), K_cards.get_rect(), T_cards.get_rect()]

sprites_of_cards = [two_cards, three_cards, four_cards, five_cards, six_cards, seven_cards, eight_cards, nine_cards,
                    ten_cards, J_cards, Q_cards, K_cards, T_cards]

text_of_cards = [str(i) for i in range(2, 11)] + ['J', 'Q', 'K', 'T']
deck_of_card = Deck_Of_Card(all_sprites)
check_pig_card = False

font = pygame.font.Font(None, 90)

rect_of_font = pygame.Rect(236, 755, 1448, 250)

text = font.render("", True, (255, 255, 255), (0, 0, 0))

take_the_card = False

taken_card = False

turn = True

while True:
    while running:
        screen.fill([0, 0, 0])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if not take_the_card: # если наш ход
                    for card in range(len(sprites_of_cards)):
                        if rect_of_cards[card].collidepoint(pos) and turn:
                            check_pig_card = True
                            c = 0
                            text = font.render(f"У вас есть {text_of_cards[card]}?", True, (255, 255, 255), (0, 0, 0))
                            flip(False)
                            time.sleep(1)
                            current_card = text_of_cards[card]
                else: # если не угадали карту
                    if deck_of_card.rect.collidepoint(pos) and not taken_card:
                        new_card = random.choice(all_cards)
                        if len(player_cards) == 8 and any(True for i in all_cards if i in player_cards):
                            while new_card not in player_cards:
                                new_card = random.choice(all_cards)
                            all_cards.remove(new_card)
                        if not any(True for i in all_cards if i in player_cards):
                            running = False
                        if new_card in player_cards:
                            player_cards[new_card] += 1
                        else:
                            player_cards[new_card] = 1
                        take_the_card = False
                        taken_card = True
                        flip(True)
                        draw_the_cards()
                        pygame.display.flip()
                        time.sleep(1)

        all_sprites.draw(screen)
        draw_the_cards()

        if check_pig_card and turn:# проверка наличия карты у свина, замена спрайтов свина, условие что сейчас ход игрока
            pygame.draw.rect(screen, (0, 0, 0), rect_of_font)
            screen.blit(text, text.get_rect(center=rect_of_font.center))
            flip(False)
            if c == 0:
                c += 1
            if current_card in pig_cards:
                pig.change_emojy('give card')
                time.sleep(1)
                pig.change_emojy('usual')
                c = 2
                if current_card in player_cards:
                    player_cards[current_card] += pig_cards[current_card]
                for card in player_cards:
                    if player_cards[card] >= 4:
                        player_cards.pop(card)
                        count_player += 1
                        break
            else:# если не угадали карту у свина, берём её из колоды(теперь можно брать карту из колоды)
                text = font.render('-Нет Сэр, берите карту.', True, (255, 255, 255), (0, 0, 0))
                flip(False)
                time.sleep(1)
                take_the_card = True
                turn = False
            check_pig_card = False

        if not turn and taken_card:# если сейчас ход свина и игрок взял карту из колоды
            cards = [i for i in pig_cards.keys()]
            card = random.choice(cards)
            text = font.render(f'-Cэр, у вас есть {card}?', True, (255, 255, 255), (0, 0, 0))
            flip(False)
            time.sleep(1)
            if card in player_cards:#если свин угадал карту
                pig.change_emojy('see card')
                flip(False)
                time.sleep(1)
                pig.change_emojy('take card')
                flip(False)
                time.sleep(1)
                pig_cards[card] += player_cards[card]
                player_cards.pop(card)
                pig.change_emojy('usual')
                flip(False)
                time.sleep(1)
            else:# если свин не угадал карту
                text = font.render(f'-Нет, берите карту, мистер свин', True, (255, 255, 255), (0, 0, 0))
                flip(False)
                time.sleep(1)
                pig.change_emojy('take_card_pig')
                flip(False)
                time.sleep(1)
                pig.change_emojy('usual')
                flip(False)
                turn = True
                taken_card = False
                card = str(random.choice(all_cards))
                all_cards.remove(card)
                if card in pig_cards:
                    pig_cards[card] += 1
                else:
                    pig_cards[card] = 1
        # проверка 4 карт в колоде свина и игрока
        for card in pig_cards:
            if pig_cards[card] >= 4:
                pig_cards.pop(card)
                count_pig += 1
                break
        for card in player_cards:
            if player_cards[card] >= 4:
                player_cards.pop(card)
                count_player += 1
                break
        # если игрок должен взять карту, то стрелка указывает на колоду карт
        if take_the_card:
            ar_sp.draw(screen)
            arrow.update()
        # если у когото не осталось карт
        if (len(player_cards) == 0 and all_cards == 0) or (len(pig_cards) == 0 and all_cards == 0):
            running = False
        # рисовка изображение: счёткик сундуков у свина и игрока, мыши
        text_of_counts1 = font.render(f'ВЫ:{count_player}', True, (255, 255, 255), (0, 0, 0))
        text_of_counts2 = font.render(f'СВИН:{count_pig}', True, (255, 255, 255), (0, 0, 0))
        screen.blit(text_of_counts1, text_of_counts1.get_rect(center=rect_of_counts1.center))
        screen.blit(text_of_counts2, text_of_counts2.get_rect(center=rect_of_counts2.center))
        screen.blit(mouse_on, pygame.mouse.get_pos())
        pygame.display.flip()
        clock.tick(30)
    #создание конечного окна с сообщением о выигрыше и количесв сундучков игрока и свина
    end_sprite = pygame.sprite.Group()
    end = End_Screen(end_sprite)
    end_buttons = pygame.sprite.Group()
    restart_button = End_Buttons(end_buttons, 1)
    exit_button = End_Buttons(end_buttons, 2)
    font = pygame.font.Font(None, 50)
    text = font.render(
        f"Ваше количество сундучков: {count_player}                       Количесвто сундучков свина: {count_pig}",
        True,
        (255, 255, 255), (0, 0, 0))
    f = pygame.font.Font(None, 100)
    win_text = f.render("Вы выиграли!", True, (0, 255, 0), (0, 0, 0))
    win_rect = win_text.get_rect(center=(960, 630))
    text_rect = text.get_rect(center=(1000, 700))
    end_bool = True
    while end_bool:# конечное окно
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in end_buttons:
                    if button.update(event) == 1:# начало новой игры
                        end_bool = False
                        running = True
                    elif button.update(event) == 2:#выход из игры
                        pygame.quit()

        end_sprite.update()
        end_sprite.draw(screen)
        if end.proove() == 1:# проверка на выигрыш
            if count_pig > count_player:
                win_text = f.render("Свин выиграл!", True, (255, 0, 0), (0, 0, 0))
            elif count_player == count_pig:
                win_text = f.render("Ничья!", True, (0, 0, 255), (0, 0, 0))
                win_rect = win_text.get_rect(center=(950, 630))
                win_rect = win_text.get_rect(center=(950, 630))
            screen.blit(win_text, win_rect)
            end_buttons.draw(screen)
            screen.blit(text, text_rect)
        screen.blit(mouse_on, pygame.mouse.get_pos())
        pygame.display.flip()
        clock.tick(30)
