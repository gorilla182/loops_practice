from pages.TopicsPage import TopicsPage
import pytest
from playwright.sync_api import *


EXPECTED_TOPICS = [
    "Awesome Lists",
    "CSS",
    "JavaScript",
    "Python",
    "React",
    "TypeScript",
]

@pytest.mark.ui
def test_topics(page: Page):
    topic_page = TopicsPage(page)
    topic_page.open()

    actual_topics = topic_page.get_topic_items()
    actual_topics_normalized = [t.strip() for t in actual_topics]

    missing = [
        topic for topic in EXPECTED_TOPICS
        if topic not in actual_topics_normalized
    ]

    assert not missing, (
        f"Отсутствующие элементы в разделе Topics: {missing}\n"
        f"Фактический список: {actual_topics_normalized}"
    )