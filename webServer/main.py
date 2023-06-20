import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()

@app.get('/')
def getList():
    return [ 1, 2, 3]

@app.get('/contact', response_class = HTMLResponse)
def getList():
    return """
        <h1>Hola soy una página</h1>
        <p>Y yo soy un parrafo</p>
        """

def run():
    store.getCategories()

if __name__ == '__main__':
    run()