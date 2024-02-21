#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from user import Base, User
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from sqlalchemy.exc import InvalidRequestError


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db")
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Memoized session object
        """
        db_user = User(email=email, hashed_password=hashed_password)
        self._session.add(db_user)
        self._session.commit()
        return db_user

    def find_user_by(self, **kwarg) -> User:
        """Memoized session object
        """
        if kwarg is None:
            raise InvalidRequestError

        user_keys = ['id', 'email', 'hashed_password',
                     'session_id', 'reset_token']
        for key in kwarg.keys():
            if key not in user_keys:
                raise InvalidRequestError

        firstRow = self._session.query(User).filter_by(**kwarg).first()
        if firstRow is None:
            raise NoResultFound

        return firstRow

    def update_user(self, user_id: int, **kwarg) -> None:
        """Memoized session object
        """
        obj = self.find_user_by(id=user_id)
        user_keys = ['id', 'email', 'hashed_password',
                     'session_id', 'reset_token']
        for key, val in kwarg.items():
            if key in user_keys:
                setattr(obj, key, val)
            else:
                raise ValueError

        self._session.commit()
