from pathlib import Path

from jinja2 import Environment, FileSystemLoader
from ordeq_jinja import JinjaTemplate


def test_it_loads():
    env = Environment(loader=FileSystemLoader(
        Path(__file__).parent))  # noqa: S701 (unsafe autoescape)
    template_name = "dummy_template.jinja"
    jinja_template = JinjaTemplate(environment=env, template=template_name)
    template = jinja_template.load()
    assert template.render(greeting="Hello", name="World") == "Hello, World!"


def test_it_loads_with_options():
    env = Environment(loader=FileSystemLoader(
        Path(__file__).parent))  # noqa: S701 (unsafe autoescape)
    template_name = "dummy_template.jinja"
    jinja_template = JinjaTemplate(environment=env, template=template_name)
    template = jinja_template.load(globals={"greeting": "Buenos dias"})
    assert template.render(name="World") == "Buenos dias, World!"
