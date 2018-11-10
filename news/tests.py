from django.test import TestCase
from .models import Editor,Article, tags


# Create your tests here.
class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.sly= Editor(first_name = 'sly', last_name ='elkwal', email ='sly@moringaschool.com')

    #test instance
    def test_instance(self):
      self.assertTrue(isinstance(self.sly,Editor))
       
    #save method
    def test_save_method(self):
      self.sly.save_editor()
      editors = Editor.objects.all()
      self.assertTrue(len(editors) > 0 )

