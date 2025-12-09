import pendulum
from air_quality import pipeline
from airflow.sdk import dag, task
from ordeq import run


@dag(
    dag_id="dag_nodes",
    schedule="@daily",
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
)
def dag_nodes():
    @task(task_id="task_run_ingest")
    def task_run_ingest(**kwargs):
        return run(pipeline.ingest)

    @task(task_id="task_run_aggregate")
    def task_run_aggregate(**kwargs):
        return run(pipeline.aggregate)

    ingest = task_run_ingest()
    aggregate = task_run_aggregate()

    ingest >> aggregate


_ = dag_nodes()
