from sqlalchemy import Column, Integer, Float, String, Boolean, Text, TIMESTAMP, func, Enum, ForeignKey, DECIMAL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from core.enums import *
Base = declarative_base()

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    photo_url = Column(String(500))
    created_at = Column(TIMESTAMP, server_default=func.now())


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    role = Column(Enum(UserRole), default=UserRole.USER)
    fname = Column(String(100), nullable=False)
    sname = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=True)
    phone = Column(String(30), unique=True, nullable=False)
    password = Column(Text, nullable=False)
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP, server_default=func.now())

    orders = relationship("Order", back_populates="user", cascade="all, delete")
    products = relationship("Product", back_populates="user", cascade="all, delete")


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    seller_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    category_id = Column(Integer, ForeignKey("category.id"), nullable=False)

    name = Column(String(150), nullable=False)
    description=Column(String(500), nullable=False)
    city = Column(String(100), nullable=False)
    price=Column(DECIMAL(10, 2), nullable=False)

    create_at = Column(TIMESTAMP, server_default=func.now())

    category = relationship("Category", back_populates="products")
    seller = relationship("User", back_populates="products")
    images = relationship("ProductImage", back_populates="products", cascade="all, delete")


class ProductImage(Base):
    __tablename__ = "product_images"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id", ondelete="CASCADE"))
    image_url = Column(String(500), nullable=False)
    is_main = Column(Boolean, default=False)

    created_at = Column(TIMESTAMP, server_default=func.now())

    product = relationship("Product", back_populates="photo_images")

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    status = Column(Enum(OrderStatus), default=OrderStatus.pending, nullable=False)
    payment_method = Column(Enum(PaymentMethod), nullable=False)