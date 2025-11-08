# ./app/utils/crud_mixin.py
from app.extensions import db

class CRUDMixin:
    """
    Mixin that adds convenience methods for CRUD (Create, Read, Update, Delete)
    operations.
    """
    @classmethod
    def create(cls, **kwargs):
        """Create a new record and save it to the database."""
        instance = cls(**kwargs)
        return instance.save()

    def update(self, commit=True, **kwargs):
        """Update specific fields of a record."""
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        return self.save() if commit else self

    def save(self, commit=True):
        """Save the object to the database."""
        db.session.add(self)
        if commit:
            db.session.commit()
        return self

    def delete(self, commit=True):
        """Remove the object from the database."""
        db.session.delete(self)
        if commit:
            db.session.commit()

    @classmethod
    def get(cls, id):
        """Get a record by its primary key."""
        return cls.query.get(id)
    
    @classmethod
    def get_all(cls):
        """Get all records of this model."""
        return cls.query.all()

    @classmethod
    def find_by(cls, **kwargs):
        """Find the first record that matches the given criteria."""
        return cls.query.filter_by(**kwargs).first()