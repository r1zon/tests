import unittest
import requests

class TestTranslate(unittest.TestCase):
    def test_translate_from_en_to_ru(self):
        API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
        URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
        params = {
            'key': API_KEY,
            'text': 'Cat',
            'lang': '{}-{}'.format('en', 'ru'),
        }
        response = requests.get(URL, params=params)
        code = response.json()["code"]
        text = ''.join(response.json()['text'])
        self.assertEqual(code, 200)
        print(f'Код запроса: {code}')
        self.assertEqual(text, 'Кошка')
        print('Успешный перевод: Cat - Кошка')

    def test_translate_from_ru_to_en(self):
        API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
        URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
        params = {
            'key': API_KEY,
            'text': 'Я студент',
            'lang': '{}-{}'.format('ru', 'en'),
        }
        response = requests.get(URL, params=params)
        code = response.json()["code"]
        text = ''.join(response.json()['text'])
        self.assertEqual(code, 200)
        print(f'Код запроса: {code}')
        self.assertEqual(text, 'I am a student')
        print('Успешный перевод: Я студент - I am a student')


    def test_error_translate_from_en_to_ru(self):
        API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
        URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
        params = {
            'key': API_KEY,
            'text': 'Cat',
            'lang': '{}-{}'.format('eng', 'ru'),
        }
        response = requests.get(URL, params=params)
        code = response.json()["code"]
        self.assertNotEqual(code, 200)
        print(f'Код запроса: {code} - неправильно введен язык перевода')
