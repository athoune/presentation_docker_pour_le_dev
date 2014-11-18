!SLIDE

#Éditeur

Les développeurs sont gentils, mais ils ont besoin de leur petit confort.

Leur petit éditeur, ou leur gros IDE.

#Runtime

Les technos intéressantes sont cross-plateforme, .NET par exemple.

Elles sont une simple recompilation de la version Linux qui tournera en prod,
ou une infâme boite noire intégré à l'IDE, ou pire, dans un clicodrome.

!SLIDE
#Mise en prod

On dépose le laptop qui est tombé en marche dans un rack du datacenter et c'est marre.

![Rack OLPC](img_2331.jpg)

!SLIDE
#LAMP est mort

Un site web, c'est un peu de code s'appuyant sur des services (persistance, cache, stockage…).

Un peu de front aussi, HTML5 et ses amis, mais c'est un autre métier.

La cible n'est plus l'hébergement gratos de Free.fr.

Cela fait longtemps que l'application est sortie du serveur web.

De toute façon, une partie du traitement est maintenant asynchrone, détachée.

Varnish, Memcache, S3, Redis, Elasticsearch … ne sont pas des technologies exotiques.

Pour les services tiers, tout le monde connait Google analytics, New Relic, Mollom,

ou pour les rebelles, Piwik, Boomerang, Sentry…

!SLIDE
#Bootstrap et configurations

Un nouveau dev doit pouvoir commencer à voir des choses sur sa machine, une heure après avoir démarré.

Des tests doivent pouvoir être lancés dans un environnement maitrisé.

Le chef de projet doit pouvoir valider tout ce bazar.

Le client doit pouvoir admirer ce qu'il a payé.

Le site doit pouvoir accueillir des visiteurs, pleins de visiteurs, mais sans IE6.

!SLIDE
#La virtualisation a failli

Vagrant n'est pas arrivé à sauver Virtualbox. Trop bleeding edge, trop gourmand.

Le provisioning n'est pas dimensionné pour les dev, c'est la chasse gardée du devops.

Je n'aime ni Capistrano ni Fabric.

!SLIDE
#Docker

!SLIDE
#Docker est indolore

C'est du golang sans dépendance, et il fonctionne étonnamment bien dans un virtualbox.

Il fonctionne en client/serveur.

#Docker n'a pas inventé la poudre

Il l'a juste emballée. Le travail est assuré par le kernel Linux (> 3.10), en standard.

#Les Dockerfile sont tout bêtes

C'est beau comme une suite de lignes de commande.

!SLIDE
#Docker est neutre

Il se fiche bien de la distribution utilisée et de celle de l'hôte.

#Docker respecte l'autorité

L'admin qui déploie un container garde le dernier mot.

#Docker aime le tricotage

Les services sont chacun dans leur conteneur, en un ou plusieurs exemplaires,
on peut les paramétrer et les organiser comme on veut.

!SLIDE
#Docker est universel

Votre container a autant sa place sur votre machine, en qualif, preprod ou prod.

Il tournera sur votre serveur, votre cloud AWS, Google, Azur…

#Docker est éphémère ou immortel

Il peut être utilisé pour faire du batch, ou du service.

Il facilite le déploiement (et son rollback), la scalabilité, la résilience.
