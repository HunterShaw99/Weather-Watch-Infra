from pydantic import BaseModel, SecretStr

class usr_in(BaseModel):
    user_email: str
    f_name: str
    l_name: str
    phone_num: str
    user_password: SecretStr | None = None

class usr_out(BaseModel):
    user_email: str
    f_name: str
    l_name: str
    phone_num: str
