from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class AuthViewsTestCase(TestCase):
    def setUp(self):
        self.username = "pedro"
        self.password = "securepassword123"
        self.user = User.objects.create_user(username = self.username, password = self.password)
        self.login_url = reverse('login')

    def test_login_view_status_code(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')