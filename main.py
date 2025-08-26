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
    digimon_escolhido = get_digimon(nome_input)
    if digimon_escolhido:
        break
    else:
        print("Digimon não encontrado")

lista_prior_evolutions = digimon_escolhido["priorEvolutions"]
lista_next_evolutions = digimon_escolhido["nextEvolutions"]

print("Prior Evolutions\n")
for digi in lista_prior_evolutions:
    print(digi["digimon"])

print("\n" + "-"*24 + "\n")

print("Next Evolutions\n")
for digi in lista_next_evolutions:
    print(digi["digimon"])
