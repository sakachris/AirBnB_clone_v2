#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            # from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            # storage.new(self)
        else:
            """kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']
            self.__dict__.update(kwargs)"""
            attr = {k: v for k, v in kwargs.items() if k != '__class__'}
            for key, val in attr.items():
                if key in ['created_at', 'updated_at']:
                    dt_obj = datetime.strptime(val, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, dt_obj)
                else:
                    setattr(self, key, val)
            if 'id' not in attr:
                self.id = str(uuid4())
            if 'created_at' not in attr:
                self.created_at = datetime.now()
            if 'update_at' not in attr:
                self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation of the instance"""
        """cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)"""
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                      self.__dict__))

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        """dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary"""
        dt = {}
        dt["__class__"] = self.__class__.__name__
        for key, val in self.__dict__.items():
            if type(val) == datetime:
                dt[key] = val.isoformat()
            else:
                dt[key] = val
        if '_sa_instance_state' in dt:
            del dt['_sa_instance_state']
        return dt

    def delete(self):
        """
        deletes the current instance from the storage
        """
        from models import storage
        storage.delete(self)
