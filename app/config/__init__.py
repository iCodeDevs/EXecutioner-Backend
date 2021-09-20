from pydantic import BaseSettings
class Settings(BaseSettings):
    # default conf goes here
    app_name: str = "EXecutioner API"
    admin_email: str
    class Config:
        env_file = ".env"