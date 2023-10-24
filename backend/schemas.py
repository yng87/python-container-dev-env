from pydantic import BaseModel


class HealthCheck(BaseModel):
    status: str


class User(BaseModel):
    name: str
