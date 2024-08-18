# Importando Libraries
import pygame
import sys
import subprocess
import os 

# Inicializando Pygame
pygame.init()

# Dimensões de Tela
largura = 800
altura = 600

# Cores do Menu
BRANCO = (255, 255, 255)
AMARELO = (255, 255, 0)

# Fontes
pygame.font.init()
font = pygame.font.Font(None, 74)

# Superfície do Display
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Inimigos da Raiva")

# Carregando Imagem de Fundo
bg_image = pygame.image.load(os.path.join("assets", "bg_menu.jpeg"))
bg_image = pygame.transform.scale(bg_image, (largura, altura))

# Carregando efeitos sonoros
select = pygame.mixer.Sound(os.path.join("SFX", "Menu_Navigate_00.mp3"))


# Menu
opcoes = ["[JOGAR]", "[CONTROLES]", "[SAIR]"]

def menu():
    opcao_selec = 0
    pygame.mixer.music.load(os.path.join("SFX", "Loop_Someday_00.mp3"))
    pygame.mixer.music.play()
    while True:
        # Desenha imagem de fundo
        tela.blit(bg_image, (0, 0))

        # Desenha opções de menu
        for i, opcao in enumerate(opcoes):
            if i == opcao_selec:
                color = AMARELO
            else:
                color = BRANCO

            text = font.render(opcao, True, color)
            text_rect = text.get_rect(center=(largura // 2, 150 + i * 100))
            tela.blit(text, text_rect)

        pygame.display.flip()  # Update do display

        # Eventos
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                select.play()
                if event.key == pygame.K_DOWN:
                    opcao_selec = (opcao_selec + 1) % len(opcoes)
                elif event.key == pygame.K_UP:
                    opcao_selec = (opcao_selec - 1) % len(opcoes)
                elif event.key == pygame.K_RETURN:
                    if opcao_selec == 0:
                        print("JOGAR")
                        pygame.quit()
                        subprocess.run(["python", "py_jogoPrincipal.py"])
                        sys.exit()
                    elif opcao_selec == 1:
                        print("CONTROLES")
                        # Opções
                    elif opcao_selec == 2:
                        pygame.quit()
                        sys.exit()

if __name__ == "__main__":
    menu()
