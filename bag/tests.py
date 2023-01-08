from django.test import TestCase

# Create your tests here.


class TestViews(TestCase):

    """
    tests that the view_bag view is rendering
    the correct template
    """

    def test_get_view_bag(self):
        response = self.client.get('/bag/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')
