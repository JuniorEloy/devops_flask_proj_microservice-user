class Config:
    SECRET_KEY = b'um-nome-bem-seguro'
    
class Development(Config):
    Debug = True

class Production(Config):
    Debug = False


config = {
    "development": Development,
    "production": Production

}
