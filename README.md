# IkaBot
Bot on Discord for enjoying Splatoon2

## Required
- [Docker][docker]

## Usage
1. Make `TOKEN` file on root directory and write your Discord bot token
2. Execute commands on root directory
```
$ docker build -t ikabot -f Dockerfile .
$ docker run -it ikabot
```

## Executing commands sample
```
$ cd IkaBot
$ cat TOKEN
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
$ docker build -t ikabot -f Docker file .
...
Successfully tagged ikabot:latest
$ docker run -it ikabot
Logged in as
IkaBot
123456789012345678
------
```

[docker]:https://www.docker.com/
