import pytest
from src.isla import posicion_inicial_del_jugador, genera_pista, genera_pista_filas, genera_pista_columnas
from src.isla import obtener_nueva_posicion, procesar_movimiento, simbolo_celda


@pytest.mark.parametrize(
    "inPosicion, inMapa, outNumero",
    [
        ((0, 5), [
            ['!', '!', '!', 'v', '<'],
            ['v', ' ', ' ', 'v', 'v'],
            ['X', ' ', '<', '!', '<'],
            ['^', '!', '<', '!', '!'],
            ['!', '!', '!', '!', '^']
         ], 1),
        ((2, 0), [
            ['!', '!', '!', 'v', '<'],
            ['v', ' ', ' ', 'v', 'v'],
            ['X', ' ', '<', '!', '<'],
            ['^', '!', '<', '!', '!'],
            ['!', '!', '!', '!', '^']
         ], 2),
        ((2, 3), [
            ['!', '!', '!', 'v', '<'],
            ['v', ' ', ' ', 'v', 'v'],
            ['X', ' ', '<', '!', '<'],
            ['^', '!', '<', '!', '!'],
            ['!', '!', '!', '!', '^']
        ], 3),
        ((3, 2), [
            ['!', '!', '!', 'v', '<'],
            ['v', ' ', ' ', 'v', 'v'],
            ['X', ' ', '<', '!', '<'],
            ['^', '!', '<', '!', '!'],
            ['!', '!', '!', '!', '^']
        ], 4),
        ((1, 2), [
            ['!', '!', '!', 'v', '<'],
            ['v', ' ', ' ', 'v', 'v'],
            ['X', ' ', '<', '!', '<'],
            ['^', '!', '<', '!', '!'],
            ['!', '!', '!', '!', '^']
        ], 5)
    ]
)
def test_procesar_movimiento(inPosicion, inMapa, outNumero):
    assert procesar_movimiento(inPosicion, inMapa) == outNumero


@pytest.mark.parametrize(
    "inCelda, outOculto",
    [
        ("!", "?"),
        ("v", "?"),
        ("^", "?"),
        ("<", "?"),
        (">", "?"),
        ("X", "?"),
        (" ", " "),

    ]
)
def test_simbolo_celda(inCelda, outOculto):
    assert simbolo_celda(inCelda) == outOculto


@pytest.mark.parametrize(
    "inJugador, inPosicion, outTupla",
    [
        ((2, 2), "u", (1, 2)),
        ((2, 2), "d", (3, 2)),
        ((2, 2), "l", (2, 1)),
        ((2, 2), "r", (2, 3)),
        ((2, 2), "q", (2, 2))
    ]
)
def test_obtener_nueva_posicion(inJugador, inPosicion, outTupla):
    assert obtener_nueva_posicion(inJugador, inPosicion) == outTupla


@pytest.mark.parametrize(
    "inTesoro, inPosicion, outPista",
    [
        ((2, 0), (1, 0), "v"),
        ((2, 0), (2, 2), "<")
    ]
)
def test_genera_pista(inTesoro, inPosicion, outPista):
    assert genera_pista(inTesoro, inPosicion) == outPista


@pytest.mark.parametrize(
    "inTesoro, inPosicion, outPista",
    [
        ((2, 0), (1, 0), "v"),
        ((2, 0), (3, 0), "^"),
    ]
)
def test_genera_pista_filas(inTesoro, inPosicion, outPista):
    assert genera_pista_filas(inTesoro, inPosicion) == outPista


@pytest.mark.parametrize(
    "inTesoro, inPosicion, outPista",
    [
        ((2, 0), (2, 2), "<"),
        ((2, 1), (3, 0), ">"),
    ]
)
def test_genera_pista_columnas(inTesoro, inPosicion, outPista):
    assert genera_pista_columnas(inTesoro, inPosicion) == outPista


def test_posicion_inicial_del_jugador():
    assert posicion_inicial_del_jugador() == (2, 2)
