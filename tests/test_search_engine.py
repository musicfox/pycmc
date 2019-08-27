import pytest
import pycm
from pycm import utilities


@pytest.fixture
def sr_keys():
    return ['artists', 'playlists', 'tracks', 'curators', 'albums']


def test_search(sr_keys):
    test = pycm.search_engine.search('Eminem')
    assert isinstance(test, type(dict()))
    result_len = []
    for key in sr_keys:
        assert key in test.keys()
        result_len.append(len(test[key]) > 0)
    assert any(result_len)
    