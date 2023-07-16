from pydantic import BaseModel, SecretStr

class usr_in(BaseModel):
    user_email: str
    f_name: str
    l_name: str
    phone_num: str
    street: str
    u_zip: str
    city: str
    state: str
    user_password: SecretStr

class usr_out(BaseModel):
    user_email: str
    f_name: str
    l_name: str
    phone_num: str
    street: str
    u_zip: str
    city: str
    state: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "user_email": "Foo@bar.com",
                    "f_name": "Foo",
                    "l_name": "Boo",
                    "phone_num": "814-521-3933",
                    "street": "123 Some Street",
                    "u_zip": "12345",
                    "city": "Cool City",
                    "state": "Ohio",
                }
            ]
        }
    }