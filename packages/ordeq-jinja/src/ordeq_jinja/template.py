from dataclasses import dataclass

from jinja2 import Environment, Template
from ordeq import Input


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
    >>> template.render(name='World')  # doctest: +SKIP
    'Hello, World!'

    ```


    """

    environment: Environment
    template: str

    def load(self) -> Template:
        return self.environment.get_template(self.template)
