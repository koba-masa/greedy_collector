import pytest

from models.announcement import Announcement

def test_tablename():
  assert(Announcement.__tablename__) == 'announcement'
