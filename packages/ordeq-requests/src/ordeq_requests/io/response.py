from abc import abstractmethod
from dataclasses import dataclass, field
from typing import Any, Literal, TypeVar

import requests
from ordeq.framework.io import Input
from requests import Session
from urllib3.response import HTTPResponse

T = TypeVar("T")


@dataclass(frozen=True, kw_only=True)
class Response(Input[T]):
    """IO to load data from an API using `requests`.

    Example:

    ```pycon
    >>> from ordeq_requests import Response
    >>> User = ResponseContent(
    ...     url="https://jsonplaceholder.typicode.com/users/1"
    ... )
    >>> User.load()  # doctest: +SKIP
    b'{"id":1,"name":"Leanne Graham", ...}'  # type bytes
    ```

    Use `ResponseText` or `ResponseJSON` to parse as `str` or `dict`:

    ```pycon
    >>> from ordeq_requests import ResponseText
    >>> UserText = ResponseText(
    ...     url="https://jsonplaceholder.typicode.com/users/1"
    ... )
    >>> UserText.load()  # doctest: +SKIP
    '{"id":1,"name":"Leanne Graham", ...}'  # type str
    >>> from ordeq_requests import ResponseJSON
    >>> UserJSON = ResponseJSON(
    ...     url="https://jsonplaceholder.typicode.com/users/1"
    ... )
    >>> UserJSON.load()  # doctest: +SKIP
    {'id': 1, 'name': 'Leanne Graham', ...}  # type dict
    ```

    Example in a node:

    ```pycon
    >>> from ordeq.framework import node
    >>> from ordeq_files import JSON
    >>> from pathlib import Path
    >>> @node(
    ...     inputs=UserJSON,
    ...     outputs=JSON(path=Path("location.json"))
    ... )
    ... def parse_user_location(user: dict) -> dict:
    ...     return {
    ...         "id": user["id"],
    ...         "lat": user["geo"]["lat"],
    ...         "lng": user["geo"]["lng"]
    ...     }

    ```

    By default, each `Response` instance will create a new `requests.Session`. To
    reuse a session across multiple datasets, pass it as attribute on init:

    ```pycon
    >>> from requests.auth import HTTPBasicAuth
    >>> session = Session()
    >>> RequestWithCookies = ResponseJSON(
    ...     url="https://httpbin.org/cookies/set/cookie/123",
    ...     method="GET",
    ...     session=session
    ... )
    >>> RequestWithCookies.load()  # doctest: +SKIP
    {'cookies': {'cookie': '123'}}
    >>> session.cookies.items()  # doctest: +SKIP
    [('cookie', '123')]
    >>> NextRequestWithCookies = ResponseJSON(
    ...     url="https://jsonplaceholder.typicode.com/users/2",
    ...     method="GET",
    ...     session=session  # reuse session and cookies in next request
    ... )

    ```

    Authentication can also be set on the `session` attribute:

    ```pycon
    >>> from requests.auth import HTTPBasicAuth
    >>> session = Session()
    >>> session.auth = HTTPBasicAuth('user', 'password')
    >>> RequestWithAuth = ResponseText(
    ...     url="https://httpbin.org/headers",
    ...     method="GET",
    ...     session=session
    ... )
    >>> RequestWithAuth.load()  # doctest: +SKIP
    {"headers":{"Accept":"*/*", ..., "Authorization": "Basic ******"}}
    ```

    Similar patterns apply to other configuration like certificates and
    proxies. See [1](https://requests.readthedocs.io/en/latest/user/advanced/#session-objects)
    for more info.

    """  # noqa: E501 (line too long)

    url: str
    method: Literal["GET"] = "GET"
    session: Session = field(default_factory=Session)

    @abstractmethod
    def load(self) -> T: ...

    def _request(self, **request_args: Any) -> requests.Response:
        """Make a request and return the response.

        Args:
            **request_args: Additional arguments to pass to `requests.request`.

        Returns:
            `requests` Response

        Raises:
            HTTPError, if one occurred

        """

        r = self.session.request(
            method=self.method, url=self.url, **request_args
        )
        r.raise_for_status()
        return r


@dataclass(frozen=True)
class ResponseContent(Response[bytes]):
    def load(self) -> bytes:
        return self._request().content


@dataclass(frozen=True)
class ResponseText(Response[str]):
    def load(self) -> str:
        return self._request().text


@dataclass(frozen=True)
class ResponseJSON(Response[dict]):
    def load(self) -> dict:
        return self._request().json()


@dataclass(frozen=True)
class ResponseStream(Response[HTTPResponse]):
    def load(self) -> HTTPResponse:
        return self._request(stream=True).raw
