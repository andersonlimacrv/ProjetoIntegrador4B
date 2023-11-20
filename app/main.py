# app/main.py
import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
import json


def init_app():
    # db connection
    app = FastAPI(
        title="Projeto Integrador 4B",
        description="API Rest para cadastro de Clientes da disciplina de Projeto Integrador 4B. 👨🏻‍💻 Anderson Carvalho",
        version="1.0.0",
        docs_url="/docs",
        server_url="http://0.0.0.0:8888",
    )

    # Configuração do CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        expose_headers=["*"],
    )

    data_file = Path("app/repository/clients.json")
    if not data_file.is_file():
        with open(data_file, "w") as file:
            json.dump([], file)

    from app.router.home import router as home_router
    from app.router.clients import router as clients_router

    app.include_router(home_router)
    app.include_router(clients_router)

    return app


app = init_app()


def start():
    """Launched with 'poetry run start' at root level."""
    uvicorn.run("app.main:app", host="0.0.0.0", port=8888, reload=True)
