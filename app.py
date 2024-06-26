import streamlit as st
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.wsgi import WSGIMiddleware

# Initialize FastAPI
app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app.post("/items/")
async def create_item(item: Item):
    return item

# Streamlit app
st.title("Streamlit with FastAPI")

st.write("This Streamlit app serves an API using FastAPI.")

# Example usage
example_request = {
    "name": "Foo",
    "description": "A very nice Item",
    "price": 35.4,
    "tax": 3.2
}
st.write("Example API request:")
st.json(example_request)

# Run FastAPI app within Streamlit
from streamlit.server.server import Server

def get_server():
    # Get the server instance
    return Server.get_current()

def add_fastapi_to_streamlit(app):
    server = get_server()
    if server:
        app.mount("/api", WSGIMiddleware(app))

add_fastapi_to_streamlit(app)
