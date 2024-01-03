import requests
import json

def capturar_dados_https(url):
    try:
        # Fazendo a solicitação HTTPS
        resposta = requests.get(url)

        # Verificando se a solicitação foi bem-sucedida (código de status 200)
        if resposta.status_code == 200:
            # Convertendo a resposta para formato JSON
            dados_json = resposta.json()

            # Escrevendo os dados em um arquivo JSON
            with open('dados.json', 'w', encoding='utf-8') as arquivo_json:
                json.dump(dados_json, arquivo_json, ensure_ascii=False, indent=4)
                
            print("Dados capturados com sucesso e escritos em 'dados.json'")
        else:
            print(f"Erro na solicitação. Código de status: {resposta.status_code}")

    except Exception as e:
        print(f"Erro ao capturar dados: {str(e)}")

# Substitua a URL abaixo pela URL desejada
url = 'https://ipinfo.io/'
capturar_dados_https(url)
