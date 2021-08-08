#pygameのimport
import pygame as pg

#ウィンドウサイズの設定
WIDTH  = 800
HEIGHT = 800

#スクリーンとキャプションの設定
SCREEN = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption('Snake Game')

#色の設定
RED    = (200, 50, 50)
BLUE   = (93, 216, 228)
GREEN  = (0, 255, 50)
YELLOW = (255, 255, 0)
BLACK  = (50, 50, 50)
WHITE  = (255, 255, 255)

#clockとfpsの設定
CLOCK = pg.time.Clock()
FPS = 10

#1マス辺りのサイズ設定
CHIP_SIZE = 20

#テキスト描画用の関数
def draw_text(text, size, x, y, color):
		font = pg.font.Font(None, size)
		text_surface = font.render(text, True, color)
		text_rect = text_surface.get_rect()
		text_rect.midtop = (x, y)
		SCREEN.blit(text_surface,text_rect)
