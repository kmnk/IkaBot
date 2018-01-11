# IkaBot
Bot on Discord for enjoying Splatoon2

## Required
- [Rappts/discord.py][discordpy]
- [Docker][docker]

## Usage
1. Make `TOKEN` file on root directory and write your Discord bot token
2. Execute commands on root directory
```
$ docker build -t ikabot -f Dockerfile .
$ docker run -it ikabot
```

Executing commands sample:
```
$ cd IkaBot
$ cat TOKEN
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
$ docker build -t ikabot -f Dockerfile .
...
Successfully tagged ikabot:latest
$ docker run -it ikabot
...
INFO:__main__:Logged in as
INFO:__main__:- name: IkaBot
INFO:__main__:- id: 000000000000000000
------
```

### Language
If you want to use this bot in Japanese, specify `-e LANGUAGE=ja_JP` environment option on execute `docker run` command
```
$ docker run -e LANGUAGE=ja_JP -it ikabot
```

### Prefix
Bot commands needs prefix (default : `?`)

If you want to change command prefix, specify `PREFIX` environment option on execute `docker run` command
```
$ docker run -e PREFIX=! -it ikabot
```

## Commands
### rand weapon (target weapon types)
Select weapon at random

```
kmnk> ?rand weapon all
IkaBot> Splattershot Jr.
kmnk> ?rand weapon chergers rollers
IkaBot> Foil Flingza Roller
```

You can specify space separated weapon types for filtering weapon candidates

#### Weapon Types
- all
- shooters
- dualies
- rollers
- brushes
- blasters
- brellas
- sloshers
- chargers
- splatlings

[discordpy]:https://github.com/Rapptz/discord.py
[docker]:https://www.docker.com/
