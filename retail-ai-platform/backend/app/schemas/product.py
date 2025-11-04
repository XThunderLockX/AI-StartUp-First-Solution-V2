from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str


class ProductOut(ProductBase):
    id: int

    class Config:
        from_attributes = True
