from django.db import models

class Student(models.Model):
    student_name = models.CharField(max_length=200)
    student_email = models.EmailField(unique=True, max_length=200)
    student_password = models.CharField(max_length=200)
    student_active = models.BooleanField(default=True)
    student_pub_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
      return self.student_name

class Category(models.Model):
    category_name = models.CharField(max_length=200)
    category_active = models.BooleanField(default=True)
    category_description = models.CharField(max_length=200)
    category_pub_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
       return self.category_name

class Word(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    word = models.CharField(max_length=200)
    word_pl = models.CharField(max_length=200)
    word_pl_api = models.CharField(max_length=200)
    word_pub_date = models.DateTimeField(auto_now_add=True)
    word_active = models.BooleanField(default=True)
    def __str__(self):
        return self.word

class Phrase(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    phrase = models.CharField(max_length=500)
    phrase_pl = models.CharField(max_length=500)
    phrase_pl_api = models.CharField(max_length=500)
    phrase_pub_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.phrase

class WordCollection(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    word_collection_title = models.CharField(max_length=200)
    word_collection_pub_date = models.DateTimeField(auto_now_add=True)
    word_collection_json = models.JSONField()
    def __str__(self):
        return self.word_collection_title

class PhraseCollection(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    phrase_collection_title = models.CharField(max_length=200)
    phrase_collection_pub_date = models.DateTimeField(auto_now_add=True)
    phrase_collection_json = models.JSONField()
    def __str__(self):
        return self.phrase_collection_title

