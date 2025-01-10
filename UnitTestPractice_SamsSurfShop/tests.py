# Import packages
import surfshop
import unittest

# Create Test Class
class SurfShopTests(unittest.TestCase):
    # Setup Fixture
    def setUp(self):
        self.cart = surfshop.ShoppingCart()
    
    # Test add_surfboards() method
    def test_add_surfboards(self):
        result = self.cart.add_surfboards(1)
        self.assertEqual(result, 'Successfully added 1 surfboard to cart!')
    
    # Parameterized test for add_surfboards
    def test_add_surfboards_parameterize(self):
        test_list = [2, 3, 4]
        for val in test_list:
            with self.subTest(i=val):
                # Create a new cart for each subtest to avoid cumulative addition
                cart = surfshop.ShoppingCart()
                result = cart.add_surfboards(val)
                suffix = '' if val == 1 else 's'  # Handle pluralization
                self.assertEqual(result, f'Successfully added {val} surfboard{suffix} to cart!')
    
    # Test add_surfboards() again
    def test_add_surfboards_2(self):
        result = self.cart.add_surfboards(2)
        self.assertEqual(result, 'Successfully added 2 surfboards to cart!')
    
    # Test max surfboards with add_surfboards()
    def test_add_surfboards_excess(self):
        with self.assertRaises(surfshop.TooManyBoardsError):
            self.cart.add_surfboards(5)
    
    # Test apply_locals_discount()
    def test_apply_locals_discount(self):
        self.cart.apply_locals_discount()
        self.assertTrue(self.cart.locals_discount)

# Run the tests
if __name__ == '__main__':
    unittest.main()




