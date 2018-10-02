# Method Resolution Order (*MRO*)

## Method Resolution Order (*MRO*)

* L'accès à un attribut ne se contente pas d'explorer le `__dict__` de l'objet
* Sont aussi analysés celui du type, et de tous les types parents
* L'ordre d'évaluation des types est défini par le *MRO*

## Method Resolution Order (*MRO*)

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


## Method Resolution Order (*MRO*)

* On peut connaître le *MRO* d'une classe en faisant appel à sa méthode `mro`

```python
B.mro()
```


## Method Resolution Order (*MRO*)

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
