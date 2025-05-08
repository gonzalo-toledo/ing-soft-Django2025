from products.models import Customer

class CustomerRepository:
    @staticmethod
    def get_all() -> list[Customer]:
        """
        Obtiene todos los objects (Clientes)
        """
        return Customer.objects.all()