import requests

urlApiCategories = 'https://api.escuelajs.co/api/v1/categories'

def getCategories():
    r = requests.get(urlApiCategories)

    print(r.status_code) # -> 200
    print(r.text) # -> Devuelve el diccionario en formato str
    print(type(r.text)) # -> str
    
    categories = r.json() # Ver la información que entrega el api en formato json no un simple string
    
    for category in categories:
        print(category['name'])