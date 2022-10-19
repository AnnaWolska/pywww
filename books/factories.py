import factory
from factory import post_generation
from faker import Factory

faker = Factory.create()

# class BookFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = "books.Books"
#     @factory.post_generation
#     def authors(self, create, extracted, **kwargs):
#         if not create: return
#         if extracted:
#             for author in extracted:
#                 self.authors.add(author)


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "books.Author"
        django_get_or_create = ("name", "birth_year")

    name = factory.LazyAttribute(lambda x: faker.name())
    birth_year = factory.LazyAttribute(lambda x: faker.date_of_birth().year)
    biogram = factory.LazyAttribute(lambda x: faker.text(200))


class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "books.Books"
        # django_get_or_create = ("title","decription","available","publication_year","author",'tags',"image")

    title = factory.LazyAttribute(lambda x: faker.text(100))
    decription = factory.LazyAttribute(lambda x: faker.text(300))
    # publication_year = factory.LazyAttribute(lambda x:faker.random.randint(1800,1980))
    publication_year = factory.LazyAttribute(lambda x: faker.date_of_birth().year)
    available = factory.LazyAttribute(lambda x: faker.boolean())

    # @factory.post_generation
    # def authors(self, create, extracted, **kwargs):
    #     if not create: return
    #     if extracted:
    #         for author in extracted:
    #             self.authors.add(author)
