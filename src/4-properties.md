# Propriétés

## Propriétés

* Les propriétés permettent de simplifier l'usage d'attributs dynamiques
* Elles associent des fonctions de récupération, de modification et de suppression à un nom d'attribut
* On associe une propriété à un nom d'attribut en la définissant comme attribut de classe

## Propriétés

```python
class Temperature:
    def __init__(self, celsius=0):
        self.celsius = celsius

    def _get_fahrenheit(self):
        return self.celsius * 1.8 + 32

    def _set_fahrenheit(self, value):
        self.celsius = (value - 32) / 1.8

    fahrenheit = property(_get_fahrenheit, _set_fahrenheit)

t = Temperature()
t.fahrenheit = 100
t.celsius
```

## Décorateur `@property`

* `property` peut aussi s'utiliser comme un décorateur
* Le nom de l'attribut découle alors du nom du *getter*

```python
class Temperature:
    def __init__(self, celsius=0):
        self.celsius = celsius

    @property
    def fahrenheit(self):
        return self.celsius * 1.8 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) / 1.8

t = Temperature()
t.fahrenheit = 100
t.celsius
```
