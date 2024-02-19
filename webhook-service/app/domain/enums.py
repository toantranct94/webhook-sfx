from enum import Enum


class EventType(Enum):
    CREATED = "created"
    UPDATED = "updated"
    DELETED = "deleted"
