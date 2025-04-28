def towns():
    cidades = set()
    for n in range(8):
        cidade = input(f"Nome da cidade: ")
        cidades.add(cidade)
    print(f"Quantidade de cidades: {len(cidades)}")
    for city in cidades:
        print(f"Cidade: {city}")
    print(cidades)
towns()