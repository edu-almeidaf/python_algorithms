import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    assert encrypt_message("EDUARDO", 30) == "ODRAUDE"
    assert encrypt_message("EDUARDO", 5) == "RAUDE_OD"
    assert encrypt_message("EDUARDO", 4) == "ODR_AUDE"

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("ABCDEF", "1")

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(48, 12)
