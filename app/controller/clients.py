# app/controller/clients.py
from fastapi import HTTPException
from typing import List, Optional
from app.model.clients import BaseClient
import json
from pathlib import Path


def get_clients_from_file() -> List[BaseClient]:
    data_file = Path("app/repository/clients.json")
    if data_file.is_file():
        with open(data_file, "r") as file:
            clients_data = json.load(file)
            return [BaseClient(**client_data) for client_data in clients_data]
    return []


def save_clients_to_file(clients: List[BaseClient]) -> None:
    data_file = Path("app/repository/clients.json")
    clients_data = [client.dict() for client in clients]
    with open(data_file, "w") as file:
        json.dump(clients_data, file)


def create_client(client: BaseClient, clients: List[BaseClient]) -> BaseClient:
    # Verifica se o ID do cliente já existe na lista
    if any(existing_client.id == client.id for existing_client in clients):
        raise HTTPException(
            status_code=400, detail="Client with the same ID already exists"
        )

    clients.append(client)
    save_clients_to_file(clients)
    return client


def get_clients(skip: int = 0, limit: int = 10) -> List[BaseClient]:
    clients = get_clients_from_file()
    return clients[skip : skip + limit]


def read_client(client_id: int) -> BaseClient:
    clients = get_clients_from_file()
    for client in clients:
        if client.id == client_id:
            return client
    raise HTTPException(status_code=404, detail="Client not found")


def delete_client(client_id: int, clients: List[BaseClient]) -> BaseClient:
    for i, client in enumerate(clients):
        if client.id == client_id:
            del clients[i]
            save_clients_to_file(clients)
            return client
    raise HTTPException(status_code=404, detail="Client not found")


""" 
    PUT:
    - Valida todos os campos do json
    - Verifica se existe Cliente com o ID informado
        Caso exista:
            - Atualiza os dados do cliente
        Caso  não exista:
            - Cria um Novo cliente
         
        - Cria um Novo cliente caso não exista
    - Atualiza os dados do cliente
    - Retorna o cliente atualizado
    - Campos completos
    - Se o recurso existir, ele é substituido pelo novo estado fornecido no corpo da requição
"""


def put_client(
    client_id: int, updated_data: BaseClient, clients: List[BaseClient]
) -> BaseClient:
    for i, client in enumerate(clients):
        if client.id == client_id:
            # Atualiza todos os campos do cliente
            for field, value in updated_data.model_dump(exclude_unset=True).items():
                setattr(client, field, value)

            save_clients_to_file(clients)
            return client

    # Se o cliente não foi encontrado, cria um novo cliente
    new_client_data = updated_data.model_dump(exclude_unset=True)
    new_client_data["id"] = client_id
    new_client = BaseClient(**new_client_data)
    clients.append(new_client)
    save_clients_to_file(clients)
    return new_client


""" 
    PATCH:
    - Precisa Apenas do id;
    - Verifica se existe Cliente com o ID informado;

        Caso exista:
            - Atualiza apenas os dados passados na requisição;
            - Retorna o cliente atualizado;
    
        Caso Não exista:
            - Retorna uma exceção;
]
"""


def patch_client(
    client_id: int, updated_data: Optional[BaseClient], clients: List[BaseClient]
) -> BaseClient:
    for i, client in enumerate(clients):
        if client.id == client_id:
            # Atualiza apenas os campos fornecidos na requisição
            if updated_data is not None:
                for field, value in updated_data.model_dump(exclude_unset=True).items():
                    setattr(client, field, value)

            save_clients_to_file(clients)
            return client
    raise HTTPException(status_code=404, detail="Client not found")
