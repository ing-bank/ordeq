from pathlib import Path

from ordeq_files import CSV


def test_it_loads(tmp_path: Path):
    path = tmp_path / "test_it_loads.csv"
    path.write_text("a,b,c\n1,2,3\n4,5,6\n")
    assert CSV(path=path).load() == [
        ["a", "b", "c"],
        ["1", "2", "3"],
        ["4", "5", "6"],
    ]


def test_it_loads_with_options(tmp_path: Path):
    path = tmp_path / "test_it_loads_with_options.csv"
    path.write_text('a,"b,c"\n1,"2,3"\n4,"5,6"\n')
    assert CSV(path=path).load(quotechar='"', delimiter=",") == [
        ["a", "b,c"],
        ["1", "2,3"],
        ["4", "5,6"],
    ]


def test_it_saves(tmp_path: Path):
    path = tmp_path / "test_it_saves.csv"
    CSV(path=path).save([["a", "b", "c"], ["1", "2", "3"], ["4", "5", "6"]])
    assert path.read_text() == "a,b,c\n1,2,3\n4,5,6\n"


def test_it_saves_with_options(tmp_path: Path):
    path = tmp_path / "test_it_saves_with_options.csv"
    CSV(path=path).save(
        [["a", "b,c"], ["1", "2,3"], ["4", "5,6"]],
        quotechar='"',
        delimiter=",",
    )
    assert path.read_text() == 'a,"b,c"\n1,"2,3"\n4,"5,6"\n'


def test_it_saves_streams(tmp_path: Path):
    path = tmp_path / "test_it_saves_stream.csv"
    csv = CSV(path=path)

    def generator():
        yield ["constant", "idx"]
        for idx in range(10):
            yield [1, idx]

    csv.save(generator())
    assert (
        path.read_text()
        == "constant,idx\n1,0\n1,1\n1,2\n1,3\n1,4\n1,5\n1,6\n1,7\n1,8\n1,9\n"
    )
