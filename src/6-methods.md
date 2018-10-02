# Méthodes

## Méthodes

* Derrière leur apparente simplicité, les méthodes sont en fait des descripteurs
* C'est ce qui explique la différence entre méthodes et *bound methods*

```python
class C:
    def method(self):
        pass

C.method
```

```python
c = C()
c.method
```

## Méthodes

* Une méthode est en alors un descripteur autour d'une fonction
* Ce descripteur réagit différemment suivant si la méthode est accédée depuis la classe ou l'une de ses instances

```python
from functools import partial

class Method:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        if instance is None:
            return self.func
        return partial(self.func, instance)
```

## Méthodes

* Les méthodes de classe fonctionnent de la même manière en utilisant l'`owner`
* Les méthodes statiques sont les plus simples et ne dépendent d'aucun descripteur
