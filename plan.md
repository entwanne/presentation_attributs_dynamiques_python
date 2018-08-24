# La dynamique des attributs

* Définition et présentation basique d'un attribut
    * a.foo = ...
    * a.foo
    * del a.foo
* Fonctions getattr et hasattr pour récupérer un attribut et tester sa présence
* Fonctions setattr et delattr pour modifier/supprimer un attribut
* object.__dict__, dictionnaire où sont stockés les attributs
* Method resolution order : parcours des __dict__ des ascendants jusqu'à trouver l'attribut (lors d'un get et non d'un set)
* Méthodes __getattr__ et __getattribute__ appelées par getattr/hasattr
    * __getattribute__ est appelée pour tout accès à un attribut
    * Si pas redéfinie, c'est object.__getattribute__ qui est appelée
    * object.__getattribute__ recherche dans le dict de l'object (et des parents -> MRO)
    * __getattr__ est appelée quand l'attribut n'est pas trouvé par __getattribute__
    * elle permet de facilement mettre en place des attributs dynamiques sans se mélanger avec les attributs existant
    * Attention aux récursions infinies avec __getattribute__ (accéder à un attribut de l'objet dans __getattribute__)
* Méthodes __setattr__ et __delattr__
    * Bindings directs de setattr et delattr
    * Attention encore aux récursions infinies
* Propriétés : définition d'attributs dynamiques avec @property
    * Les propriétés sont définies au niveau de la classe et non de l'objet
    * Exemple : gestion d'un cache
    * Exemple : calcul dynamique d'un atribut (aire d'un rectangle)
* Derrière les propriétés : descripteurs
    * Méthodes spéciales __get__, __set__ et __del__
    * Définis au niveau de la classe et récupérés par le __getattribute__ sur un objet, la méthode spéciale appropriée est alors appeler pour en renvoyer le résultat
    * Attributs owner et instance du __get__ (agir selon que l'attribut soit récupéré sur l'instance ou la classe)
    * Méthode __set_name__
* Les méthodes sont des descripteurs : bound methods, @staticmethod, @classmethod
    * Réécriture de @classmethod
* Aparté sur les slots : optimisation du stockage des attributs dans un objet (et limitation, sans __dict__)
    * Les slots sont compatibles avec __getattr__, descripteurs et autres choses vues dans la présentation
* __getattr__ au niveau d'un module (Python 3.7)
