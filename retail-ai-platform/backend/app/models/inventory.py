from sqlalchemy import Column, Integer
from ..core.database import Base


class Inventory(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, index=True, nullable=False)
    quantity = Column(Integer, default=0, nullable=False)
