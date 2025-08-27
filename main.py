import requests

def next_evolutions(lista,num):
    print("Next Evolutions\n")
    for digi in lista:
        print(" "*num + digi["digimon"])
        novo_digimon = get_digimon(digi["digimon"])
        nova_lista = novo_digimon["nextEvolutions"]
        next_evolutions(nova_lista, num+1)

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

next_evolutions(lista_next_evolutions,0)
