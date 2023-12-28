from src.server.database import pydantic_models, database_models
from src.server.service import RouterManager


routers = (
    RouterManager(database_model=database_models.User, pydantic_model=pydantic_models.User, prefix='/user', tags=['Users']).fastapi_router,
    RouterManager(database_model=database_models.Product, pydantic_model=pydantic_models.Product, prefix='/product', tags=['Products']).fastapi_router,
    RouterManager(database_model=database_models.Customer, pydantic_model=pydantic_models.Customer, prefix='/customer', tags=['Customers']).fastapi_router,
    RouterManager(database_model=database_models.Order, pydantic_model=pydantic_models.Order, prefix='/order', tags=['Orders']).fastapi_router,
    RouterManager(database_model=database_models.Supplier, pydantic_model=pydantic_models.Supplier, prefix='/supplier', tags=['Suppliers']).fastapi_router,
    RouterManager(database_model=database_models.Employee, pydantic_model=pydantic_models.Employee, prefix='/employee', tags=['Employees']).fastapi_router,
    RouterManager(database_model=database_models.Position, pydantic_model=pydantic_models.Position, prefix='/position', tags=['Positions']).fastapi_router)