FROM python:3-onbuild

LABEL maintainer "kmnk <kmnknmk+com-github@gmail.com>"

RUN pip install discord.py

CMD ["python", "ikabot.py"]
