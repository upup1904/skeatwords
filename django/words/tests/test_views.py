from django.test import TestCase, Client
from django.urls import reverse

from words import  views

class ExTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_hi_says_hi(self):
        response = self.client.get(reverse('hi'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'hi')
        


    def test_hi_times_says_hi_multiple_times(self):
        url = ''.join(reverse('hitimes', kwargs={'times': 2}))
        response = self.client.post(url)
        print(url)
        self.assertEqual(response.content, b'hihi')

    def test_hi_is_quiet_zero_times(self):
        url = ''.join(reverse('hitimes', kwargs={'times': 0}))
        response = self.client.post(url)
        print(url)
        self.assertEqual(response.content, b'')

    def test_hi_prints_name_with_to(self):
        url = reverse('hi') 
        response = self.client.get(url, data={'to': 'mary'})
        self.assertEqual(response.content, b'hi mary')
