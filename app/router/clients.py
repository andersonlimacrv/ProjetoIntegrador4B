from fastapi import APIRouter, HTTPException, Depends
from typing import List
from app.model.clients import BaseClient

from app.controller.clients import (
    get_clients_from_file,
    create_client,
    get_clients,
    read_client,
    put_client,
    delete_client,
    patch_client,
)

router = APIRouter(prefix="/clients", tags=["Clients"])


@router.post(
    "",
    response_model=BaseClient,
    summary="Create Client",
    description="Rota que cria um novo cliente. A partir de um objeto Schema -> BaseClient. Caso o ID do cliente informado exista, uma exceção será levantada. Caso o ID do cliente informado não exista, o cliente será criado.",
)
async def create_client_route(
    client: BaseClient,
    current_clients: List[BaseClient] = Depends(get_clients_from_file),
):
    return create_client(client, current_clients)


@router.get(
    "",
    response_model=List[BaseClient],
    summary="Get All Clients",
    description="Rota que retorna uma lista de clientes.",
)
async def get_clients_route(skip: int = 0, limit: int = 10):
    return get_clients(skip, limit)


@router.get(
    "/{client_id}",
    response_model=BaseClient,
    summary="Get Client by ID",
    description="Rota que retorna um cliente a partir de um ID, caso o recurso exista.",
)
async def read_client_route(client_id: int):
    return read_client(client_id)


@router.delete(
    "/{client_id}",
    response_model=BaseClient,
    summary="Delete Client by ID",
    description="Rota que deleta um cliente a partir de um ID. Caso o recurso exista, ele será excluído. Caso o recurso não exista, uma exceção será levantada.",
)
async def delete_client_route(
    client_id: int, current_clients: List[BaseClient] = Depends(get_clients_from_file)
):
    return delete_client(client_id, current_clients)


@router.patch(
    "/{client_id}",
    response_model=BaseClient,
    summary="Patch Client by ID",
    description="Rota que atualiza um cliente a partir de um ID. Caso o recurso exista, ele é atualizado pelo novo estado fornecido no corpo da requição. Caso o recurso não exista, ele não é alterado.",
)
async def patch_client_route(
    client_id: int,
    updated_data: BaseClient,
    current_clients: List[BaseClient] = Depends(get_clients_from_file),
):
    return patch_client(client_id, updated_data, current_clients)


@router.put(
    "/{client_id}",
    response_model=BaseClient,
    summary="Update Client by ID",
    description="Rota que atualiza um cliente a partir de um ID. Caso o recurso exista, ele é substituido pelo novo estado fornecido no corpo da requição. Caso o recurso não exista, ele é criado com o novo estado fornecido no corpo da requição.",
)
async def update_client_route(
    client_id: int,
    updated_data: BaseClient,
    current_clients: List[BaseClient] = Depends(get_clients_from_file),
):
    return put_client(client_id, updated_data, current_clients)
