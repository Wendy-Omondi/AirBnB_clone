#!/usr/bin/python3
"""defines a city class"""


from models.base_model import BaseModel


class City(BaseModel):
    """describes city parameters"""

    state_id = ""
    name = ""
