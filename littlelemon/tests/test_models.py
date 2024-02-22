from django.test import TestCase
from restaurant.models import MenuItem

class MenuTest(TestCase):
    def test_get_item(self):
        item= MenuItem.objects.create(title="IceCream",price=80,featured=True)
        itemstr=item.get_item()
        self.assertEqual(itemstr, "IceCream : 80")
