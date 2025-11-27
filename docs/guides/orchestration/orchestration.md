# Orchestration

This guide explains the concept of orchestration integrations in Ordeq.

## Why use orchestration tools?

Orchestration tools help manage the execution of complex workflows by handling task scheduling, dependencies, retries, and resource management.
This is crucial for pipelines that run frequently, require significant computational resources, or need to be monitored and logged effectively.
Examples of orchestration tools include Apache Airflow, Kubeflow, Prefect, and cloud-native services like Google Cloud Composer or AWS Step Functions.

What orchestration tools typically provide:

- **Scheduling**: Automate the execution of pipelines at specified intervals or in response to events.
- **Error Handling and Retries**: Automatically handle task failures and retries according to predefined policies.
- **Containerization**: Many orchestration tools support running tasks in containers, facilitating consistent environments.
- **Monitoring and Logging**: Track the status of tasks and log outputs for debugging and auditing.

Orchestration tools often provide support for writing pipelines in some way.
However, the problem with most orchestration tools is that they force you to write your pipeline logic in their own specific way.
This leads to that as a user, you are solving two problems at once: the domain problem (i.e., your actual data processing logic) and the orchestration problem (i.e., how to run and schedule your pipeline).
This can lead to complex, hard-to-maintain codebases where the pipeline logic is tightly coupled with the orchestration logic.

For example, if we take a look at Kubeflow's [tutorial on building a ML pipeline](https://www.kubeflow.org/docs/components/pipelines/user-guides/core-functions/build-advanced-pipeline/), we can see that the user has to think about the domain logic (i.e., the ML tasks) as well as how to define the pipeline using Kubeflow's specific constructs (e.g., components, pipelines, etc.).
A data scientist reviewing this code (e.g. to check for statistical soundness) would have to understand both the ML domain as well as the specifics of Kubeflow's pipeline definitions.

## How Ordeq helps

Ordeq aims to solve this problem by allowing you to define your pipeline logic independently of the orchestration tool.
This means that you can focus on writing clean, maintainable code for your data processing tasks without worrying about the specifics of how the pipeline will be executed and scheduled.
You can then easily integrate your Ordeq pipelines with various orchestration tools as needed, without changing the core logic of your pipelines.

This separation of concerns leads to more modular, reusable, and testable code, making it easier to maintain and evolve your data processing workflows over time.
As a bonus, this also allows you to switch between different orchestration tools with minimal changes to your pipeline code.

## Open-source integrations

[![Kubeflow](https://avatars.githubusercontent.com/u/33164907?s=280&v=4)](./kubeflow.md)
