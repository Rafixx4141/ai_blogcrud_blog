import os
import django
from faker import Faker
import random

# Konfiguracja środowiska Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ai_blogcrud_blog.settings')
django.setup()

from crud_blog_web.models import Article

def populate(N=100):
    fake = Faker()
    for _ in range(N):
        title = fake.sentence(nb_words=6)
        # content = fake.text(max_nb_chars=2000)  # Usunięte, ponieważ nie ma takiego pola
        year = random.randint(1990, 2021)

        # Tworzenie nowego rekordu Article
        article = Article(title=title, year=year)
        article.save()

if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(100)  # Wpisz liczbę artykułów, które chcesz wygenerować
    print('Populating Complete')
