import pygame
import element
import time
SZEROKOSC_EKRANU = 800
WYSOKOSC_EKRANU = 600

obraz_tla = pygame.image.load('images/background.png')
obraz_bazy_postaci =  pygame.image.load('images/base.png')

pygame.init()

ekran = pygame.display.set_mode([SZEROKOSC_EKRANU, WYSOKOSC_EKRANU])
zegar = pygame.time.Clock()

moja_czcionka = pygame.font.SysFont('Comic Sans MS', 30)

def wypisz_tekst(ekran, tekst, pozycja):
    napis = moja_czcionka.render(tekst, False, (255, 255, 255))
    ekran.blit(napis, pozycja)

nakrycie_glowy = element.NakrycieGlowy()
ubranie_element = element.UbranieElement()
oczy_element = element.OczyElement()
bron_element = element.BronElement()

gra_dziala = True
zapisywanie = False
while gra_dziala:
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.KEYDOWN:
            if zdarzenie.key == pygame.K_ESCAPE:
                gra_dziala = False
            if zdarzenie.key == pygame.K_q:
                nakrycie_glowy.wybierzNastepny()
            if zdarzenie.key == pygame.K_w:
                oczy_element.wybierzNastepny()
            if zdarzenie.key == pygame.K_e:
                ubranie_element.wybierzNastepny()
            if zdarzenie.key == pygame.K_r:
                bron_element.wybierzNastepny()
            if zdarzenie.key == pygame.K_s:
                zapisywanie = True
        elif zdarzenie.type == pygame.QUIT:
            gra_dziala = False

    ekran.blit(obraz_tla, (0,0))
    ekran.blit(obraz_bazy_postaci, (270,130))
    ekran.blit(nakrycie_glowy.wybranyObraz(), (270, 130))
    ekran.blit(ubranie_element.wybranyObraz(), (270, 130))
    ekran.blit(oczy_element.wybranyObraz(), (270, 130))
    ekran.blit(bron_element.wybranyObraz(), (270, 130))


    if zapisywanie:
        timestamp = time.strftime('%Y%m%d%H%M%S')
        pygame.image.save(ekran, f'postac{timestamp}.png')
        zapisywanie = False

    wypisz_tekst(ekran, f'[Q] Glowa{nakrycie_glowy.wybrany}', (100, 100))
    wypisz_tekst(ekran, f'[W] Oczy{oczy_element.wybrany}', (100, 140))
    wypisz_tekst(ekran, f'[E] Ubranie{ubranie_element.wybrany}', (100, 180))
    wypisz_tekst(ekran, f'[R] Bron{bron_element.wybrany}', (100, 220))
    wypisz_tekst(ekran, f'[S] Zapisz', (100, 260))
    pygame.display.flip()
    zegar.tick(30)

pygame.quit()



