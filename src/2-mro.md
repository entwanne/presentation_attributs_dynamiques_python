# Method Resolution Order (*MRO*)

## Method Resolution Order

* L'accès à un attribut ne se contente pas d'explorer le `__dict__` de l'objet
* Sont aussi analysés celui du type, et de tous les types parents
* L'ordre d'évaluation des types est défini par le *MRO*

## Method Resolution Order

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


## Method Resolution Order

* On peut connaître le *MRO* d'une classe en faisant appel à sa méthode `mro`

```python
B.mro()
```


## Method Resolution Order

* Celui-ci est surtout utile lors d'héritages multiples, il se base sur l'algorithme C3
* Il permet de linéariser la hiérarchie des classes parentes

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

## Method Resolution Order

```python
object.mro()
```

```python
class A: pass

A.mro()
```

```python
class B(A): pass

B.mro()
```

```python
class C: pass

C.mro()
```

## Method Resolution Order

```python
class D(A, C): pass

D.mro()
```

```python
class E(B, C): pass

E.mro()
```

```python
class F(D, E): pass

F.mro()
```

```python
class G(E, D): pass

G.mro()
```

## *MRO* de l'impossible

```python
class H(A, B): pass
```

```python
class H(B, A): pass

H.mro()
```
