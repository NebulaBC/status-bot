# StatusBot

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Setting up bot

To set up the bot you need to fill out `config.env` with your token, channel-id, and the cooldown for server updates. From there you can run `init.py`, and it will send a message. You can take the ID of the message and put that in `config.env`, once all of the feilds are filled out you can run `main.py`

## Misc

This bot does not use the query port, and just takes from the user list (due to me not having query port access at the time of creation), I am now working on a new version of this that will have a public bot and query port support (so check back).
