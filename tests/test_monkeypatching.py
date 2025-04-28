import pytest
import responses
from implementations import get_class

# парсер новостей, который нужно протестировать
NewsParser = get_class()


# BEGIN (write your solution here)
@pytest.fixture
def htmlf():
    return """ <html>
     <body>
         <h2 class="news-title">Новость 1</h2>
         <h2 class="news-title">Новость 2</h2>
         <h2 class="not-news">Это не новость</h2>
         <h2 class="news-title">Новость 3</h2>
     </body>
 </html>"""

@responses.activate
def test_new_parser(htmlf, tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "answer.txt"
    p.write_text(CONTENT)
    rsp1 = responses.Response(
        method="GET",
        url="http://example.com",
        body = htmlf
    )
    responses.add(rsp1)
    parser = NewsParser("http://example.com")
    print('f vrjvnfkjvnkjnvjn', parser.fetch_html())
    assert 0
# END
