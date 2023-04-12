import pytest
from rentomatic.repository import mongorepo

pytestmark = pytest.mark.integration

def test_repository_list_without_params(app_configuration, mg_database, mg_test_data):
    repo = mongorepo.MongoRepo(app_configuration)

    repo_rooms = repo.list()

    assert set([r.code for r in repo_rooms]) == set([r["code"] for r in mg_test_data])

def test_repository_list_with_code_equal_filter(app_configuration, mg_database, mg_test_data):
    repo = mongorepo.MongoRepo(app_configuration)

    repo_rooms = repo.list(filters={"code__eq": "fe2c3195-aeff-487a-a08f-e0bdc0ec6e9a"})

    assert len(repo_rooms) == 1
    assert repo_rooms[0].code == "fe2c3195-aeff-487a-a08f-e0bdc0ec6e9a"
