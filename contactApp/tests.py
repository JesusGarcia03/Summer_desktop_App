from django.test import TestCase
from .models import Record, Post

# Create your tests here.

#python manage.py test myapp

class RecordModelTest(TestCase):

	self.record = Record.objects.create(
		frist_name = "John",
		last_name = "Johnson",
		email = "jj@johnson@gmail.com",
		phone = "9567777777"

		)
	def test_record_creation(self):
		self.assertEqual(self.record.first_name."John")
		self.assertEqual(self.record.last_name."Johnson")
		self.assertEqual(self.record.email."jj@johnson@gmail.com")
		self.assertEqual(self.record.phone."9657777777")
