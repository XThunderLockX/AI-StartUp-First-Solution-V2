from pydantic import BaseModel


class InventoryBase(BaseModel):
    product_id: int
    quantity: int


class InventoryOut(InventoryBase):
    id: int

    class Config:
        from_attributes = True
