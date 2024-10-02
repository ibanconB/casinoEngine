import pytest
from casino.rng import generate_number_wheel


def test_generar_numero_ruleta():
    numero = generate_number_wheel()
    assert 0 <= numero <= 36