from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):

    def setUp(self):
        Menu.objects.create(title="Pizza", price=80, inventory=100)
        Menu.objects.create(title="Burger", price=50, inventory=200)

    def test_getall(self):
        items = Menu.objects.all()
        serialized = MenuSerializer(items, many=True)

        self.assertEqual(serialized.data[0]["title"], "Pizza")
        self.assertEqual(serialized.data[1]["title"], "Burger")