from ordeq import IO, Input, node, run
from ordeq_common import Print


class Chat(IO[str]):
    """Dummy IO class representing a chat interface."""

    def load(self) -> None:
        pass

    def save(self, _) -> None:
        print("Its sunny!")


question = Input[str]("What's the weather today")
country_iso = Input[str]("NL")
chat = Chat("weather_bot")


@node(inputs=[question, country_iso], outputs=chat)
def ask_question_for_country(q: str, cntry_iso: str) -> str:
    match cntry_iso:
        case "NL":
            return f"{q} in The Netherlands?"
        case "DE":
            return f"{q} in Germany?"
        case _:
            return f"{q} in Hawaii?"


@node(inputs=[chat], outputs=Print())
def print_answer(answer: str) -> str:
    return f"The bot answered: '{answer}'"


run(ask_question_for_country, print_answer)
