# La dynamique des attributs
## Antoine Rozo

# La dynamique des attributs

* Comprendre le stockage et l'accès aux attributs en Python
* Mettre en place des attributs dynamiques sur nos objets

```python skip
# Base object
class Obj:
    pass
obj = Obj()
```

# Attributs en Python

* Les attributs permettent d'associer des données à un objet

```python
obj.attr = 'foo'
```

```python
obj.attr
```

```python
del obj.attr
```

# Fonctions `getattr`, `setattr` et `delattr`

* Ces opérations élémentaires correspondent à des fonctions Python

```python
getattr(obj, 'bar')
```

```python
setattr(obj, 'bar', 10)
```

```python
delattr(obj, 'bar')
```

# Fonctions `hasattr`

* Une fonction supplémentaire permet de tester la présence d'un attribut

```python
hasattr(obj, 'bar')
```

# Stockage des attributs

* Les objets Python possèdent un attribut spécial, `__dict__`
* Il s'agit d'un dictionnaire qui stocke toutes les données de l'objet

```python
obj.__dict__
```

* Ce dictionnaire est utilisé lors de l'accès à un attribut

```python
obj.__dict__['attr']
```

# Method Resolution Order (*MRO*)

* L'accès à un attribut ne se contente pas d'explorer le `__dict__` de l'objet
* Sont aussi analysés celui du type, et de tous les types parents
* L'ordre d'évaluation des types est défini par le *MRO*

--------------------

```python
class A:
    foo = 'A.foo'
    bar = 'A.bar'
    baz = 'A.baz'

class B(A):
    bar = 'B.bar'

b = B()
b.baz = 'b.baz'

b.foo, b.bar, b.baz
```

--------------------

* On peut connaître le *MRO* d'une classe en faisant appel à sa méthode `mro`

```python
B.mro()
```

--------------------

* Celui-ci est surtout utile lors d'héritages multiples, il se base sur l'algorithme C3

```python
class P1:
    foo = 'P1.foo'

class P2:
    foo = 'P2.foo'
    bar = 'P2.bar'

class C(P1, P2):
    pass

C.mro()
```

```python
C.foo, C.bar
```

# Méthodes spéciales `__getattr__` et `__getattribute__`

* Des méthodes spéciales sont impliquées dans la recherche des attributs d'un objet
* Lors de l'accès à un attribut, la méthode `__getattribute__` est appelée
* C'est celle-ci qui s'occupe par défaut d'explorer les dictionnaires d'attributs

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

--------------------

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

--------------------

* `__getattr__` est appelée lorsqu'un attribut n'est pas trouvé par `__getattribute__`
* Elle est à privilégier pour gérer des attributs dynamiques en plus des existants

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

# Méthodes spéciales `__setattr__` et `__delattr__`

* Ces méthodes sont appelées respectivement pour l'écriture et la suppression d'un attribut
* Elles sont appelées dans tous les cas, pour tous les attributs

```python
class Temperature:
    def __init__(self, celsius=0):
        self.celsius = celsius

    def __getattr__(self, name):
        if name == 'fahrenheit':
            return self.value * 1.8 + 32
        raise AttributeError(name)

    def __setattr__(self, name, value):
        if name == 'fahrenheit':
            self.celsius = (value - 32) / 1.8
        else:
            super().__setattr__(name, value)

t = Temperature()
t.fahrenheit = 30
t.celsius
```

* Attention encore aux récursions infinies

# Propriétés

* Les propriétés permettent de simplifier l'usage d'attributs dynamiques

* Décorateur `@property`

# Descripteurs

# Méthodes

# Slots

# Python 3.7 : Module et `__getattr__`
