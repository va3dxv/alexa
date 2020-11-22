# -*- coding: utf-8 -*-
import gettext

_ = gettext.gettext

WELCOME_MSG = _("Welcome to {}")
HELP_MSG = _("Welcome to {}.")
UNHANDLED_MSG = _("What?")
CANNOT_SKIP_MSG = _("This is a radio!")
RESUME_MSG = _("Resuming {}")
NOT_POSSIBLE_MSG = _("What?")
STOP_MSG = _("73")
DEVICE_NOT_SUPPORTED = _("I cant do that Dave.")

TEST = _("test english")
TEST_PARAMS = _("test with parameters {} and {}")

jingle = {
    "db_table": "my_radio",
    "play_once_every": 1000*60*60*24  # 24 hours
}

en = {
    "card": {
        "title": 'Reflector 14 Charlie',
        "text": 'You can listen to D-Star Reflector 14 Charlie',
        "large_image_url": 'https://alexademo.ninja/skills/logo-512.png',
        "small_image_url": 'https://alexademo.ninja/skills/logo-108.png'
    },
    "url": 'https://relay.broadcastify.com/6jsn4cg25bm7vk9.mp3?xan=xtf9912b',
    "start_jingle": 'https://ve3oje.s3.amazonaws.com/ve3oje.mp3'
}