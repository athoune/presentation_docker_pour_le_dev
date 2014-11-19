!SLIDE
# Je veux un redis

Il existe une [image officielle](https://registry.hub.docker.com/_/redis/).

    $ boot2docker up
    $ docker run --name redis_classique -p 6379:6379 redis

Dans une autre fenêtre

    $ boot2docker ip
    $ redis-cli -h 192.168.59.103

Je peux l'arreter et le relancer

    $ docker stop redis_classique
    $ docker start redis_classique

!SLIDE
# Finalement, je veux le redis trop neuf

    $ docker stop redis_classique
    $ docker run --name redis_bleeding -p 6379:6379 redis:latest

Dans une autre fenêtre

    redis-cli -h 192.168.59.103

!SLIDE
# Je veux voir ce que je pourrais mesurer en prod

Les bases de données orientées série de temps, le compagnon indispensable du développeur consciencieux.

Maintenir des compteurs dans une technologie synchrone est une punition, autant utiliser des outils simples.

Les données métiers vont être poussées via Statsd, sur un InfluxDB, et découverte via Grafana.

Quelques ajouts dans le code, de la configuration en ENV, et c'est parti!

    export STATSD_HOST=192.168.59.103

!SLIDE
# Je veux Mon Code, dans un environement comme la prod

Je voudrais voir comment se comporte mon code dans un environnement un peu farfelu : du [HHVM](https://github.com/nikolaplejic/docker.hhvm)

Comme je n'ai pas confiance, et que l'image n'est pas dispo sur le hub, je la construit :

    docker build -t hhvm .

Depuis le dossier contenant mon code, je lance :

    docker run --rm -p 8080:80 -v `pwd`:/mnt/hhvm:ro hhvm

Finalement, je compare avec l'[image officielle de PHP](https://registry.hub.docker.com/_/php/):

    docker run --rm -p 8080:80 -v `pwd`:/var/www/html:ro php:5.6-apache
