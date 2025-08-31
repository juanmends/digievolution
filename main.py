import requests

set_digimon = set()

def level_check(levels):
    if not levels:
        return True
    for level in levels:
        # print(level)
        if level["level"] == "Perfect" or level["level"] == "Ultimate":
            return True
    return False

def next_evolutions(lista,num=0,primeira_chamada=True):
    if primeira_chamada:
        set_digimon.clear()
        print("Next Evolutions:")
    for digi in lista:
        print(" "*num + digi["digimon"])
        novo_digimon = get_digimon(digi["digimon"])
        digi_id = novo_digimon["id"]
        if digi_id in set_digimon:
            continue
        else:
            set_digimon.add(digi_id)
        levels = novo_digimon["levels"]
        if level_check(levels):
            continue
        nova_lista = novo_digimon["nextEvolutions"]
        next_evolutions(nova_lista, num+1, primeira_chamada=False)

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

next_evolutions(lista_next_evolutions)
