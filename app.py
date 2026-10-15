from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, Producto 
from schema import ProductoResponse

app = FastAPI()

#abrir la conexión cuando llega una petición y cerrarla apenas termina.
def get_db():
    #Esta línea crea una sesión única y exclusiva para ese usuario instanciando tu fábrica de sesiones.
    db = SessionLocal() # Tu fábrica de sesiones (Session = sessionmaker(...))
    try:
        #trae la base de datos, ejecuta y espera y luego vuelve
        yield db
    finally:
        db.close()

@app.get("/") #es el home
async def root():
    return {"message": "Hello World"}

@app.get("/producto", response_model=ProductoResponse)
def listar_productos(database: Session = Depends(get_db)):
    
    # Buscamos el producto usando la sesión
    producto = database.query(Producto).all()
    
    # Si no existe, lanzamos el error con código 404
    if producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
        
    # Si existe, lo devolvemos
    return producto

#buscar x id
@app.get("/producto/{id}", response_model=ProductoResponse)
def obtener_producto(id: int, database: Session = Depends(get_db)):
    
    # Buscamos el producto usando la sesión
    producto = database.get(Producto, id)
    
    # Si no existe, lanzamos el error con código 404
    if producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
        
    # Si existe, lo devolvemos
    return producto