#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ """
        new = self.value()
        new.first_name = "Jacqueline"
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ """
        new = self.value()
        new.last_name = "Tuyisenge"
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ """
        new = self.value()
        new.email = "tuyisengejacqui@gmail.com"
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ """
        new = self.value()
        new.password = "G343sD6"
        self.assertEqual(type(new.password), str)
