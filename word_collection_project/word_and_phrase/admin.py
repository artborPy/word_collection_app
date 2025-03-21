from django.contrib import admin
from word_and_phrase.models import Word, WordCollection, Phrase, PhraseCollection, Category, Student

admin.site.register(Word)
admin.site.register(WordCollection)
admin.site.register(Phrase)
admin.site.register(PhraseCollection)
admin.site.register(Category)
admin.site.register(Student)
