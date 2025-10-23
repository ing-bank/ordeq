# Adding integrations

Ordeq is designed to integrate seamlessly with the other tooling.
The level of integration can vary from examples in the documentation to fully-fledged extensions that are maintained as part of the Ordeq repository.

Here are the different levels of integrations, from least to most integrated:

1. **User customizations**: Implemented and maintained in the users' own codebases.

    - _Examples_: custom IOs or hooks.

1. **Documented examples**: Integrations that are documented in the Ordeq documentation.

    - _Examples_: Streamlit and Docker integration guide.

1. **IO extensions**: Integrations that extend the IO packages of Ordeq.

    - _Examples_: `ordeq-pandas`, `ordeq-polars`. See the [packages overview][packages].

1. **Framework extensions**: Integrations that extend framework functionality of Ordeq.

    - _Examples_: `ordeq-viz` and `ordeq-cli-runner`. See the [packages overview][packages].

1. **Core framework**: Reusable components that are added to the Ordeq core framework.

    - _Examples_: hooks.

When deciding the level of integration, we evaluate the following criteria:

- **Generality**: Is the integration useful for a broad audience?
- **Community interest**: Is there a demand or interest from the community for this integration?
- **Complexity**: How much complexity does the integration add to the codebase?
- **Maintenance**: Can we maintain the integration over time?

A favourable score on these criteria results in a higher level of integration.

!!! question "Not sure where to start?"

    If you're unsure about the appropriate level of integration for your use case, please reach out to us on [GitHub][issues]

[issues]: https://github.com/ing-bank/ordeq/issues/new
[packages]: ../packages.md
