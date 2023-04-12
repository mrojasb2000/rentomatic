import pytest
from rentomatic.repository import mongorepo

pytestmark = pytest.mark.integration

def test_repository_list_without_params(app_configuration, mg_database, mg_test_data):
    repo = mongorepo.MongoRepo(app_configuration)

    repo_rooms = repo.list()

    assert set([r.code for r in repo_rooms]) == set([r["code"] for r in mg_test_data])
