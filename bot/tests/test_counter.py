from bot.common.utils import Counter


def test_counter():
    a, = Counter()
    b, = Counter()
    c, d, e = Counter(3)

    assert (a, b, c, d, e) == (*map(chr, range(5)), )
