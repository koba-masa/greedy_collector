import pytest

from models.database import Database

def test_session():
  assert(Database.session()) is not None
