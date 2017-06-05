"""
translate.py - VoxBox module
Translates specified text to other languages
"""

import json, urllib

# yandex translate api key
api_key = ''

country_codes = {
    'angielski': 'en',
    'niemiecki': 'de',
    'francuski': 'fr'
}

def translate(bot, input_groups):
    lang = input_groups[0]
    lang_code = country_codes[lang]
    text = urllib.quote(input_groups[1])
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate?key=%s&text=%s&lang=pl-%s' % (api_key, text, lang_code)
    try:
        u = urllib.urlopen(url)
        raw_data = u.read()
        obj = json.loads(raw_data)
        translated_text = obj['text']
        return translated_text
    except:
        return 'Nie udało się przetłumaczyć'

translate.pattern = r'przetłumacz na ([a-z]+) (.*)'
translate.priority = 1