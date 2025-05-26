# KATKE

**CURRENTLY IN EARLY DEVELOPMENT / UNVERIFIED**

The goal of KATKE is to redefine how modern coding tools function.

[What KATKE will actually be; an app-style tool, combining a code editor, compilation, intuitive UI, etc..]

We intend to wherever possible employing, enhancing and augmenting existing solutions such as Rust, Python, Git, semantically correct project file structures, etc.

KATKE is a permissive open-source project licensed under the Apache 2.0 license.

[Explaining how we are not fearful of innovation; we intend to break backwards compatability continually thoughout the development process, we believe the best way to ensure project and tool compatability is to use the original version of the tool, for reproducable workflows; we intend in the future to approximately bi-annually release LTS editions, which will receive support indefinetely, though no cross compatability between LTS versions should be expected... the reason for this that in combination of using pre-existing solutions, we will also integrate a lot of our own workflow configurations, project workspace configuration, etc into a project. Due to our philosophy of ensuring reproductability and relatively concistent development enviroments]

## REFERENCE-TABLE: Table of Contents

- [KATKE](#katke)
  - [REFERENCE-TABLE: Table of Contents](#reference-table-table-of-contents)
  - [REFERENCE: Project Status](#reference-project-status)
  - [REFERENCE: Our Current Roadmap for KATKE](#reference-our-current-roadmap-for-katke)
  - [REFERENCE: Our Current Vision for KATKE](#reference-our-current-vision-for-katke)
  - [REFERENCE: Tech Architecture](#reference-tech-architecture)
  - [REFENCE: Contributing to KATKE](#refence-contributing-to-katke)
  - [REFERENCE: License](#reference-license)
  - [REFERENCE: TODO for this `README.md`](#reference-todo-for-this-readmemd)

## REFERENCE: Project Status

**Current status**: Project is in its very initial development and planning phase.

## REFERENCE: Our Current Roadmap for KATKE

- **2025 Q4**: Our first official Alpha release demonstrating at least some level of functionality; and demonstrating our vision for what's to come

## REFERENCE: Our Current Vision for KATKE

A code editor not too different from a newspaper in looks and feel. Designed to be intuitive, while not being restrictive. Designed to be an integrated solution from code writing, to project compilation and deployment--while not restricting developers' capability to use other external tools for maximum flexbility. Being initially focused on supporting Rust based programming and Markdown based documentation--while ensuring intuitiveness that begins to rival visual programming languages like Scratch.

## REFERENCE: Tech Architecture

- `python` (version: 3.13.3)
  - Serves as the "core"
  - [Chosen as the internal programming language for building at least the initial versions of KATKE. Due to Python's proven flexibility and rapid development capabilities for complex "middleware" tools. While we believe that in the future it will probably make sense to transition completely to a programming language like Rust for building KATKE; currently Python and its modern complimentary tooling best serve our needs for these initial stages]
  - Docs: https://docs.python.org/3.13/
- `pygame-ce` (version: 2.5.3)
  - Serves as the "frontend-framework"
  - [Chosen due to our need for pixel-perfect precision, and our need to have the ability to define custom UI behaviour to optimise our UI, make the workflw efficient, and ensure we can make a "fun" tool--we previosly considered frameworks like Electron, Flet, etc and found them not to fit our needs, due to us circling around to our believe in the need to have flexibility and deterministic behaviour in how we do things.]
  - Docs: https://pyga.me/docs/

## REFENCE: Contributing to KATKE

We welcome contributions. If you wish to contribute to KATKE please consider opening a GitHub Issue first to discuss your contribution ideas and how they fit into the wider project and its priorities before contributing--we intend to swiftly respond to any Issues and Pull Requests opened in our GitHub repository (https://github.com/KATKE-GROUP/KATKE).

Especially as this project (KATKE) matures we will focus on making this an amazing project contribute to for all kinds of contributors.

## REFERENCE: License

KATKE is a permissive open-source project licensed under the Apache 2.0 license.

## REFERENCE: TODO for this `README.md`

- [ ] Add "practical" section on installing KATKE
- [ ] Add "practical" section on setting up a dev enviroment for working on developing KATKE
