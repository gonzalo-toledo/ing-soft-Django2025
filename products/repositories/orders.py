from products.models import Order

class OrderRepository:
    @staticmethod
    def get_all() -> list[Order]:
        """
        Obtiene todos los pedidos
        """
        return Order.objects.all()