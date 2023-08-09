import secrets


class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///extraction.db"
    SECRET_KEY = f"{secrets.token_hex(16)}"
    