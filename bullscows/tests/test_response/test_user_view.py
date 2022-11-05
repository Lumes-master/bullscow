from django.test import Client, TestCase
from django.shortcuts import redirect

class Testview(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.home_url = redirect("/")
