from models import book, user
import requests

url = "https://www.googleapis.com/books/v1/volumes"


# URL del endpoint de búsqueda de la API de Google Books
url = "https://www.googleapis.com/books/v1/volumes"

# Parámetros de búsqueda
params = {
    'q': 'Python',  # Consulta de búsqueda
    'maxResults': 5  # Número máximo de resultados a devolver
}

# Realizar la solicitud GET
response = requests.get(url, params=params)

# Verificar el estado de la respuesta
if response.status_code == 200:
    # Convertir la respuesta en JSON
    data = response.json()
    
    # Imprimir los títulos de los libros encontrados
    for item in data.get('items', []):
        title = item['volumeInfo'].get('title', 'No title')
        print(f"Title: {title}")
else:
    print(f'Error: {response.status_code}')


