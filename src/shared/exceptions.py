from fastapi import HTTPException

def unauthorized():
    return HTTPException(
        status_code=401, 
        detail="Invalid cpf or password"
    )

def not_found(resource: str):
    return HTTPException(
        status_code=404,
        detail=f"{resource} Not found"
    )