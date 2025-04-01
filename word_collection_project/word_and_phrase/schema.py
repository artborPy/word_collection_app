import graphene

from graphene_django import DjangoObjectType
from word_and_phrase import models


class StudentType(DjangoObjectType):
    class Meta:
        model = models.Student

class WordType(DjangoObjectType):
    class Meta:
        model = models.Word

class PhraseType(DjangoObjectType):
    class Meta:
        model = models.Phrase

class WordCollectionType(graphene.ObjectType):
    class Meta:
        model = models.WordCollection

class PhraseCollectionType(graphene.ObjectType):
    class Meta:
        model = models.PhraseCollection

class CategoryType(graphene.ObjectType):
    class Meta:
        model = models.Category


class Query(graphene.ObjectType):
    all_words = graphene.List(WordType)
    words_by_student = graphene.List(WordType, student_id=graphene.Int())

    def resolve_all_words(root, info, **kwargs):
        return models.Word.objects.all()

    def resolve_words_by_student(root, info, id):
        return models.Word.objects.filter(student_id=student_id)




schema = graphene.Schema(query=Query)