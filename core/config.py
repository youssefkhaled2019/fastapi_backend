from pydantic_settings import BaseSettings

from pydantic import ConfigDict
class Settings(BaseSettings):

    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM:str
    ACCESS_TOKEN_EXPIRE_MINUTES:int
    REFRESH_TOKEN_EXPIRE_DAYS: int

    ADMIN_USERNAME: str
    ADMIN_EMAIL: str
    ADMIN_PASSWORD: str
    
    TEST_ADMIN_USERNAME: str
    TEST_ADMIN_EMAIL: str
    TEST_ADMIN_PASSWORD: str
    # class Config:
    #     env_file = ".env"

    model_config = ConfigDict(env_file=".env")


settings = Settings()

