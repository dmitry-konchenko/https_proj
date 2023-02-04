from sys import argv

from search_maps_api import find_nearest_organization
from geocoder_api import (
    get_coordinates,
)
from show_map import show_map


def main() -> None:
    toponym_to_find = ' '.join(argv[1:])

    if toponym_to_find == '':
        print('No data')
        return

    # Получаем координаты ближайшей аптеки.
    lat, lon = get_coordinates(toponym_to_find)
    organization = find_nearest_organization(ll=(lat, lon), span=(0.005, 0.005),
                                             organization_type='аптека')
    org_lat, org_lon = map(float, organization['geometry']['coordinates'])
    show_map(ll=(lat, lon), spn=(0.005, 0.005), map_type='map', pt=(org_lat, org_lon, 'pm2dgl'))

    # Добавляем на карту точку с исходным адресом.
    show_map(ll=(lat, lon), spn=(0.005, 0.005), map_type='map',
             pt=f'{org_lat},{org_lon},pm2dgl~{lat},{lon},pm2rdl')

    # Автопозиционирование
    show_map(spn=(0.005, 0.005), map_type='map',
             pt=f'{org_lat},{org_lon},pm2dgl~{lat},{lon},pm2rdl')


main()

