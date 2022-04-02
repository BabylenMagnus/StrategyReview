import tinvest


def sandbox_mod():  # в data/token_sandbox пишите токены свои от сэндбокса
    with open('data/token_sandbox') as f:  # потом в yaml файл будем складывать, если понадобится
        client = tinvest.AsyncClient(f.read(), use_sandbox=True)
    return client
