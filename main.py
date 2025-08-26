import requests

def get_digimon(nome):
    url = f"https://digi-api.com/api/v1/digimon?name={nome}"
    response = requests.get(url)

    if response.status_code != 200:
        print("Erro: ", response.status_code)
        return None

    digimon = response.json()

    if "content" in digimon:
        if digimon["content"]:
            return digimon["content"][0]
        else:
            return None
    else:
        return None

#MAIN
while True:
    nome = input("Digite o nome de um digimon: ")
    digimon_escolhido = get_digimon(nome)
    if digimon_escolhido:
        break
    else:
        print("Digimon não encontrado")

print(digimon_escolhido["name"])