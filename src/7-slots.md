# Slots

## Slots

* Tous les objets ne possèdent pas de `__dict__`
* Il est possible d'optimiser le stockage des attributs en définissant des slots au niveau de la classe
* Cela évite l'instanciation d'un dictionnaire mais empêche de définir des attributs non déclarés

```python
class Point:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y
```

```python
p = Point(3, 4)
p.x, p.y
```

```python
p.z = 1
```

## Slots

* Les classes utilisant des slots restent compatibles avec les mécanismes d'attributs dynamiques

```python
class Point:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def distance(self):
        return (self.x**2 + self.y**2)**0.5

p = Point(3, 4)
p.distance
```
