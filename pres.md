# La dynamique des attributs
## Antoine Rozo

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

# Fonctions `getattr` et `hasattr`

* Ces opérations élémentaires sont accessibles depuis des fonctions

```python
hasattr(obj, 'bar')
```

```python
obj.bar = 5
```

```python
getattr(obj, 'bar')
```

# Fonctions `setattr` et `delattr`

```python
setattr(obj, 'bar', 10)
```

```python
delattr(obj, 'bar')
```

# Attribut `__dict__`

* Les données stockées dans un objet le sont dans un dictionnaire `__dict__`

```python
obj.__dict__
```

# Method Resolution Order (*MRO*)

* L'accès à un attribut ne se contente pas d'explorer le `__dict__` de l'objet
* Sont aussi analysés celui du type, et de tous les types parents
* L'ordre d'évaluation des types est défini par le *MRO*

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

* On peut connaître le *MRO* d'une classe en faisant appel à sa méthode `mro`

```python
B.mro()
```

* Celui-ci est surtout utile lors d'héritages multiples, il se base sur l'algorithme C3

```python
class P1:
    foo = 'P1.foo'

class P2:
    foo = 'P2.foo'
    bar = 'P2.bar'

class C(P1, P2):
    pass

C.foo, C.bar
```

```python
C.mro()
```

# Méthodes spéciales `__getattr__` et `__getattribute__`

* Des méthodes spéciales sont impliquées dans la recherche des attributs d'un objet
* Lors de l'accès à un attribut, la méthode `__getattribute__` est appelée
* C'est celle-ci qui s'occupe par défaut d'explorer les dictionnaires d'attributs

* `__getattr__` est appelée lorsqu'un attribut n'est pas trouvé par `__getattribute__`

# Méthodes spéciales `__setattr__` et `__delattr__`

# Propriétés

* Décorateur `@property`

# Descripteurs

# Méthodes

# Slots

# Python 3.7 : Module et `__getattr__`
