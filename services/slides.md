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
