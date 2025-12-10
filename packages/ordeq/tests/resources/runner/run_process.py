import subprocess  # noqa S404 (subprocess)
from dataclasses import dataclass

from ordeq import IO, Input, node, run
from ordeq_common import Print


@dataclass(frozen=True)
class Subprocess(IO[subprocess.CompletedProcess[str]]):
    cmd: tuple[str, ...]

    def _run(self) -> subprocess.CompletedProcess[str]:
        return subprocess.run(self.cmd, check=False, text=True)  # noqa S602 (subprocess)

    def load(self) -> subprocess.CompletedProcess[str]:
        return self._run()

    def save(self, _) -> None:
        self._run()


q = Input[str]("What's the weather today")
country = Input[str]("NL")
write = Subprocess(cmd=("echo", "It's sunny!"))


@node(inputs=[q, country], outputs=write)
def ask_question_for_country(q: str, cntry_iso: str) -> str:
    return f"{q} in {cntry_iso}?"


@node(inputs=write, outputs=Print())
def print_answer(answer: str) -> str:
    return f"The process answered: '{answer}'"


run(ask_question_for_country, print_answer)
