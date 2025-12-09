import pendulum
from airflow.sdk import dag, task


@dag(
    dag_id="dag_docker",
    schedule="@daily",
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
)
def dag_docker():
    @task.docker(task_id="run_docker", image="air_quality:latest")
    def run_docker(**kwargs):
        pass


_ = dag_docker()
