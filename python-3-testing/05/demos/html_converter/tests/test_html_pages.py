import io

from html_pages import HtmlPagesConverter


def test_convert_second_page():
    fake_file = io.StringIO("""\
page one
PAGE_BREAK
page two
PAGE_BREAK
page three
""")
    converter = HtmlPagesConverter(fake_file)
    converted_text = converter.get_html_page(1)
    assert converted_text == "page two<br />"