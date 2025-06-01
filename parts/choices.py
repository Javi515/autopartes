# parts/choices.py

from .models import Automake, Category

# Inicializamos category_choices como diccionario vacío
category_choices = {}
try:
    # Solo intentamos llenar la lista si la tabla ya existe
    for category in Category.objects.all():
        category_choices.setdefault(category.name, category.name)
except Exception:
    # Si falla (p. ej. la tabla no existe), dejamos el diccionario vacío
    category_choices = {}

# Inicializamos automake_choices como diccionario vacío
automake_choices = {}
try:
    for automake in Automake.objects.all():
        automake_choices.setdefault(automake.name, automake.name)
except Exception:
    automake_choices = {}

# price_choices y count_choices se pueden mantener estáticos tal cual
price_choices = {
    '10': 10,
    '100': 100,
    '500': 500,
    '1000': 1000,
    '5000': 5000,
    '10000': 10000
}

count_choices = {
    '1': 1,
    '5': 5,
    '10': 10,
    '20': 20,
    '50': 50,
    '100': 100
}
