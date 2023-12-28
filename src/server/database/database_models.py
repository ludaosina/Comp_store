from peewee import *

database = SqliteDatabase('database.db')

class BaseModel(Model):
    class Meta:
        database = database


class User(BaseModel):
    login = TextField(default='')
    password = TextField(default='')
    position = TextField(default='')
    power_level = IntegerField(default=0)


class Product(BaseModel):
    product_name = TextField(default='')
    description = TextField(default='')
    price = FloatField(default=0.0)
    quantity_in_stock = IntegerField(default=0)
    product_category = TextField(default='')

class Customer(BaseModel):
    first_name = TextField(default='')
    last_name = TextField(default='')
    address = TextField(default='')
    phone_number = TextField(default='')
    email = TextField(default='')

class Order(BaseModel):
    customer_id = ForeignKeyField(Customer, backref='orders')
    order_date = TextField(default='')
    order_total = FloatField(default=0.0)
    order_status = TextField(default='')

class Supplier(BaseModel):
    company_name = TextField(default='')
    address = TextField(default='')
    phone_number = TextField(default='')
    email = TextField(default='')

class Employee(BaseModel):
    first_name = TextField(default='')
    last_name = TextField(default='')
    position = TextField(default='')
    salary = FloatField(default=0.0)
    start_date = TextField(default='')

class Position(BaseModel):
    position_name = TextField(default='')

database.create_tables([User, Product, Customer, Order, Supplier, Employee, Position])