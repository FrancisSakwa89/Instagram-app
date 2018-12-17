from django.test import TestCase
from .models import Profile, Image, Comment

# Create your tests here.
class ProfileTestClass(TestCase):
  """  
  Tests Profile class and its functions
  """
  def setUp(self):
      self.prof =Profile(photo='test.jpg', bio='test bio')

  def test_instance(self):
      self.assertTrue(isinstance(self.prof, Profile))

  def test_save_method(self):
      """
      Function to test that location is being saved
      """
      self.prof.save_profile()
      profiles = Location.objects.all()
      self.assertTrue(len(profiles) > 0)

  def test_delete_method(self):
      """
      Function to test that a location can be deleted
      """
      self.prof.save_profile()
      self.prof.delete_profile()
      profiles = Profile.objects.all()
      self.assertTrue(len(profiles) == 0)
  
  def test_update_method(self):
      """
      Function to test that a location's details can be updates
      """
      self.prof.save_profile()
      new_prof = Profile.objects.filter(photo='test.jpg').update(photo='new.jpg')
      profiles = Profile.objects.get(photo='new.jpg')
      self.assertTrue(profiles.photo, 'new.jpg')



class ImageTestClass(TestCase):
  """  
  Tests Image class and its functions
  """
  def setUp(self):
      self.img = Image(image='test.jpg',name='test name',caption='test caption')

  def test_instance(self):
      self.assertTrue(isinstance(self.img, Image))

  def test_save_method(self):
      """
      Function to test that location is being saved
      """
      self.img.save_image()
      imgs = Image.objects.all()
      self.assertTrue(len(imgs) > 0)

  def test_delete_method(self):
      """
      Function to test that a location can be deleted
      """
      self.img.save_image()
      self.img.delete_image()
      imgs = Image.objects.all()
      self.assertTrue(len(imgs) == 0)
    
  def test_update_method(self):
      """
      Function to test that a location's details can be updates
      """
      self.img.save_image()
      new_img = Image.objects.filter(name='test').update(name='new')
      imgs = Image.objects.get(name='new')
      self.assertTrue(imgs.name, 'new')



class CommentTestClass(TestCase):
  """  
  Tests Comment Class and its functions
  """
  def setUp(self):
      self.com = Comment(comment='test comment')

  def test_instance(self):
      self.assertTrue(isinstance(self.com, Comment))

  def test_save_method(self):
      """
      Function to test that location is being saved
      """
      self.com.save_comment()
      coms = Comment.objects.all()
      self.assertTrue(len(coms) > 0)

  def test_delete_method(self):
      """
      Function to test that a location can be deleted
      """
      self.com.save_comment()
      self.com.delete_comment()
      comments = Comment.objects.all()
      self.assertTrue(len(comments) == 0)
  
  def test_update_method(self):
      """
      Function to test that a location's details can be updates
      """
      self.com.save_comment()
      new_com = Comment.objects.filter(comment='test comment').update(comment='new comment')
      coms = Comment.objects.get(comment='new comment')
      self.assertTrue(coms.comment, 'new comment')