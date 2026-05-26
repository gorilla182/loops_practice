import pytest
from playwright.sync_api import Page, expect

from pages.TopicsPage import TopicsPage

SEARCH_QUERIES = ["qa", "aqa", "python"]
MIN_RESULTS = 5


@pytest.mark.ui
@pytest.mark.parametrize("query", SEARCH_QUERIES)
def test_search_returns_enough_results(page: Page, query: str):
    main_page = TopicsPage(page)
    main_page.search(query)

    results = main_page.get_search_result_items()

    expect(results.nth(MIN_RESULTS)).to_be_visible(timeout=10_000)

    count = results.count()
    assert count > MIN_RESULTS, (
        f"Запрос «{query}»: ожидалось > {MIN_RESULTS} результатов, получено {count}"
    )