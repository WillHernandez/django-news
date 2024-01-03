from django.test import TestCase, SimpleTestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your tests here.
class HomePageTests(SimpleTestCase):
    def test_homepage_status_code(self):
        res = self.client.get('/')
        self.assertEqual(res.status_code, 200)
    def test_view_url_by_name(self):
        res = self.client.get(reverse('home'))
        self.assertEqual(res.status_code, 200)
    def test_view_uses_correct_template(self):
        res = self.client.get(reverse('home'))
        self.assertTemplateUsed(res, 'home.html')

class SignupPageTests(TestCase):
    def test_signup_status_code(self):
        res = self.client.get('/accounts/signup/')
        self.assertEqual(res.status_code, 200)
    def test_view_url_by_name(self):
        res = self.client.get(reverse('signup'))
        self.assertEqual(res.status_code, 200)
    def test_view_uses_correct_template(self):
        res = self.client.get(reverse('signup'))
        self.assertTemplateUsed(res, 'registration/signup.html')
    def test_signup_form(self):
        username = 'testuser'
        email = 'testuser@email.com'
        get_user_model().objects.create_user(username, email) # create a new test-user
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, username)
        self.assertEqual(get_user_model().objects.all()[0].email, email)