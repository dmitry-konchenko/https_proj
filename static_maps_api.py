import requests


def get_map(*, ll: tuple[float, float], spn: tuple[float, float], map_type: str) -> str:
    response = requests.get('http://static-maps.yandex.ru/1.x/', params={
        'll': ','.join(map(str, ll)),
        'spn': ','.join(map(str, spn)),
        'l': spn,
    })

    if not response:
        raise RuntimeError(
            f'''Ошибка выполнения запроса:
                    {response.request.url}
                    Http статус: {response.status_code} ({response.reason})''')

    map_file = 'map.png'
    with open(map_file, "wb") as file:
        file.write(response.content)
    return map_file
