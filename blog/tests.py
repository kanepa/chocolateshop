from django.test import TestCase
from django.core.urlresolvers import resolve
from views import post_detail

# Create your tests here.
from .models import Post


class PostTests(TestCase):
    def test_str(self):
        test_title = Post(title='My Prefect Brownie')
        self.assertEqual(str(test_title),
                         'My Prefect Brownie')




# Create your tests here.
