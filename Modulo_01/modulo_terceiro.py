print("\nImportação de módulos de terceiros")
import requests

url = "https://www.example.com"
response = requests.get(url)
print(f"Solicitacao HTTP para {url} retornou o status {response.status_code}")