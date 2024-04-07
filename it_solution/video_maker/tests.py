from django.test import TestCase
from .models import Request
# Create your tests here.


class RequestModelTestCase(TestCase):


    def setUp(self):
        print('-'*20)
        print("Start setUp")
        Request.objects.create(message="123")
        Request.objects.create(message="52")
        print("Finish setUp\n")

    def test_requests_get_all_records(self):
        print('Start test_requests_get_all_records')
        movie = Request.objects.all()
        self.assertEqual(len(movie), 2)
        print('Finish test_requests_get_all_records\n')

    def test_request_delete(self):
        print("Start test_request_delete")
        open = Request.objects.get(message='52')
        open.delete()
        requests = Request.objects.all()
        self.assertEqual(len(requests), 1)
        print("Finish test_request_delete\n")

    def test_request_create(self):
        print("Start test_request_delete")
        open = Request.objects.get(message='52')
        open.delete()
        requests = Request.objects.all()
        self.assertEqual(len(requests), 1)
        print("Finish test_request_delete\n")


class TestHome(TestCase):
    # Проверка главной страницы
    def test_homepage(self):
        print("Start test_homepage")
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        print("Finish test_homepage\n")


