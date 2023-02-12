from django.test import TestCase
from .models import Product, Category, Review
from .forms import ReviewForm


class ReviewFormTestCase(TestCase):
    def setUp(self):
        # Create a test product
        self.product = Product.objects.create(
            name='Test Product',
            description='This is a test product',
            price=10.00
        )

        # Create a test category
        self.category = Category.objects.create(
            name='Test Category',
            friendly_name='Test Category Friendly Name'
        )

    def test_valid_form(self):
        # Create a test review
        review = Review.objects.create(
            author='Test Author',
            content='This is a test review',
            rating=5,
            product=self.product
        )
        form = ReviewForm(data={
            'author': review.author,
            'content': review.content,
            'rating': review.rating
        })
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = ReviewForm(data={
            'author': '',
            'content': '',
            'rating': ''
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)
