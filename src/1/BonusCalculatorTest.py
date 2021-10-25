import unittest
from BonusCalculator import SalesRecord


# A testcase is created by subclassing unittest.TestCase.
class BonusCalculatorTest(unittest.TestCase):

    # Tests are defined with methods whose names start with the letters test.
    # This naming convention informs the test runner about which methods represent tests.

    def test_no_bonus_when_sales_equal_quota(self):
        sales_record = SalesRecord(10000, 100, 0)
        sales_record.add_sale(1000)
        bonus = sales_record.calculate_bonus()

        self.assertEqual(bonus, 0)

    def test_bonus_when_sales_greater_than_quota(self):
        sales_record = SalesRecord(10000, 100, 0)
        sales_record.add_sale(12000)
        bonus = sales_record.calculate_bonus()

        self.assertEqual(bonus, 2000)

    def test_bonus_depends_on_commission(self):
        sales_record = SalesRecord(10000, 50, 0)
        sales_record.add_sale(12000)
        bonus = sales_record.calculate_bonus()

        self.assertEqual(bonus, 1000)

    def test_tax_is_applied_on_bonus(self):
        sales_record = SalesRecord(10000, 50, 10)
        sales_record.add_sale(12000)
        bonus = sales_record.calculate_bonus()

        self.assertEqual(bonus, 900)

    def test_bonus_is_calculated_on_total_sales(self):
        sales_record = SalesRecord(10000, 100, 0)
        sales_record.add_sale(5000)
        sales_record.add_sale(6000)

        self.assertEqual(sales_record.calculate_bonus(), 1000)


if __name__ == '__main__':
    unittest.main()
