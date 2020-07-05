# This file is part product_variant_delete module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import PoolMeta
from trytond.i18n import gettext
from trytond.exceptions import UserError

__all__ = ['Product']


class Product(metaclass=PoolMeta):
    __name__ = 'product.product'

    @classmethod
    def delete(cls, products):
        for product in products:
            prods = product.template.products
            if len(prods) <= 1:
                raise UserError(
                    gettext('product_variant_delete.msg_delete_last_variant',
                    product=product.rec_name))
        super(Product, cls).delete(products)
