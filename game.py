import pygame
from pygame import mixer


pygame.init()
window = pygame.display.set_mode((1280, 608))
pygame.display.set_caption("Cyberpunk 2078")

music = pygame.mixer.music.load('static/sound.mp3')
pygame.mixer.music.play(-1, 0.0)

char = pygame.image.load('static/char.png')
enemy = pygame.image.load('static/enemy.png')
bg = pygame.image.load('static/bg.png')

lose_sign = pygame.image.load('static/lose.png')


x_char = 120
y_char = 410
isjump = False
jumpcount = 10

x_enemy = 1200
y_enemy = 460
speed_enemy = 12

score = 0


def main():
	window.blit(bg, (0, 0))
	window.blit(char, (x_char, y_char))
	window.blit(enemy, (x_enemy, y_enemy))
	pygame.display.update()

while True:
	pygame.time.delay(30)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()

	keys = pygame.key.get_pressed()

	if not(isjump):
		if keys[pygame.K_SPACE]:
			isjump = True
	else:
		if jumpcount >= -10:
			if jumpcount < 0:
				y_char += (jumpcount ** 2) / 2
			else:
				y_char -= (jumpcount ** 2) / 2
			jumpcount -= 1
		else:
			isjump = False
			jumpcount = 10


	if x_enemy > 1:
		x_enemy -= speed_enemy
	else:
		x_enemy = 1200
		score += 1

	if x_enemy == x_char and isjump == False:
		window.blit(lose_sign, (320, 100))
		pygame.display.update()
		lose = True
		while lose == True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()

					print(" ")
					print("Your score is ", score)
					print(" ")

	main()


# cteated by h4cktivist