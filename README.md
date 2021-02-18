# happy-birthday

Pour lire cette carte d'anniversaire, suivre les étapes suivantes:

```
git clone https://github.com/stecaron/happy-birthday.git
cd happy-birthday
docker build -t bonnefete .
docker run --name keven -p 8282:4000 bonnefete
```

Allez sur ton `localhost:8282`.

Allez, bye.
