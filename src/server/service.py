from typing import Type
from src.server.database.database_models import BaseModel
from src.server.database.pydantic_models import ModifyBaseModel
import peewee
import fastapi


class RouterManager:
    def __init__(self, database_model: Type[BaseModel], pydantic_model: Type[ModifyBaseModel], prefix: str, tags: [str]) -> None:
        self.database_model: Type[BaseModel] = database_model
        self.pydantic_model: Type[ModifyBaseModel] = pydantic_model
        self.fastapi_router: fastapi.APIRouter = fastapi.APIRouter(prefix=prefix, tags=tags)
        self.resolver_manager: ResolverManager = ResolverManager(self.database_model, self.pydantic_model)
        self.__init_methods()
    
    def __init_methods(self) -> None:
        pm: Type[ModifyBaseModel] = self.pydantic_model

        @self.fastapi_router.get(path='/{id}', response_model=dict)
        def get(id: int) -> dict:
            return self.resolver_manager.get(id)
        
        @self.fastapi_router.get(path='/', response_model=dict)
        def get_all() -> dict:
            return self.resolver_manager.get_all()
        
        @self.fastapi_router.post(path='/', response_model=dict)
        def create(new_model: pm) -> dict:
            return self.resolver_manager.create(new_model)
        
        @self.fastapi_router.put(path='/{id}', response_model=dict)
        def update(id: int, new_model: pm) -> dict:
            return self.resolver_manager.update(id, new_model)
        
        @self.fastapi_router.delete(path='/{id}', response_model=dict)
        def delete(id: int) -> dict:
            return self.resolver_manager.delete(id)


class ResolverManager:
    def __init__(self, database_model: Type[BaseModel], pydantic_model: Type[ModifyBaseModel]) -> None:
        self.database_model = database_model
        self.pydantic_model = pydantic_model
    
    def check_for_errors(self) -> dict:
        try:
            self.check_func()
            return {'code': 200, 'msg': 'Succesfully', 'result': False}
        except peewee.DoesNotExist:
            return {'code': 201, 'msg': 'Test', 'result': False}
        except peewee.DatabaseError as ex:
            return {'code': 400, 'msg': str(ex), 'result': True}
    
    def check_func(self, id=-1):
        return self.database_model.get(self.database_model.id==id)
    
    def get(self, id: int) -> dict:
        check = self.check_for_errors()
        if check['result']:
            return check
        
        res = self.database_model.get_or_none(self.database_model.id == id)
        
        return {'code': 200, 'msg': 'Succesfully', 'result': res.__data__} if res else {'code': 400, 'msg': 'Not found', 'result': None}
    
    def get_all(self) -> dict:
        check = self.check_for_errors()
        if check['result']:
            return check
        
        list_models = []

        for model in self.database_model.select():
            new_model = {}

            for atr in model.__data__:
                get_atr = getattr(model, atr)

                new_model[get_atr] = get_atr.id if isinstance(get_atr, peewee.Model) else get_atr

            list_models.append(new_model)
        
        return {'code': 200, 'msg': 'Succesfully', 'result': list_models} if len(list_models) > 0 else {'code': 400, 'msg': 'Not found', 'result': None}
    
    def create(self, new_model: Type[ModifyBaseModel]) -> dict:
        check = self.check_for_errors()
        if check['result']:
            return check
        
        new_database_model = self.database_model.create()

        for atr in dir(new_model):
            if atr.startswith('__') or atr.startswith('id'):
                continue

            setattr(new_database_model, atr, getattr(new_model, atr))
        
        new_database_model.save()

        return self.get(id=new_database_model.id)
    
    def update(self, id: int, new_model: Type[ModifyBaseModel]) -> dict:
        check = self.check_for_errors()
        if check['result']:
            return check
        
        res = self.get(id=id)

        if res['code'] != 200:
            return res

        model = self.database_model.get(self.database_model.id == id)

        for atr in dir(new_model):
            if atr.startswith('__') or atr.startswith('id'):
                continue

            setattr(model, atr, getattr(new_model, atr))
        
        model.save()

        return self.get(id=model.id)
    
    def delete(self, id: int) -> dict:
        check = self.check_for_errors()
        if check['result']:
            return check
        
        res = self.get(id=id)

        if res['code'] != 200:
            return res
        
        self.database_model.get(self.database_model.id == id).delete_instance()

        return {'code': 200, 'msg': 'Succesfully', 'result': None}
