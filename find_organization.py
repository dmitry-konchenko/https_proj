from config import SEARCH_MAPS_API_KEY
import requests


def find_nearest_organization(ll: tuple[float, float], span: tuple[float, float],
                              organization_type: str) -> dict | None:
    # Выполняем запрос.
    response = requests.get('http://geocode-maps.yandex.ru/1.x/', params={
        'apikey': API_KEY,
        'span': ','.join(map(str, span)),
        'text': organization_type,
        'll': ','.join(map(str, ll)),
        'lang': 'ru_RU',
        'type': 'biz',
    })

    if not response:
        raise RuntimeError(
            f'''Ошибка выполнения запроса:
                {response.request.url}
                Http статус: {response.status_code} ({response.reason})''')

    data = response.json()
    organizations = data['features']
    if len(organizations) == 0:
        return None
    return organizations[0]
