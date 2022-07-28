from pc_status.filters import valueformat, fromtimestamp, uptimeformat


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
