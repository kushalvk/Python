from fastapi import FastAPI, Depends # this is show error because 'fastapi' working in virtual environment(VM) - myenv
from models import Product
from database import session, engine
import database_models
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"]
)

database_models.Base.metadata.create_all(bind=engine)

@app.get("/")
def greet():
    return "Welcome to Kushal's First Fast API Project."

products = [
    Product(id=1, name="Phone", description="Budget smartphone", price=99.00, quantity=10),
    Product(id=2, name="Laptop", description="High performance gaming laptop", price=999.00, quantity=7),
    Product(id=3, name="Headphones", description="Noise cancelling wireless headphones", price=149.50, quantity=25),
    Product(id=4, name="Keyboard", description="Mechanical RGB keyboard", price=79.99, quantity=15),
    Product(id=5, name="Mouse", description="Wireless optical mouse", price=29.99, quantity=40),
    Product(id=6, name="Monitor", description="24-inch Full HD LED monitor", price=189.99, quantity=12),
    Product(id=7, name="PowerBank", description="20000mAh fast charging power bank", price=49.99, quantity=20)
]

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

def init_db():
    db = session()

    count = db.query(database_models.Product).count

    if count == 0:
        for product in products:
            db.add(database_models.Product(**product.model_dump()))

        db.commit()
init_db()

@app.get("/products")
def get_all_products(db: Session = Depends(get_db)):
    db_products = db.query(database_models.Product).all()
    return db_products

@app.get("/product/{id}")
def get_product_by_id(id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        return db_product
    return "Product not found"

@app.post("/products")
def add_product(product: Product, db: Session = Depends(get_db)):
    db.add(database_models.Product(**product.model_dump()))
    db.commit()
    return product

@app.put("/products/{id}")
def get_product_by_id(id: int, newProduct: Product, db: Session = Depends(get_db)):
    old_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if old_product:
        old_product.name = newProduct.name
        old_product.description = newProduct.description
        old_product.price = newProduct.price
        old_product.quantity = newProduct.quantity
        db.commit()
        return "Product updated successfully"
    else:
        return "Product not found"

@app.delete("/products/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return "Product deleted"
    else:
        return "Product not found"