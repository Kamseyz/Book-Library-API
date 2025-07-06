from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator
# Create your models here.

User = get_user_model()



#Category model
class Category(models.Model):
    name = models.CharField(max_length=50, blank= False, null= False,
                            validators=[RegexValidator(regex=r'^[^\s].*', message= "Category name cannot begin with a space"), 
                                        MinLengthValidator(3, message="Category name must be greater than 3 character"), 
                                        MaxLengthValidator(50, message="Category name cannot be greater than 50 character")])
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='categories', default='')

    
    def __str__(self):
        return f'{self.name}'
    
    
#Book model
class Book(models.Model):
    author = models.CharField(max_length=100, blank= False, null= False,
                            validators=[RegexValidator(regex=r'^[^\s].*', message= "Author name cannot begin with a space"), 
                                        MinLengthValidator(3, message="Author name must be greater than 3 character"), 
                                        MaxLengthValidator(100, message="Author name cannot be greater than 100 character")]) 
    
    
    title = models.CharField(max_length=100, blank= False, null= False,
                            validators=[RegexValidator(regex=r'^[^\s].*', message= "Title cannot begin with a space"), 
                                        MinLengthValidator(3, message="Title must be greater than 3 character"), 
                                        MaxLengthValidator(100, message="Title cannot be greater than 100 character")])
    
    
    book_file = models.FileField(upload_to='book_file/', blank=False)
    
    
    category =  models.ForeignKey(Category, on_delete=models.CASCADE)
    
    
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__ (self):
        return f"{self.posted_by} posted a book called {self.title} which belong to the category {self.category} to see the book file find it here{self.book_file}"

