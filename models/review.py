#!/usr/bin/python3
"""defines a review class"""


from models.base_model import BaseModel


class Review(BaseModel):
    """review details"""
    place_id = ""
    user_id = ""
    text = ""
