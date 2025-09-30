from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Garante que o arquivo exista antes de começar. Se não existir, cria um vazio.
with open('precos.csv', 'a', encoding='utf-8') as arquivo:
    pass

driver = webdriver.Chrome()
driver.get("https://devaprender-play.netlify.app")
sleep(5)

produtos = driver.find_elements(By.XPATH,
                                "//h3[@class='text-lg font-semibold text-gray-900 group-hover:text-indigo-600']")
precos = driver.find_elements(By.XPATH, "//p[@class='text-2xl font-bold text-indigo-600']")

for produto, preco in zip(produtos, precos):

    nova_linha = f'{produto.text};{preco.text}\n'

    with open('precos.csv', 'r', encoding='utf-8') as arquivo:
        conteudo_do_arquivo = arquivo.read()

    if nova_linha not in conteudo_do_arquivo:
        with open('precos.csv', 'a', encoding='utf-8') as arquivo:
            arquivo.write(nova_linha)
            print(f'Adicionando: {produto.text}')
    else:
        print(f'Item já existe, pulando: {produto.text}')

driver.quit()
print("\nProcesso finalizado!")
input('Pressione Enter para sair...')
