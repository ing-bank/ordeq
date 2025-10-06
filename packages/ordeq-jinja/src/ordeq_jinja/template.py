from dataclasses import dataclass

from jinja2 import Environment, Template
from ordeq import Input
from typing import Any


@dataclass(frozen=True, kw_only=True)
class JinjaTemplate(Input[Template]):
    """IO for loading Jinja2 templates.

    Example:

    ```pycon
    >>> from jinja2 import Environment, FileSystemLoader
    >>> from ordeq_jinja import JinjaTemplate
    >>> env = Environment(loader=FileSystemLoader('templates'))
    >>> io = JinjaTemplate(environment=env, template='my_template.jinja')
    >>> template = io.load()  # doctest: +SKIP
    <Template 'my_template.jinja'>
    >>> template.render(name='World')  # doctest: +SKIP
    'Hello, World!'

    ```

    """

    environment: Environment
    template: str

    def load(self, **load_options: Any) -> Template:
        """Load the Jinja2 template.

        Args:
            **load_options: Additional options for loading the template.
        """

        return self.environment.get_template(self.template, **load_options)
