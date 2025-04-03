import graphene

from graphene_django import DjangoObjectType
from word_and_phrase import models
from word_and_phrase.models import Student


class StudentType(DjangoObjectType):
    class Meta:
        model = models.Student

class CreateStudent(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)
        active = graphene.Boolean(required=True)

    student = graphene.Field(StudentType)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        student = Student.objects.create(
            student_name=kwargs['name'],
            student_email=kwargs['email'],
            student_password=kwargs['password'],
            student_active=kwargs['active'])

        return CreateStudent()

class UpdateStudent(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)
        active = graphene.Boolean(required=True)

    student = graphene.Field(StudentType)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        student = Student.objects.get(pk=kwargs['id'])
        student.student_name = kwargs['name']
        student.student_email = kwargs['email']
        student.student_password = kwargs['password']
        student.student_active = kwargs['active']
        student.save()


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

    def resolve_words_by_student(root, info, studentId):
        return models.Word.objects.filter(student_id=studentId)


class Mutation(graphene.ObjectType):
    create_student = CreateStudent.Field()
    update_student = UpdateStudent.Field()



schema = graphene.Schema(query=Query, mutation=Mutation)