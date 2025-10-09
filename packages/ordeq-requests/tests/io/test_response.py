import pytest
from ordeq import IOException
from ordeq_requests import (
    Response,
    ResponseContent,
    ResponseJSON,
    ResponseStream,
    ResponseText,
)


class TestRaiseForError:
    @pytest.mark.parametrize(
        "cls", [ResponseContent, ResponseJSON, ResponseText]
    )
    def test_it_raises_for_status(self, cls: type[Response], url):
        with pytest.raises(IOException) as exc:
            # noinspection PyArgumentList
            cls(url=f"{url}/nok").load()
        assert "418 Client Error: I'm a Teapot" in exc.value.args[0]


class TestResponseContent:
    def test_it_loads(self, url):
        content = ResponseContent(url=f"{url}/").load()
        assert content == b'{"Hello":"World"}'


class TestResponseText:
    def test_it_loads(self, url):
        text = ResponseText(url=f"{url}/").load()
        assert text == '{"Hello":"World"}'


class TestResponseJSON:
    def test_it_loads(self, url):
        data = ResponseJSON(url=f"{url}/").load()
        assert data == {"Hello": "World"}


class TestResponseStream:
    def test_it_loads(self, url):
        stream = ResponseStream(url=f"{url}/").load()
        # Read all bytes from the stream
        content = stream.read()
        assert content == b'{"Hello":"World"}'
        stream.close()
