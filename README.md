# docker-basic-1

**Explique la différence entre CMD dans le Dockerfile et les arguments passés au docker run .**
CMD c'est la commande par défaut qui va s'exécuter à l'exécution et il peut être override
Les arguments passés dans `python -c "print('Commande override')"` override la commande

**Explique la différence entre supprimer un conteneur ( docker rm ) et supprimer une image ( docker image rm ).**
Supprimer un conteneur c'est supprimer l'exécution de l'image
et supprimer l'image c'est supprimer l'image qui est la config de l'app/os

```bash
$ docker build -t <name>:<version> <path>
$ docker run --rm --name <container_name> <name>:<version>
$ docker logs <container_name>
$ docker image prune
$ docker container prune
```
