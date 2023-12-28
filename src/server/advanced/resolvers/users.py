from src.server.database import pydantic_models, database_models


def login(login: str, password: str) -> dict:
    res = database_models.User.get_or_none(database_models.User.login == login, database_models.User.password == password)
    return {'code': 200, 'msg': 'Succesfully', 'result': pydantic_models.User(
        id=res.id,
        login=res.login,
        password=res.password,
        position=res.position,
        power_level=res.power_level
    )} if res else {'code': 400, 'msg': 'Not found', 'result': None}


def update(id: int, password: str) -> dict:
    model = database_models.User.get_or_none(database_models.User.id == id)
    if model:
        model.password = password
        model.save()
    return {'code': 200, 'msg': 'Succesfully', 'result': pydantic_models.User(
        id=model.id,
        position=model.position,
        login=model.login,
        password=model.password,
        power_level=model.power_level
    )}