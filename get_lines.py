import os
from sys import argv
import pygame
from geocode_api import get_coordinates
from static_maps_api import get_map


def main() -> None:
    toponym_to_find = ' '.join(argv[1:])

    if toponym_to_find == '':
        print('No data')
        exit()

    lat, lon = get_coordinates(toponym_to_find)
    show_map((lat, lon), (0.005, 0.005), 'map')


def show_map(ll: tuple[float, float], spn: tuple[float, float], map_type: str) -> None:
    map_filename = get_map(ll, spn, map_type)
    pygame.init()
    screen = pygame.display.set_mode((600, 450))
    screen.blit(pygame.image.load(map_filename), (0, 0))
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
    os.remove(map_filename)


if __name__ == '__main__':
    main()
