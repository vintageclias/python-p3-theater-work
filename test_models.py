import pytest
from lib.models import db_session, Theater




def test_create_theater():
    theater = Theater(name="Test Theater", location="Virtual")
    db_session.add(theater)
    db_session.commit()

    saved_theater = db_session.query(Theater).filter_by(name="Test Theater").first()
    assert saved_theater is not None
    assert saved_theater.location == "Virtual"
