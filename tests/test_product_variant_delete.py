#!/usr/bin/env python
# This file is part product_product module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import test_view, test_depends


class ProductVariantDeleteCase(unittest.TestCase):
    'Test Product Variant Delete module'

    def setUp(self):
        trytond.tests.test_tryton.install_module('product_variant_delete')

    def test0006depends(self):
        'Test depends'
        test_depends()


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        ProductVariantDeleteCase))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
