from pc_status.filters import (
    valueformat,
    fromtimestamp,
    uptimeformat,
    totaluptimeformat
)


def test_valueformat():
    assert valueformat('') == '-'
    assert valueformat(22) == 22
    assert valueformat('4312') == '4312'


def test_fromtimestamp():
    assert fromtimestamp(933189323) == "1999.07.28 19:15"


def test_uptimeformat():
    assert uptimeformat('0') == '0 мин.'
    assert uptimeformat('5') == '5 мин.'
    assert uptimeformat('21') == '21 мин.'
    assert uptimeformat('1:21') == '1 ч. 21 мин.'
    assert uptimeformat('21:03') == '21 ч. 03 мин.'
    assert uptimeformat('') == '-'


def test_totaluptimeformat():
    assert totaluptimeformat(0) == 'меньше минуты'
    assert totaluptimeformat(50) == 'меньше минуты'
    assert totaluptimeformat(120) == '02 мин.'
    assert totaluptimeformat(1200) == '20 мин.'
    assert totaluptimeformat(3600) == '1 ч. '
    assert totaluptimeformat(36000) == '10 ч. '
    assert totaluptimeformat(36060) == '10 ч. 01 мин.'
    assert totaluptimeformat(100000) == '1 д. 3 ч. 46 мин.'
