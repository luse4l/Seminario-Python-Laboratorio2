from pydantic import BaseModel

# 1. Schema para RECIBIR datos (ej: endpoint POST)
class ProductoCreate(BaseModel):
    nombre: str
    precio: float
    # No pedimos el ID porque la base de datos lo crea con autoincrement

# 2. Schema para DEVOLVER datos (ej: endpoint GET)
class ProductoResponse(BaseModel):
    id: int
    nombre: str
    precio: float

    class Config:
        # Esto es clave: le enseña a Pydantic a "leer" tus objetos de SQLAlchemy
        from_attributes = True