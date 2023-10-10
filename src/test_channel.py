import pytest
from ../src import *

@pytest.fixture
def channel():
    return Channel('channel_id')

def test_channel_init(channel):
    assert channel.channel_id == 'channel_id'
