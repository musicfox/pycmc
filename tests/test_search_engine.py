import pytest
import pycmc
from pycmc import utilities

# TODO Refactor the search test below.
@pytest.fixture
def sr_keys():
    return ["artists", "playlists", "tracks", "curators", "albums"]


def test_search(sr_keys):
    test = pycmc.search_engine.search("Eminem")
    assert isinstance(test, type(dict()))
    result_len = []
    for key in sr_keys:
        assert key in test.keys()
        result_len.append(len(test[key]) > 0)
    assert any(result_len)


@pytest.mark.parametrize(
    "type,query",
    [
        ("artists", "Dua Lipa"),
        ("tracks", "Don't Start Now"),
        ("playlists", "Today's Top Hits"),
        ("curators", "Spotify"),
        ("albums", "Future Nostalgia"),
        ("stations", "Radio"),
        ("cities", "Paris")
    ]
)
def test_search_by_type(type, query):
    test = pycmc.search_engine.search(query, type=type)
    assert isinstance(test, dict)
    assert set(test) == {type}
    result_type = dict if type in ('playlists', 'curators') else list
    assert isinstance(test[type], result_type)
    assert len(test[type]) > 0
