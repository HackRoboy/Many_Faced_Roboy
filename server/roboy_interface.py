import logging
from logs import log


def roboy_say(text:str):
    log.info("ROBOYSAY: {text}".format(text = text))