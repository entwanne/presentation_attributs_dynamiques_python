# Descripteurs

## Descripteurs

* Les propriétés sont un sous-ensemble des descripteurs
* Un descripteur est un objet spécial qui permet de régir le comportement d'un attribut
* Il possède pour cela des méthodes `__get__`, `__set__` et `__delete__`

## Descripteurs

* Le descripteur est instancié une seule fois pour toute la classe
* Ses méthodes spéciales sont appelées lors des différents accès à l'attribut
* L'objet duquel on accède à l'attribut est alors passé en paramètre

## Descripteurs

```python
class Fahrenheit:
    def __get__(self, instance, owner):
        return instance.celsius * 1.8 + 32

    def __set__(self, instance, value):
        instance.celsius = (value - 32) / 1.8

class Temperature:
    def __init__(self, celsius=0):
        self.celsius = 0

    fahrenheit = Fahrenheit()

t = Temperature()
t.fahrenheit = 100
t.celsius
```

## Méthode `__get__` des descripteurs

* Quel est donc ce paramètre `owner` de la méthode `__get__` ?
* Un descripteur peut-être récupéré depuis la classe et non depuis une instance de cette classe
* Dans ce cas, le paramètre `instance` vaudra `None`, et `owner` référence toujours la classe utilisée

## Méthode `__get__` des descripteurs

```python
class Descriptor:
    def __get__(self, instance, owner):
        if instance is None:
            return f'Attribute of class {owner}'
        return f'Attribute of {instance}'

class C:
    attr = Descriptor()

C.attr
```

```python
obj = C()
obj.attr
```

## Descripteurs

* Ce comportement n'est valable que pour le `__get__`
* En effet, la redéfinition et la suppression de l'attribut de classe doivent toujours être possibles

```python
C.attr = 'foo'
```

```python
del C.attr
```

## Méthode `__set_name__`

* Depuis Python 3.6, les descripteurs peuvent aussi comporter une méthode `__set_name__` appelée lorsqu'ils sont définis dans une classe

```python
class cachedescriptor:
    def __init__(self, func):
        self.func = func

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, inst, owner):
        if inst is None:
            return self
        if self.name not in inst.__dict__:
            inst.__dict__[self.name] = self.func(inst)
        return inst.__dict__[self.name]
```

## Méthode `__set_name__`

```python
class Calculation:
    @cachedescriptor
    def result(self):
        print('Complex calculation')
        ...
        return 0

calc = Calculation()
```

```python
calc.result
```

## Propriétés

* Implémentation simple des propriétés (ne gère pas l'utilisation en décorateurs)

```python
class my_property:
    def __init__(self, fget, fset, fdel):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
    def __get__(self, instance, owner):
        return self.fget(instance)
    def __set__(self, instance, value):
        return self.fset(instance, value)
    def __delete__(self, instance):
        return self.fdel(instance)
```
