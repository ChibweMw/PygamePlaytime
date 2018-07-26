import sys, pygame
import random
pygame.init()


randColor = colR, colG, colB = random.randint(50, 200), random.randint(50, 200) , random.randint(50, 200)
size = width, height = 640, 480
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
pygame.display.set_caption("Arkshard Rezonator")
screen = pygame.display.set_mode(size)
font = pygame.font.SysFont(None, 25)

clock = pygame.time.Clock()

def message(msg, color):
	screen_text = font.render(msg, True, color)
	screen.blit(screen_text, [0,0])	

def gameLoop():

	gameExit = False
	
	jumpCount = 10

	char_x = width/2
	char_y = height/2

	char_x_change = 0
	char_y_change = 0

	char_height = 10
	char_width = 10

	plat_width = 60
	plat_height = 20

	plat_x = width / 2
	plat_y = height - plat_height



	while not gameExit:

		for event in pygame.event.get(): 
			if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
				gameExit = True

		keys = pygame.key.get_pressed()

		if char_x <= 0  and not keys[pygame.K_RIGHT]:
			char_x_change = 0
			char_x += 0
		elif char_x >= (width - char_width) and not keys[pygame.K_LEFT]:
			char_x_change = 0
			char_x = (width - char_width)
		else:
			char_x += char_x_change

		if char_y <= 0  and not keys[pygame.K_DOWN]:
			char_y_change = 0
			char_y += 0
		elif char_y >= (height - char_height) and not keys[pygame.K_UP]:
			char_y_change = 0
			char_y = (height - char_height)
		else:
			char_y += char_y_change

		if keys[pygame.K_LEFT]:
			char_x_change = -char_width
		if keys[pygame.K_RIGHT]:
			char_x_change = char_width
		if keys[pygame.K_UP]:
			char_y_change = -char_height
		if keys[pygame.K_DOWN]:
			char_y_change = char_height

		if not (keys[pygame.K_UP] or keys[pygame.K_DOWN]):
			char_y_change = 0
		if not (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]):
			char_x_change = 0


		screen.fill(black)
		message("FPS: " + str(clock.get_fps()), white)

		player = pygame.draw.rect(screen, randColor, [char_x, char_y, char_width, char_height])

		platformGroup = []

		i = 1
		while i < 10:
			platformGroup.append(pygame.draw.rect(screen, red, [((plat_width * i) + plat_width), (height - plat_height * i), plat_width, plat_height]))
			i += 1

		for platform in platformGroup:
			if player.colliderect(platform):
				print str(platform.top)

		pygame.display.update()

		clock.tick(30)


	pygame.quit()
	quit()

gameLoop()