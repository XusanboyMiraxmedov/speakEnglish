import requests

app_id = "32c62cfb"
app_key = "	88f53ffe1ca5f079813e82167dde878c"
language = "en-gb"
word_id = "example"

def getDefinitions(wort_id):
    url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
    r = requests.get(url, headers={"app_id": "32c62cfb", "app_key": "88f53ffe1ca5f079813e82167dde878c"})
    res = r.json()
    if 'error' in res.keys():
        return False

    output = {}
    senses = res['results'][0]['lexicalEntries'][0]['entries'][0]['senses']
    definitions = []
    for sense in senses:
        definitions.append(f"👉 {sense['definitions'][0]}")
    output['definitions'] = "\n".join(definitions)

    if res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0].get('audioFile'):
        output['audio'] = res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile']

    return output

if __name__ == '__main__':
    from pprint import pprint as print
    print(getDefinitions('Great Britain'))
    print(getDefinitions('fneifug'))


