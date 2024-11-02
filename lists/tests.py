from django.test import TestCase
from lists.models import Item
from django.http import HttpRequest
from lists.views import home_page

# Create your tests here.


# class SmokeTest(TestCase):
#     def test_bad_maths(self):
#         self.assertEqual(1 + 1, 3)

# class HomePageTest(TestCase):
#     def test_home_page_returns_correct_html(self):
#         request = HttpRequest()
#         response = home_page(request)
#         html = response.content.decode("utf8")
#         self.assertIn("<title>To-Do lists</title>", html)
#         self.assertTrue(html.startswith("<html>"))
#         self.assertTrue(html.endswith("</html>"))

#     def test_home_page_returns_correct_html_2(self):
#         response = self.client.get("/")
#         self.assertContains(response, "<title>To-Do lists</title>")

# class HomePageTest(TestCase):
#     def test_home_page_returns_correct_html(self):

#         response = self.client.get("/")
#         self.assertContains(response, "<title>To-Do lists</title>")
#         self.assertContains(response, "<html>")
#         self.assertContains(response, "</html>")
#         self.assertTemplateUsed(response, "home.html")

class HomePageTest(TestCase):
    def test_uses_home_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "home.html")

    def test_displays_all_list_items(self):
        Item.objects.create(text="itemey 1")
        Item.objects.create(text="itemey 2")
        response = self.client.get("/")
        self.assertContains(response, "itemey 1")
        self.assertContains(response, "itemey 2")

    def test_can_save_a_POST_request(self):
        # response = self.client.post("/", data={"item_text": "A new list item"})
        self.client.post("/", data={"item_text": "A new list item"})
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, "A new list item")

    def test_redirects_after_POST(self):
        response = self.client.post("/", data={"item_text": "A new list item"})
        self.assertRedirects(response, "/")

        # self.assertContains(response, "A new list item")
        # self.assertTemplateUsed(response, "home.html")

    def test_only_saves_items_when_necessary(self):
        self.client.get("/")
        self.assertEqual(Item.objects.count(), 0)


class ItemModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = "The first (ever) list item"
        first_item.save()

        second_item = Item()
        second_item.text = "Item the second"
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, "The first (ever) list item")
        self.assertEqual(second_saved_item.text, "Item the second")
