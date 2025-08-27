import requests

def get_digimon(nome):
    url = f"https://digi-api.com/api/v1/digimon/{nome}"
    response = requests.get(url)

    if response.status_code != 200:
        print("Erro: ", response.status_code)
        return None

    digimon = response.json()

    return digimon

#MAIN
while True:
    nome_input = input("Digite o nome de um digimon: ")
    nome_input = nome_input.lower().strip()
    print(nome_input)
    digimon_escolhido = get_digimon(nome_input)
    if digimon_escolhido:
        break
    else:
        print("Digimon não encontrado")

lista_next_evolutions = digimon_escolhido["nextEvolutions"]

print("Next Evolutions\n")
for digi in lista_next_evolutions:
    print(digi["digimon"])
