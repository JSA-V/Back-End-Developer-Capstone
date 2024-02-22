from django.test import TestCase
from restaurant.models import Menu, MenuItem
from restaurant.serializers import MenuSerializer, MenuItemSerializer
from django.urls import reverse

class MenuViewTest(TestCase):
    def setUp(self):
        # Adding test instances of the Menu model
        self.menu1=MenuItem.objects.create(title='Menu 1', price=10.99, featured=True)
        self.menu2=MenuItem.objects.create(title='Menu 2', price=12.99, featured=True)
        self.menu3=MenuItem.objects.create(title='Menu 3', price=9.99, featured=True)

    def test_getall(self):
        # Retrieving all Menu objects added for test purposes
        response = self.client.get(reverse('menu')) 
        menus = MenuItem.objects.all()
        
        # Utilizando MenuSerializer para serializar los objetos Menu
        serializer = MenuItemSerializer(menus, many=True)

        # Comprobando que el código de estado y los datos serializados son los esperados
        self.assertEqual(response.status_code, 200)
        # Asegurándonos de que la respuesta sea igual a los datos serializados
        # Aquí se compara la cadena serializada con la respuesta, ambas en formato JSON
        self.assertEqual(response.data,serializer.data)

