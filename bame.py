import pygame

pygame.init()

screenWidth, screenHeight = 700, 500 
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Bame by Sujal Agre")

running = True
gameOver = False

rectWidth, rectHeight = 100, 20
rectPosition = pygame.Vector2(screen.get_width() / 2 - rectWidth / 2, screen.get_height() - rectHeight - 3.5)

ballRadius = 15
ballPosition = pygame.Vector2(screen.get_width() / 2, screen.get_height() - rectHeight - ballRadius)
ballVelocity = pygame.Vector2(0.2, -0.2)  # ball starts moving right and up first

buttonWidth, buttonHeight = 200, 50
buttonX = screenWidth // 2 - buttonWidth // 2
buttonY = screenHeight // 2 + 20

def reset_game():
    global ballPosition, ballVelocity, rectPosition, gameOver
    ballPosition = pygame.Vector2(screen.get_width() / 2, screen.get_height() - rectHeight - ballRadius)
    ballVelocity = pygame.Vector2(0.2, -0.2)
    rectPosition = pygame.Vector2(screen.get_width() / 2 - rectWidth / 2, screen.get_height() - rectHeight - 3.5)
    gameOver = False

while running:
    # to close the game on clicking X icon
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not gameOver:
        # change position on key press
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if rectPosition.x < screenWidth - rectWidth: rectPosition.x += 0.2
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if rectPosition.x > 0: rectPosition.x -= 0.2

        # ball movement
        ballPosition.x += ballVelocity.x
        ballPosition.y += ballVelocity.y

        # ball collision with left and right walls
        if ballPosition.x - ballRadius <= 0 or ballPosition.x + ballRadius >= screenWidth:
            ballVelocity.x = -ballVelocity.x  # reverse horizontal direction

        # ball collision with top wall
        if ballPosition.y - ballRadius <= 0:
            ballVelocity.y = -ballVelocity.y  # reverse vertical direction

        # ball collision with rectangle
        if (ballPosition.y + ballRadius >= rectPosition.y and
            ballPosition.x >= rectPosition.x and 
            ballPosition.x <= rectPosition.x + rectWidth and
            ballVelocity.y > 0):  # only bounce when ball is moving down
            ballVelocity.y = -ballVelocity.y
            ballPosition.y = rectPosition.y - ballRadius  # adjust position to avoid sticking
        
        if ballPosition.y + ballRadius >= screenHeight:
            gameOver = True

        screen.fill("lightpink") # to clear the screen on every frame
        pygame.draw.rect(screen, "black", (rectPosition.x, rectPosition.y, rectWidth, rectHeight), 20)
        pygame.draw.circle(screen, "white", ballPosition, 15) # drawing a circle above the rectangle
    else:
    # restart menu
        # game over text
        font = pygame.font.Font(None, 74)
        text = font.render("GAME OVER!", True, "red")
        text_rect = text.get_rect(center=(screenWidth//2, screenHeight//2 - 50))
        screen.blit(text, text_rect)
        
        # restart button
        pygame.draw.rect(screen, "white", (buttonX, buttonY, buttonWidth, buttonHeight))
        pygame.draw.rect(screen, "black", (buttonX, buttonY, buttonWidth, buttonHeight), 3)
        
        # restart button text
        button_font = pygame.font.Font(None, 36)
        button_text = button_font.render("RESTART", True, "black")
        button_text_rect = button_text.get_rect(center=(buttonX + buttonWidth//2, buttonY + buttonHeight//2))
        screen.blit(button_text, button_text_rect)

        # instructions
        inst_font = pygame.font.Font(None, 28)
        inst_text = inst_font.render("Click button or Press ENTER", False, "white")
        inst_rect = inst_text.get_rect(center=(screenWidth//2, buttonY + buttonHeight + 30))
        screen.blit(inst_text, inst_rect)

    # restart menu behavior
    if event.type == pygame.MOUSEBUTTONDOWN:
            if gameOver:
                mouse_x, mouse_y = event.pos
                # if click is within button area
                if (buttonX <= mouse_x <= buttonX + buttonWidth and
                    buttonY <= mouse_y <= buttonY + buttonHeight):
                    reset_game()
    if event.type == pygame.KEYDOWN:
            if gameOver and event.key == pygame.K_RETURN:
                reset_game()

    pygame.display.flip() # to show stuff on screen

pygame.quit() # clearing memory on closing the game

# name, icon, add 3 sfx, score, high score and fps limiting