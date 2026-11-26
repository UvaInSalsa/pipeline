import pytest
from descuentos import calcular_total


def test_cp01_precio_invalido():
    with pytest.raises(ValueError, match="positivos"):
        calcular_total(0, 5, False)


def test_cp02_cantidad_invalida():
    with pytest.raises(ValueError, match="positivos"):
        calcular_total(100, -1, False)


def test_cp03_limite_9_sin_frecuente():
    assert calcular_total(100, 9, False) == 900.00


def test_cp04_limite_9_cliente_frecuente():
    assert calcular_total(100, 9, True) == 855.00


def test_cp05_limite_10_sin_frecuente():
    assert calcular_total(100, 10, False) == 900.00


def test_cp06_limite_10_cliente_frecuente():
    assert calcular_total(100, 10, True) == 850.00


def test_cp07_limite_11_sin_frecuente():
    assert calcular_total(100, 11, False) == 990.00


def test_cp08_limite_11_cliente_frecuente():
    assert calcular_total(100, 11, True) == 935.00


def test_cp09_estandar_sin_descuento():
    assert calcular_total(50, 4, False) == 200.00


def test_cp10_estandar_descuento_maximo():
    assert calcular_total(80, 20, True) == 1360.00
