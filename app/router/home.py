from fastapi import APIRouter

router = APIRouter(prefix="", tags=["Home"])


@router.get("/")
def get_home():
    """
    Rota inicial ou ROOT da aplicação.
        - Retorna apenas uma mensagem de boas-vindas para teste.
    """

    return {"message": "Welcome to the home route!"}
