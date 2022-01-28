from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import fish
from PIL import Image

class TestListCreateFishs(APITestCase):

    def test_creates_fish(self):
        sample_fish = {
            'fishname':'fefes',
            'species':'greg',
            'weight':44.4,
            'length':35.6,
            'latitude':'35.5353',
            'longitude':'54.5336',
            'image':open('./media/pictures/pexels-eberhard-grossgasteiger-1421903.jpg','rb')
        }
        response = self.client.post(reverse('fish'), sample_fish)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

    def test_retrieves_all_fish(self):
        response = self.client.get(reverse('fish'))
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_size_image(self):
        fishs = fish.objects.all()
        for f in fishs:
            img = Image.open(f.image)
            self.assertTrue(img.height<=140 and img.width<=140)

    
