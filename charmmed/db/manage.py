from datetime import datetime

from peewee import (
    SQL,
    BooleanField,
    CharField,
    CompositeKey,
    DateTimeField,
    ForeignKeyField,
    IntegerField,
    Model,
    UUIDField,
    chunked,
)

from playhouse.sqlite_ext import SqliteExtDatabase

#TODO: create tables for data that is important to store/access
class DBDeltaG():
    class Meta:
        table_name = "deltaG"

    name = CharField(max_length=255, null=True, index=True)
    created = DateTimeField(null=False, default=datetime.now)