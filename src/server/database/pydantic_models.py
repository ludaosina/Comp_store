from pydantic import BaseModel


class ModifyBaseModel(BaseModel):
    id: int = 0


class ChangePassword(ModifyBaseModel):
    password: str


class LoginData(BaseModel):
    password: str
    login: str


class User(LoginData):
    id: int = 0
    position: str
    power_level: int


class Product(ModifyBaseModel):
    product_name: str
    description: str
    price: float
    quantity_in_stock: int
    product_category: str

class Customer(ModifyBaseModel):
    first_name: str
    last_name: str
    address: str
    phone_number: str
    email: str

class Order(ModifyBaseModel):
    customer_id: int
    order_date: str
    order_total: float
    order_status: str

class Supplier(ModifyBaseModel):
    company_name: str
    address: str
    phone_number: str
    email: str

class Employee(ModifyBaseModel):
    first_name: str
    last_name: str
    position: str
    salary: float
    start_date: str

class Position(ModifyBaseModel):
    position_name: str