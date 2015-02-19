#!/usr/bin/env python
# This file is part stock_shipment_moves_relate module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import test_depends


class StockShipmentMovesRelateTestCase(unittest.TestCase):
    'Test Stock Shipment Moves Relate module'

    def setUp(self):
        trytond.tests.test_tryton.install_module('stock_shipment_moves_relate')

    def test0006depends(self):
        'Test depends'
        test_depends()


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        StockShipmentMovesRelateTestCase))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
