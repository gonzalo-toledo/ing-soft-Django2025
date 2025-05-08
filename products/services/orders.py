from products.models import Order
from products.repositories.orders import OrderRepository


class OrderService:
    @staticmethod
    def get_all() -> list[Order]:
        return OrderRepository.get_all()
    