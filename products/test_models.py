from django.test import TestCase
from .models import Review, Product


class ReviewModelTestCase(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name='Test Product',
            description='Test Description',
            price=100.00
        )
        self.review = Review.objects.create(
            product=self.product,
            author='Test Author',
            content='Test Content',
            rating=5
        )

    def test_review_str_representation(self):
        self.assertEqual(str(self.review), self.product.name)

    def test_review_saving_and_retrieving(self):
        reviews = Review.objects.all()
        self.assertEqual(reviews.count(), 1)
        self.assertEqual(reviews[0], self.review)
