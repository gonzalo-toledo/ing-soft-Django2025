from products.models import Customer
from products.repositories.customers import CustomerRepository

class CustomerService:
    @staticmethod
    def get_all() -> list[Customer]:
        return CustomerRepository.get_all()