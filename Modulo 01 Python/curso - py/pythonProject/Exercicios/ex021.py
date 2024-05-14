import pygame

def play_music(file_path):
    # Inicializa o módulo mixer do pygame
    pygame.mixer.init()

    # Carrega a música
    pygame.mixer.music.load(file_path)

    # Toca a música
    pygame.mixer.music.play()

    # Espera a música terminar de tocar
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

if __name__ == "__main__":
    # Use o caminho absoluto para o arquivo MP3
    mp3_path = 'C:\\Users\\thoma\\OneDrive\\Documentos\\Estudo\\curso - py\\pythonProject\\Exercicios\\ex021.mp3'
    play_music(mp3_path)
