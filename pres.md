# La dynamique des attributs
## Antoine Rozo

```python-skip
# Base object
class Obj:
    pass
obj = Obj()
```

# Attributs en Python

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

```python
obj.__dict__
```

# Method Resolution Order (*MRO*)

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

```python
B.mro()
```

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

# Méthodes spéciales `__setattr__` et `__delattr__`

# Propriétés

* Décorateur `@property`

# Descripteurs

# Méthodes

# Slots

# Python 3.7 : Module et `__getattr__`
