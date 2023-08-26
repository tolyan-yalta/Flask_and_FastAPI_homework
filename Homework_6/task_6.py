from fastapi import FastAPI
import uvicorn
import sqlalchemy
from sqlalchemy import create_engine
import databases
from pydantic import BaseModel, Field, PastDatetime
from datetime import datetime
from typing import List
import random

DATABASE_URL = "sqlite:///mydatabase_6.db"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table("users", metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(80)),
    sqlalchemy.Column("surname", sqlalchemy.String(80)),
    sqlalchemy.Column("email", sqlalchemy.String(128)),
    sqlalchemy.Column("password", sqlalchemy.String(128)),
    sqlalchemy.Column("access", sqlalchemy.Boolean()),
    )
products = sqlalchemy.Table("products", metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(128)),
    sqlalchemy.Column("description", sqlalchemy.String(128)),
    sqlalchemy.Column("price", sqlalchemy.Integer()),
    )

orders = sqlalchemy.Table("orders", metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("date", sqlalchemy.DateTime()),
    sqlalchemy.Column("status", sqlalchemy.Boolean()),
    sqlalchemy.Column("user_id", sqlalchemy.ForeignKey("users.id")),
    sqlalchemy.Column("product_id", sqlalchemy.ForeignKey("products.id")),
    )

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata.create_all(engine)

app = FastAPI()

class UserIn(BaseModel):
    name: str = Field(max_length=80)
    surname: str = Field(max_length=80)
    email: str = Field(max_length=128)
    password: str = Field(min_length=8, max_length=128)
    access: bool = Field(default=True)

class User(UserIn):
    id: int

class ProductIn(BaseModel):
    name: str = Field(max_length=128)
    description: str = Field(max_length=128)
    price: int

class Product(ProductIn):
    id: int

class OrderIn(BaseModel):
    date: PastDatetime = Field(default=datetime.now())
    status: bool = Field(default=True)
    user_id: int
    product_id: int

class Order(OrderIn):
        id: int

@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


"""Working with a table Users"""


@app.post("/create_user/", response_model=User)
async def create_user(user: UserIn):
    """Create user for table Users"""
    # query = users.insert().values(name=user.name, surname=user.surname, email=user.email, password=user.password)
    query = users.insert().values(**user.model_dump())
    last_record_id = await database.execute(query)
    return {**user.model_dump(), "id": last_record_id}


# @app.get("/fake_users/{count}")
# async def create_fake_users(count: int):
#     """Create 'count' fake users for table Users"""
#     for i in range(1, count + 1):
#         query = users.insert().values(name=f'user{i}', surname=f'surname{i}', 
#                                       email=f'mail{i}@mail.ru', password=f'password{i}', access=True)
#         await database.execute(query)
#     return {'message': f'{count} fake users create'}


@app.get("/read_users/", response_model=List[User])
async def read_users():
    """Read all users from table Users"""
    query = users.select()
    return await database.fetch_all(query)


@app.get("/read_user/{user_id}", response_model=User)
async def read_user(user_id: int):
    """Read user with 'user_id' from table Users"""
    query = users.select().where(users.c.id == user_id)
    return await database.fetch_one(query)


@app.put("/update_user/{user_id}", response_model=User)
async def update_user(user_id: int, new_user: UserIn):
    """Update data for user with 'user_id' from table Users"""
    query = users.update().where(users.c.id == user_id).values(**new_user.model_dump())
    await database.execute(query)
    return {**new_user.model_dump(), "id": user_id}


@app.delete("/delete_user/{user_id}")
async def delete_user(user_id: int):
    """Delete user with 'user_id' from table Users"""
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return {'message': 'User deleted'}


"""Working with a table Products"""


@app.post("/create_product/", response_model=Product)
async def create_product(product: ProductIn):
    """Create product for table Products"""
    query = products.insert().values(**product.model_dump())
    last_record_id = await database.execute(query)
    return {**product.model_dump(), "id": last_record_id}


# @app.get("/fake_products/{count}")
# async def create_fake_products(count: int):
#     """Create 'count' fake products for table Products"""
#     for i in range(1, count + 1):
#         query = products.insert().values(name=f'product{i}', description=f'product description{i}', price=i**3)
#         await database.execute(query)
#     return {'message': f'{count} fake products create'}


@app.get("/read_products/", response_model=List[Product])
async def read_products():
    """Read all products from table Products"""
    query = products.select()
    return await database.fetch_all(query)


@app.get("/read_product/{product_id}", response_model=Product)
async def read_product(product_id: int):
    """Read product with 'product_id' from table Products"""
    query = products.select().where(products.c.id == product_id)
    return await database.fetch_one(query)


@app.put("/update_product/{product_id}", response_model=Product)
async def update_product(product_id: int, new_product: ProductIn):
    """Update data for product with 'product_id' from table Products"""
    query = products.update().where(products.c.id == product_id).values(**new_product.model_dump())
    await database.execute(query)
    return {**new_product.model_dump(), "id": product_id}


@app.delete("/delete_product/{product_id}")
async def delete_product(product_id: int):
    """Delete product with 'product_id' from table Products"""
    query = products.delete().where(products.c.id == product_id)
    await database.execute(query)
    return {'message': 'product deleted'}


"""Working with a table Orders"""


@app.post("/create_order/", response_model=Order)
async def create_order(order: OrderIn):
    """Create order for table Orders"""
    query = orders.insert().values(**order.model_dump())
    last_record_id = await database.execute(query)
    return {**order.model_dump(), "id": last_record_id}


# @app.get("/fake_orders/{count}")
# async def create_fake_orders(count: int):
#     """Create 'count' fake orders for table Orders"""
#     for i in range(1, count + 1):
#         query = orders.insert().values(date=datetime.datetime.now(), status=True, 
#                                         user_id=random.randint(1, 5), product_id=random.randint(1, 10))
#         await database.execute(query)
#     return {'message': f'{count} fake orders create'}


@app.get("/read_orders/", response_model=List[Order])
async def read_orders():
    """Read orders from table Orders"""
    query = orders.select()
    return await database.fetch_all(query)


@app.get("/read_order/{order_id}", response_model=Order)
async def read_order(order_id: int):
    """Read order with order_id' from table Orders"""
    query = orders.select().where(orders.c.id == order_id)
    return await database.fetch_one(query)


@app.put("/update_order/{order_id}", response_model=Order)
async def update_order(order_id: int, new_order: OrderIn):
    """Update data for order with 'order_id' from table Orders"""
    query = orders.update().where(orders.c.id == order_id).values(**new_order.model_dump())
    await database.execute(query)
    return {**new_order.model_dump(), "id": order_id}


@app.delete("/delete_order/{order_id}")
async def delete_order(order_id: int):
    """Delete order with 'order_id' from table Orders"""
    query = orders.delete().where(orders.c.id == order_id)
    await database.execute(query)
    return {'message': 'order deleted'}


if __name__ == "__main__":
    uvicorn.run("task_6:app", port=8000, reload=True)
    # http://127.0.0.1:8000/docs
    # http://127.0.0.1:8000/fake_users/5
    # http://127.0.0.1:8000/fake_products/10
    # http://127.0.0.1:8000/fake_orders/10
