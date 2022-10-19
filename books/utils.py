from .models import Books
from faker import Faker
from random import randint

def create_books(n=10):
    fake = Faker('pl_PL')
    # tworzę obiekt

    for n in range(n):
        created = fake.date_time()
        post = Books(
            title=fake.text(randint(10,30)),
            decription=fake.text(randint(40,100)),
            available=fake.boolean(),
            publication_year= 1925,   #int(fake.year())
            author= fake.text(randint(10,18)) #fake.name()

            # content=fake.text(randint(100,300)),
            # created=created,
            # modified=created + fake.time_delta(10),
            # published= fake.boolean(),
            # sponsored=fake.boolean()
        )
        post.save()
