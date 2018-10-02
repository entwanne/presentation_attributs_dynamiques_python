# Méthodes spéciales liées aux attributs

## `__getattr__` et `__getattribute__`

* Des méthodes spéciales sont impliquées dans la recherche des attributs d'un objet
* Lors de l'accès à un attribut, la méthode `__getattribute__` est appelée
* C'est celle-ci qui s'occupe par défaut d'explorer les dictionnaires d'attributs

## `__getattr__` et `__getattribute__`

```python
class Temperature:
    def __init__(self, celsius=0):
        self.celsius = celsius

    def __getattribute__(self, name):
        print(f"Récupération de l'attribut {name}")
        if name == 'fahrenheit':
            return self.celsius * 1.8 + 32
        return super().__getattribute__(name)

t = Temperature(25)
t.celsius
```

```python
t.fahrenheit
```

## Pièges de `__getattribute__`

* Attention aux cas de récursions infinies

```python
class WTF:
    def __getattribute__(self, name):
        return self.__dict__[name]

wtf = WTF()
wtf.foo = 0
```

```python
wtf.foo
```

## `__getattr__` et `__getattribute__`

* `__getattr__` est appelée lorsqu'un attribut n'est pas trouvé par `__getattribute__`
* Elle permet plus facilement de gérer des attributs dynamiques en plus des existants

```python
class Temperature:
    def __init__(self, celsius=0):
        self.celsius = celsius

    def __getattr__(self, name):
        if name == 'fahrenheit':
            return self.celsius * 1.8 + 32
        raise AttributeError(name)

t = Temperature(25)
t.celsius
```

```python
t.fahrenheit
```

## `__setattr__` et `__delattr__`

* Ces méthodes sont appelées respectivement pour l'écriture et la suppression d'un attribut
* Elles sont appelées dans tous les cas, pour tous les attributs

## `__setattr__` et `__delattr__`

```python
class Temperature:
    def __init__(self, celsius=0):
        self.celsius = celsius

    def __getattr__(self, name):
        if name == 'fahrenheit':
            return self.celsius * 1.8 + 32
        raise AttributeError(name)

    def __setattr__(self, name, value):
        if name == 'fahrenheit':
            self.celsius = (value - 32) / 1.8
        else:
            super().__setattr__(name, value)

t = Temperature()
t.fahrenheit = 100
t.celsius
```

## Pièges de `__setattr__`

* Attention encore aux récursions infinies

```python
class WTF:
    def __setattr__(self, name, value):
        super().__setattr__(name, value)
        self.last_attribute_modified = name

wtf = WTF()
wtf.foo = 0
```

## Pièges de `__setattr__`

* Et aux appels par l'initialiseur

```python
class WTF:
    def __init__(self, path, prefix=''):
        self.path = path
        self.prefix = prefix

    def __setattr__(self, name, value):
        if name == 'path':
            self.path = value + self.suffix
        else:
            super().__setattr__(self, name, value)

wtf = WTF('foo', '/tmp/')
```

## Méthodes spéciales liées aux attributs

* En raison des potentiels bugs décrits précédemment, évitez au maximum d'avoir recours à ces méthodes
* Elles sont de plus complexes à utiliser car nécessitent de traiter tous les attributs un à un
* Heureusement Python nous offre d'autres facilités pour gérer des attributs dynamiques
