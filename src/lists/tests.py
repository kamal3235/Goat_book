from django.test import TestCase
from lists.models import Item, List
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

    # def test_displays_all_list_items(self):
    #     Item.objects.create(text="itemey 1")
    #     Item.objects.create(text="itemey 2")
    #     response = self.client.get("/")
    #     self.assertContains(response, "itemey 1")
    #     self.assertContains(response, "itemey 2")

        # self.assertContains(response, "A new list item")
        # self.assertTemplateUsed(response, "home.html")

    # def test_only_saves_items_when_necessary(self):
    #     self.client.get("/")
    #     self.assertEqual(Item.objects.count(), 0)


class NewItemTest(TestCase):
    def test_can_save_a_POST_request_to_an_existing_list(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()

        self.client.post(
            f"/lists/{correct_list.id}/add_item",
            data={"item_text": "A new item for an existing list"},
        )

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.get()
        self.assertEqual(new_item.text, "A new item for an existing list")
        self.assertEqual(new_item.list, correct_list)

    def test_redirects_to_list_view(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()

        response = self.client.post(
            f"/lists/{correct_list.id}/add_item",
            data={"item_text": "A new item for an existing list"},
        )

        self.assertRedirects(response, f"/lists/{correct_list.id}/")


class NewListTest(TestCase):
    def test_can_save_a_POST_request(self):
        # response = self.client.post("/", data={"item_text": "A new list item"})
        self.client.post("/lists/new", data={"item_text": "A new list item"})
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.get()
        self.assertEqual(new_item.text, "A new list item")

    def test_redirects_after_POST(self):
        response = self.client.post(
            "/lists/new", data={"item_text": "A new list item"})
        new_list = List.objects.get()
        self.assertRedirects(response, f"/lists/{new_list.id}/")


class ListViewTest(TestCase):
    def test_uses_list_template(self):
        mylist = List.objects.create()
        response = self.client.get(f"/lists/{mylist.id}/")
        self.assertTemplateUsed(response, "list.html")

    def test_displays_only_items_for_that_list(self):
        correct_list = List.objects.create()
        Item.objects.create(text="itemey 1", list=correct_list)
        Item.objects.create(text="itemey 2", list=correct_list)
        other_list = List.objects.create()
        Item.objects.create(text="other list item", list=other_list)

        response = self.client.get(f"/lists/{correct_list.id}/")
        self.assertContains(response, "itemey 1")
        self.assertContains(response, "itemey 2")
        self.assertNotContains(response, "other list item")

    def test_passes_correct_list_to_template(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()
        response = self.client.get(f"/lists/{correct_list.id}/")
        self.assertEqual(response.context["list"], correct_list)


class ListAndItemModelsTest(TestCase):
    def test_saving_and_retrieving_items(self):
        mylist = List()
        mylist.save()

        first_item = Item()
        first_item.text = "The first (ever) list item"
        first_item.list = mylist
        first_item.save()

        second_item = Item()
        second_item.text = "Item the second"
        second_item.list = mylist
        second_item.save()

        saved_list = List.objects.get()
        self.assertEqual(saved_list, mylist)

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, "The first (ever) list item")
        self.assertEqual(first_saved_item.list, mylist)
        self.assertEqual(second_saved_item.text, "Item the second")
        self.assertEqual(second_saved_item.list, mylist)