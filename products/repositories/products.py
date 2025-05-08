from products.models import Product

class ProductRepository:
    """
    clase de repositorio que se encargará de conectarse con la db para manipular productos
    """
    
    @staticmethod    
    def create(
        name:str, 
        price:float,
        description:str, 
        stock:int
    ) -> Product:
        """
        Crea un object (Producto)
        """
        return Product.objects.create(
            name=name, 
            price=price, 
            description=description,
            stock=stock,
        ) 
    
    @staticmethod
    def delete(product:Product) -> bool:
        try:
            product.delete() #!lo cambie!!! preguntar a MAti porque tenia Product
        except Product.DoesNotExist:
            raise ValueError("El producto no existe")
    
    
    # @staticmethod
    # def delete(product_id) -> bool:
    #     try:
    #         Product.objects.get(id=product_id).delete()
    #     except Product.DoesNotExist:
    #         raise ValueError("El producto no existe")
        
        
    @staticmethod    
    def update(
        product: Product, 
        price:float,
        description:str, 
        stock:int, 
    ) -> Product:
        """
        Modifica un object (Producto)
        """
        product.price = price
        product.description = description
        product.stock = stock
        product.save() #guarda
        
        return product
    
    
    @staticmethod
    def get_all() -> list[Product]:
        """
        Obtiene todos los objects (Productos)
        """
        return Product.objects.all()


    @staticmethod    
    def get_by_id(product_id:int) -> Product:
        """
        Obtiene un object (Producto) por su id
        """
        try:
            return Product.objects.get(id=product_id)
        except Product.DoesNotExist: #si no lo encuentra
            # return None #no retorna nada pero no se rompe
            raise ValueError("El producto no existe")
        
    
    @staticmethod
    def search_by_name(name:str) -> list[Product]:
        """
        Busca un object (Producto) que contenga parte  del nombre ingresado
        """
        return Product.objects.filter(name__icontains=name)
        #############################(atributo__que contenga__cadena que le paso )
        
        
    @staticmethod
    def filter_by_price_range(min_price:float, max_price:float) -> list[Product]:
        """
        Retorna un listado de productos cuyo precio este entre min_price y max_price
        """
        return Product.objects.filter(price__range=(min_price, max_price)) #range incluye los extremos igual que gte y lte
        # return Product.objects.filter(price__gte=min_price, price__lte=max_price)