from pathlib import Path

from ordeq_files import CSV

TEST_RESOURCES_DIR = Path(__file__).resolve().parent.parent / "tests-resources"
names = CSV(path=TEST_RESOURCES_DIR / "test-names.csv")
greetings = CSV(path=TEST_RESOURCES_DIR / "test-greetings.csv")
