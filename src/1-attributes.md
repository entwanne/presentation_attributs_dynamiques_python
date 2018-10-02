# Attributs en Python

## Attributs en Python

* Les attributs permettent d'associer des données à un objet

```python
dana.attr = 10
```

```python
dana.attr
```

```python
del dana.attr
```

## Fonctions `setattr`, `getattr` et `delattr`

* Ces opérations élémentaires correspondent à des fonctions Python

```python
setattr(dana, 'foo', 'bar')
```

```python
getattr(dana, 'foo')
```

```python
delattr(dana, 'foo')
```

## Fonction `hasattr`

* Une fonction supplémentaire permet de tester la présence d'un attribut

```python
hasattr(dana, 'foo')
```

## Stockage des attributs

* Les objets Python possèdent un attribut spécial, `__dict__`
* Il s'agit d'un dictionnaire qui stocke toutes les données de l'objet

```python
dana.__dict__
```

* Ce dictionnaire est utilisé lors de l'accès à un attribut

```python
dana.__dict__['foo']
```
