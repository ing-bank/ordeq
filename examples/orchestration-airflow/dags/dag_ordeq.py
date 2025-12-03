import air_quality_insights
import pendulum
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.sdk import dag, task
from ordeq import run


@dag(
    schedule=None,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=["example"],
)
def tutorial_object_storage():
    # Run the entire pipeline in one task:
    @task
    def task_pipeline(**kwargs) -> None:
        return run(air_quality_insights)

    # Run each node as a separate task:
    @task
    def task_get_air_quality_data(**kwargs) -> None:
        return run("air_quality_insights.pipeline.get_air_quality_data")

    @task
    def task_analyze(**kwargs) -> None:
        return run("air_quality_insights.pipeline.analyze")

    # Run as Docker container:
    return DockerOperator(
        task_id="task_docker",
        image="air_quality_insights:latest",
        api_version="auto",
        docker_url="unix://var/run/docker.sock",
        network_mode="bridge",
    )


tutorial_object_storage()
