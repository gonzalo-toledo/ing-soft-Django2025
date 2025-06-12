from django.apps import AppConfig


class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'

    #los signals se configuran en el apps.py
    def ready(self):
        """
        Metodo que se ejecuta cuando la app está lista (app producto en este caso)
        Importar aqui los signasl evita problams de importacion circular
        """
        from products import signals #importo todos los signals, pero se podria importar uno por uno
        return super().ready