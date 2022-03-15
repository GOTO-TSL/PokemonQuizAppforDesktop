import requests
import json

class PokeModel():

    flavorText = ""
    pokemonName = ""
    hints = []

    def __init__(self, number) -> None:

        self.hints = []

        url = "https://pokeapi.co/api/v2/pokemon-species/"
        response = requests.get(url + str(number))

        jsonData = response.json()

        for flavorTexts in jsonData['flavor_text_entries']:
            if flavorTexts['language']['name'] in 'ja':
                self.flavorText = flavorTexts['flavor_text']

        for names in jsonData['names']:
            if names['language']['name'] in 'ja-Hrkt':
                self.pokemonName = names['name']

        # ヒント1
        for genera in jsonData['genera']:
            if genera['language']['name'] == 'ja':
                self.hints.append(genera['genus'])

        # ヒント2
        self.hints.append(jsonData['name'])

        # ヒント3
        self.hints.append(jsonData['generation']['name'])

        # ヒント4
        self.hints.append(jsonData['color']['name'])

if __name__ == '__main__':
    pokeModel = PokeModel(804)
    print(f"flavor_text:{pokeModel.flavorText}\nname:{pokeModel.pokemonName}")
    print(pokeModel.hints)