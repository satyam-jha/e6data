from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from blog.models import CustomUser, Blog
from blog.serializer import CustomUserSerializer, BlogSerializer


class RegistrationViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse('registration_view')

    def test_registration_view(self):
        data = {'first_name': 'testuser', 'email': 'test@example.com', 'password': 'testpassword'}
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('token' in response.data)
        # You may add more assertions here to test the response data


class BlogApiViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.blog_list_url = reverse('blog_list_view')

    def test_blog_list_view(self):
        # Assuming authentication is not required for blog listing
        response = self.client.get(self.blog_list_url)
        self.assertEqual(response.status_code, 200)
        # You may add more assertions here to test the response data


class BlogDetailApiViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create(first_name='testuser', email='test@example.com')
        self.blog = Blog.objects.create(title='Test Blog', content='Test Content', author=self.user)
        self.blog_detail_url = reverse('blog_detail_view', kwargs={'pk': self.blog.pk})

    def test_blog_detail_view(self):
        # Assuming authentication is not required for blog detail view
        response = self.client.get(self.blog_detail_url)
        self.assertEqual(response.status_code, 200)
        # You may add more assertions here to test the response data


# You may add more test cases as needed for different scenarios
