"""
Package wide configurations
"""

from pathlib import Path
import sys
from threading import Lock
from typing import Any, Dict

from dotenv import dotenv_values


class ThreadSafeMeta(type):
    """
    Thread safe implementation of Singleton.
    """

    _instances: Dict[Any, Any] = {}

    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the __init__
            do not affect the returned instance.
        """

        with cls._lock:

            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance

        return cls._instances[cls]


class Config(metaclass=ThreadSafeMeta):
    """
    Global program configuration, usess the dotenv package
        to load runtime configuration from a .env file, once
        and only once into this object, this object can be used
        through-out the code base.
    """

    try:
        __config: Dict[str, Any] = dotenv_values('.env')
        __sql_addr = str(__config["SQL_ADDR"])
        __sql_name = str(__config["SQL_NAME"])
        __sql_pass = str(__config["SQL_PASS"])
        __sql_db = str(__config["SQL_DB"])
        __sql_table = str(__config["SQL_TABLE"])

    except KeyError as error:
        sys.stderr.write(f'Dotenv config error: {error} is missing \n')
        sys.exit(1)

    @classmethod
    def sql_address(cls) -> str:
        """
        @description: getter for config
        """
        return cls.__sql_addr

    @classmethod
    def sql_name(cls) -> str:
        """
        @description: getter for config
        """
        return cls.__sql_name

    @classmethod
    def sql_pass(cls) -> str:
        """
        @description: getter for config
        """
        return cls.__sql_pass

    @classmethod
    def sql_db(cls) -> str:
        """
        @description: getter for config
        """
        return cls.__sql_db

    @classmethod
    def sql_table(cls) -> str:
        """
        @description: getter for config
        """
        return cls.__sql_table
