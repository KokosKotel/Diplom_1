from praktikum.bun import Bun


class TestBun:
    def test_bun_get_name(self):
        bun = Bun("Краторная булка", 1255)
        assert bun.get_name() == "Краторная булка"

    def test_bun_get_price(self):
        bun = Bun("Краторная булка", 1255)
        assert bun.get_price() == 1255
