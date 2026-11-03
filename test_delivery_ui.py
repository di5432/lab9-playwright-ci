import pytest

@pytest.mark.parametrize(
    ("amount", "expected"),
    [
        (1, "Стоимость доставки: 1\u00a0000 ₸"),
        (5000, "Стоимость доставки: 1\u00a0000 ₸"),
        (9999, "Стоимость доставки: 1\u00a0000 ₸"),
        (10000, "Доставка бесплатная."),
        (10001, "Доставка бесплатная."),
        (15000, "Доставка бесплатная."),
    ],
)
def test_city_delivery(delivery_page, amount, expected):
    delivery_page.locator("#delivery-type").select_option("city")
    delivery_page.locator("#order-amount").fill(str(amount))
    delivery_page.locator("#calculate").click()
    assert delivery_page.locator("#delivery-result").inner_text() == expected


@pytest.mark.parametrize(
    ("amount", "expected"),
    [
        (1, "Стоимость доставки: 2\u00a0000 ₸"),
        (5000, "Стоимость доставки: 2\u00a0000 ₸"),
        (9999, "Стоимость доставки: 2\u00a0000 ₸"),
        (10000, "Доставка бесплатная."),
        (10001, "Доставка бесплатная."),
        (15000, "Доставка бесплатная."),
    ],
)
def test_region_delivery(delivery_page, amount, expected):
    delivery_page.locator("#delivery-type").select_option("region")
    delivery_page.locator("#order-amount").fill(str(amount))
    delivery_page.locator("#calculate").click()
    assert delivery_page.locator("#delivery-result").inner_text() == expected
