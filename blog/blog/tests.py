from django.test import TestCase
from django.test import Client
from django.urls import reverse
from django.conf import settings

class NonAuthenticationRequiredTemplatesTest(TestCase):
    """
    Tests whether the pages / templates, which doesn't require authentication
    can be accessed by unauthenticated user or not
    """
    c = Client()

    def test_index_page(self):
        """
        Test whether unauthenticated user can access index page
        """
        response = self.c.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
    
    def test_contact_me_page(self):
        """
        Test whether unauthenticated user can access contact me page
        """
        response = self.c.get(reverse("contact-me"))
        self.assertEqual(response.status_code, 200)
    
    def test_login_page(self):
        """
        Test whether unauthenticated user can access login page
        """
        response = self.c.get(reverse("user:login"))
        self.assertEqual(response.status_code, 200)
    
    def test_create_account_page(self):
        """
        Test whether unauthenticated user can access signup page
        """
        response = self.c.get(reverse("user:signup"))
        self.assertEqual(response.status_code, 200)
    
    def test_dashboard_page(self):
        """
        Test whether unauthenticated user can access dashboard page
        """
        response = self.c.get(reverse("post:dashboard"))
        redirection_page = settings.LOGIN_URL
        self.assertEqual(response.status_code, 200)


class AuthenticationRequiredRedirectionTest(TestCase):
    """
    Tests whether the non-authenticated user is redirected to login required page or not
    """

    c = Client()

    def test_view_profile_redirection(self):
        """
        Tests whether the non-authenticated user is redirected to login required page or not 
        when accessing the view profile url
        """
        response = self.c.get("/user/view-profile/")
        self.assertNotEqual(response.status_code, 200)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/user/login/?next=/user/view-profile/")
    
    def test_change_password_redirection(self):
        """
        Tests whether the non-authenticated user is redirected to login required page or not 
        when accessing the change password url
        """
        response = self.c.get("/user/change-password/")
        self.assertNotEqual(response.status_code, 200)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/user/login/?next=/user/change-password/")
