from django.test import SimpleTestCase
from django.urls import reverse


# Create your tests here.

class HomepageTest(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse('home_page'))
        self.assertEqual(response.status_code, 200)

    def test_template_content(self):  # new
        response = self.client.get(reverse("home_page"))
        self.assertContains(response, "<h1>Home Page</h1>")


class AboutpageTest(SimpleTestCase):
    def test_url_exist_at_correct_location(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_template_content(self):  # new
        response = self.client.get(reverse("about"))
        self.assertContains(response, "<h1>About pages</h1>")
