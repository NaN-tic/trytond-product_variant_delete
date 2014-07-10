# This file is part product_variant_delete module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import PoolMeta

__all__ = ['Product']
__metaclass__ = PoolMeta


class Product:
    __name__ = 'product.product'

    @classmethod
    def __setup__(cls):
        super(Product, cls).__setup__()
        cls._error_messages.update({
                'delete_last_variant': ('Not allow to delete last variant.'),
                })

    @classmethod
    def delete(cls, products):
        for product in products:
            prods = product.template.products
            if len(prods) <= 1:
                cls.raise_user_error('delete_last_variant', (product.rec_name,))
        super(Product, cls).delete(products)
