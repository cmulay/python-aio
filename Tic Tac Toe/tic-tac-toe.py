import pygame

pygame.init()

size = width, height = 550, 540

screen = pygame.display.set_mode(size)

pygame.display.set_caption("Tic Tac Toe")

# drawing on screen
zero = pygame.draw.rect(screen, (255, 255, 255), (20, 20, 150, 150))
first = pygame.draw.rect(screen, (255, 255, 255), (200, 20, 150, 150))
second = pygame.draw.rect(screen, (255, 255, 255), (380, 20, 150, 150))

third = pygame.draw.rect(screen, (255, 255, 255), (20, 190, 150, 150))
fourth = pygame.draw.rect(screen, (255, 255, 255), (200, 190, 150, 150))
fifth = pygame.draw.rect(screen, (255, 255, 255), (380, 190, 150, 150))

sixth = pygame.draw.rect(screen, (255, 255, 255), (20, 360, 150, 150))
seventh = pygame.draw.rect(screen, (255, 255, 255), (200, 360, 150, 150))
eighth = pygame.draw.rect(screen, (255, 255, 255), (380, 360, 150, 150))

running = True

# 0: red, 1: yellow, 2: idle / empty

gameState = [2, 2, 2, 2, 2, 2, 2, 2, 2]

winningPositions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

activePlayer = 0

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if zero.collidepoint(event.pos):
                if gameState[0] == 2:
                    gameState[0] = activePlayer

                    if activePlayer == 0:
                        pygame.draw.rect(screen, (255, 0, 0), (45, 45, 100, 100))
                        activePlayer = 1
                    else:
                        pygame.draw.rect(screen, (0, 255, 0), (45, 45, 100, 100))
                        activePlayer = 0

                    for winningPos in winningPositions:
                        if gameState[winningPos[0]] == gameState[winningPos[1]] and gameState[winningPos[1]] == \
                                gameState[winningPos[2]]:
                            if gameState[winningPos[0]] != 2:
                                if activePlayer == 0:
                                    print("Green has won")
                                    running = False
                                elif activePlayer == 1:
                                    print("Red has won")
                                    running = False

            if first.collidepoint(event.pos):
                if gameState[1] == 2:
                    gameState[1] = activePlayer

                    if activePlayer == 0:
                        pygame.draw.rect(screen, (255, 0, 0), (225, 45, 100, 100))
                        activePlayer = 1
                    else:
                        pygame.draw.rect(screen, (0, 255, 0), (225, 45, 100, 100))
                        activePlayer = 0

                    for winningPos in winningPositions:
                        if gameState[winningPos[0]] == gameState[winningPos[1]] and gameState[winningPos[1]] == \
                                gameState[winningPos[2]]:
                            if gameState[winningPos[0]] != 2:
                                if activePlayer == 0:
                                    print("Green has won")
                                    running = False
                                elif activePlayer == 1:
                                    print("Red has won")
                                    running = False

            if second.collidepoint(event.pos):
                if gameState[2] == 2:
                    gameState[2] = activePlayer

                    if activePlayer == 0:
                        pygame.draw.rect(screen, (255, 0, 0), (405, 45, 100, 100))
                        activePlayer = 1
                    else:
                        pygame.draw.rect(screen, (0, 255, 0), (405, 45, 100, 100))
                        activePlayer = 0

                    for winningPos in winningPositions:
                        if gameState[winningPos[0]] == gameState[winningPos[1]] and gameState[winningPos[1]] == \
                                gameState[winningPos[2]]:
                            if gameState[winningPos[0]] != 2:
                                if activePlayer == 0:
                                    print("Green has won")
                                    running = False
                                elif activePlayer == 1:
                                    print("Red has won")
                                    running = False

            if third.collidepoint(event.pos):
                if gameState[3] == 2:
                    gameState[3] = activePlayer

                    if activePlayer == 0:
                        pygame.draw.rect(screen, (255, 0, 0), (45, 215, 100, 100))
                        activePlayer = 1
                    else:
                        pygame.draw.rect(screen, (0, 255, 0), (45, 215, 100, 100))
                        activePlayer = 0

                    for winningPos in winningPositions:
                        if gameState[winningPos[0]] == gameState[winningPos[1]] and gameState[winningPos[1]] == \
                                gameState[winningPos[2]]:
                            if gameState[winningPos[0]] != 2:
                                if activePlayer == 0:
                                    print("Green has won")
                                    running = False
                                elif activePlayer == 1:
                                    print("Red has won")
                                    running = False

            if fourth.collidepoint(event.pos):
                if gameState[4] == 2:
                    gameState[4] = activePlayer

                    if activePlayer == 0:
                        pygame.draw.rect(screen, (255, 0, 0), (225, 215, 100, 100))
                        activePlayer = 1
                    else:
                        pygame.draw.rect(screen, (0, 255, 0), (225, 215, 100, 100))
                        activePlayer = 0

                    for winningPos in winningPositions:
                        if gameState[winningPos[0]] == gameState[winningPos[1]] and gameState[winningPos[1]] == \
                                gameState[winningPos[2]]:
                            if gameState[winningPos[0]] != 2:
                                if activePlayer == 0:
                                    print("Green has won")
                                    running = False
                                elif activePlayer == 1:
                                    print("Red has won")
                                    running = False

            if fifth.collidepoint(event.pos):
                if gameState[5] == 2:
                    gameState[5] = activePlayer

                    if activePlayer == 0:
                        pygame.draw.rect(screen, (255, 0, 0), (405, 215, 100, 100))
                        activePlayer = 1
                    else:
                        pygame.draw.rect(screen, (0, 255, 0), (405, 215, 100, 100))
                        activePlayer = 0

                    for winningPos in winningPositions:
                        if gameState[winningPos[0]] == gameState[winningPos[1]] and gameState[winningPos[1]] == \
                                gameState[winningPos[2]]:
                            if gameState[winningPos[0]] != 2:
                                if activePlayer == 0:
                                    print("Green has won")
                                    running = False
                                elif activePlayer == 1:
                                    print("Red has won")
                                    running = False

            if sixth.collidepoint(event.pos):
                if gameState[6] == 2:
                    gameState[6] = activePlayer

                    if activePlayer == 0:
                        pygame.draw.rect(screen, (255, 0, 0), (45, 385, 100, 100))
                        activePlayer = 1
                    else:
                        pygame.draw.rect(screen, (0, 255, 0), (45, 385, 100, 100))
                        activePlayer = 0

                    for winningPos in winningPositions:
                        if gameState[winningPos[0]] == gameState[winningPos[1]] and gameState[winningPos[1]] == \
                                gameState[winningPos[2]]:
                            if gameState[winningPos[0]] != 2:
                                if activePlayer == 0:
                                    print("Green has won")
                                    running = False
                                elif activePlayer == 1:
                                    print("Red has won")
                                    running = False

            if seventh.collidepoint(event.pos):
                if gameState[7] == 2:
                    gameState[7] = activePlayer

                    if activePlayer == 0:
                        pygame.draw.rect(screen, (255, 0, 0), (225, 385, 100, 100))
                        activePlayer = 1
                    else:
                        pygame.draw.rect(screen, (0, 255, 0), (225, 385, 100, 100))
                        activePlayer = 0

                    for winningPos in winningPositions:
                        if gameState[winningPos[0]] == gameState[winningPos[1]] and gameState[winningPos[1]] == \
                                gameState[winningPos[2]]:
                            if gameState[winningPos[0]] != 2:
                                if activePlayer == 0:
                                    print("Green has won")
                                    running = False
                                elif activePlayer == 1:
                                    print("Red has won")
                                    running = False

            if eighth.collidepoint(event.pos):
                if gameState[8] == 2:
                    gameState[8] = activePlayer

                    if activePlayer == 0:
                        pygame.draw.rect(screen, (255, 0, 0), (405, 385, 100, 100))
                        activePlayer = 1
                    else:
                        pygame.draw.rect(screen, (0, 255, 0), (405, 385, 100, 100))
                        activePlayer = 0

                    for winningPos in winningPositions:
                        if gameState[winningPos[0]] == gameState[winningPos[1]] and gameState[winningPos[1]] == \
                                gameState[winningPos[2]]:
                            if gameState[winningPos[0]] != 2:
                                if activePlayer == 0:
                                    print("Green has won")
                                    running = False
                                elif activePlayer == 1:
                                    print("Red has won")
                                    running = False

    pygame.display.update()

pygame.quit()
