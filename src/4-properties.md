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

## Propriétés en lecture seule

* Le *getter* peut être implémenté sans le *setter*

```python
class Rect:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    @property
    def perimeter(self):
        return 2 * (self.width + self.height)
    @property
    def area(self):
        return self.width * self.height

rect = Rect(10, 20)
```

```python
rect.perimeter
```

```python
rect.area
```
