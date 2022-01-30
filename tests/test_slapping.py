import pytest

from app.slapp import LikeState, slap_many


def test_many_slaps():
    assert slap_many(LikeState.empty, 'll') is LikeState.empty
