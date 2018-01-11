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
### rand weapon `[count]` `[target_weapon_types]`
Select weapon at random

```
kmnk> ?rand weapon
IkaBot> Splattershot Jr.
kmnk> ?rand weapon 1 chargers rollers
IkaBot> Foil Flingza Roller
```

#### Parameters
- `count`
    - select count(default:1)
- `target_weapon_types`
    - space separated weapon types for filtering weapon candidates(default:all)
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

## License
MIT

[discordpy]:https://github.com/Rapptz/discord.py
[docker]:https://www.docker.com/
