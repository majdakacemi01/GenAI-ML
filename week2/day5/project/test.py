# create_blogs.py
from blog import Blog
from db import init_db

# Make sure table exists
init_db()

# List of blog data
blogs_data = [
    {"title": "Bonjour le monde", "content": "Ceci est le premier article du blog. Nous testons la traduction et le TTS."},
    {"title": "Python Tips", "content": "Python is a powerful programming language. This blog post shares some useful tips."},
    {"title": "Recette de crêpes", "content": "Pour faire des crêpes, vous aurez besoin de farine, lait, œufs et sucre. Mélangez bien."},
    {"title": "Travel Guide: Paris", "content": "Paris is the city of lights. Visit the Eiffel Tower, Louvre, and enjoy French cuisine."},
    {"title": "Healthy Eating", "content": "Eating fruits and vegetables daily is essential for good health. Drink plenty of water too."},
    {"title": "Technologie et Futur", "content": "La technologie avance rapidement et change notre quotidien de manière spectaculaire."},
    {"title": "Learn Flask", "content": "Flask is a lightweight web framework for Python. It is easy to learn and very flexible."},
    {"title": "Le Chat et le Chien", "content": "Le chat est curieux et agile, tandis que le chien est fidèle et protecteur."},
    {"title": "Meditation Tips", "content": "Meditation can help reduce stress and improve focus. Practice daily for best results."},
    {"title": "Voyage au Maroc", "content": "Le Maroc est un pays riche en culture, avec des paysages magnifiques et une cuisine délicieuse."}
]


# Create Blog instances using map + lambda
blogs = list(map(lambda data: Blog(title=data["title"], content=data["content"]), blogs_data))

# Save blogs using a for loop
for b in blogs:
    b.save()
    print(f"Created blog: {b.to_dict()}")
