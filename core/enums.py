from enum import Enum as PyEnum

class UserRole(PyEnum):
    USER = "user"
    ADMIN = "admin"

class OrderStatus(PyEnum):
    pending = "pending"
    processing = "processing"
    shipped = "shipped"
    completed = "completed"
    canceled = "canceled"

class PaymentMethod(PyEnum):
    cash = "cash"
    card = "card"
    