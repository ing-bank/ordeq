# Integration model

We follow an integration model to assess which integrations should be provided by Ordeq, and how.
We distinguish the following types of integrations:

1. User customizations: These are user-defined customizations that allow users to use Ordeq for their specific needs.
   Examples include custom IOs or hooks.
   These integrations are implemented by users themselves, using the Ordeq components, and maintained in the repository of the user.
2. Documented examples: These are integrations that are documented in the Ordeq documentation.
   They provide users with examples of how to use Ordeq with a popular tool, or how to set up an Ordeq project to suit certain needs.
   Examples include the Streamlit and Docker integration guide.
3. IO extensions: These are integrations that extend the IO packages of Ordeq.
   They provide users with generic and reusable IO to load and save data.
   Examples include integrations with databases, cloud storage, and file formats.
4. Framework extensions: These are integrations that extend the framework functionality of Ordeq.
   They provide users with additional features and capabilities.
   An example is `ordeq-viz`.
5. Core functionality: These are integrations that are part of the core framework.
   They are maintained as part of the  Ordeq repository and are considered essential for the operation of Ordeq.
   Examples include the IO and node components.

When considering new integrations, we evaluate them based on the following criteria:
