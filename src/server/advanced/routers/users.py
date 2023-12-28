from src.server.router import routers
from src.server.advanced.resolvers.users import login, update
from src.server.database.pydantic_models import LoginData, ChangePassword


user_rout = routers[0]


@user_rout.post(path='/login', response_model=dict)
def log_in(data: LoginData) -> dict:
    return login(login=data.login, password=data.password)


@user_rout.put(path='/change/{id}', response_model=dict)
def change(id: int, new_data: ChangePassword) -> dict:
    return update(id=id, password=new_data.password)