import pytest

@pytest.fixture
def delivery_page(page):
    page.goto("http://127.0.0.1:8000/delivery.html")
    return page
