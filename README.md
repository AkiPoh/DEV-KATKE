# KATKE

**CURRENTLY IN EARLY DEVELOPMENT / UNVERIFIED**

The goal of KATKE is to redefine how modern coding tools function.

KATKE will be an app that seamlessly integrates code editing, compilation, and deployment through an intuitive interface--bringing the cohesiveness of modern creative tools to software development.

We intend to employ, enhance, and augment existing solutions wherever possible, building upon established foundations like Rust, Python, Git, and semantically correct project structures.

KATKE is a permissive open-source project licensed under the Apache 2.0 license.

## Our Current Development Philosophy for KATKE

We believe in continuous innovation.  By extension, we believe that backwards compatability on the "main" branch version is not a major priority--due to the need to have the flexibility required to innovate with low-friction, and not be limited by past decisions, that might not fit our and our users modern needs the best.

We believe true and transparent reproducibility comes from using the same tool version, the same way, to achieve the same outcome. We intend to with native solutions to enable such rapid version hopping between tool versions, to ensure smooth usage experience for project developers, across multiple projects.

Looking ahead, we current to in the future to employ bi-annual LTS "branch" edition "fork" releases that will receive indefinite support. This approach allows us to maintain momentup and agility on the "main" branch. While ensuring we can offer tooling that that serves the need for longer (especially security update) supported versions for longer projects.

Cross compatability between LTS editions will not be a priority. But for *updates* on specific LTS editions backwards and forwards compatability is an absolute priority.

## REFERENCE-TABLE: Table of Contents

- [KATKE](#katke)
  - [Our Current Development Philosophy for KATKE](#our-current-development-philosophy-for-katke)
  - [REFERENCE-TABLE: Table of Contents](#reference-table-table-of-contents)
  - [REFERENCE: The Current Project Status for KATKE](#reference-the-current-project-status-for-katke)
  - [REFERENCE: Our Current Roadmap for KATKE](#reference-our-current-roadmap-for-katke)
  - [REFERENCE: Our Current Vision for KATKE](#reference-our-current-vision-for-katke)
  - [REFERENCE: Tech Architecture](#reference-tech-architecture)
  - [REFERENCE: Contributing to KATKE](#reference-contributing-to-katke)
  - [REFERENCE: License](#reference-license)
  - [REFERENCE: TODO for this `README.md`](#reference-todo-for-this-readmemd)

## REFERENCE: The Current Project Status for KATKE

**Current status**: Project is in its very initial development and planning phase. We currently have really nothing concrete to show you guys--but we hope for that to change in the near-future.

## REFERENCE: Our Current Roadmap for KATKE

- **2025 Q4**: Our first official Alpha release demonstrating at least some level of functionality; and demonstrating our vision for what's to come

## REFERENCE: Our Current Vision for KATKE

A code editor not too different from a newspaper in looks and feel. Designed to be intuitive, while not being restrictive. Designed to be an integrated solution from code writing, to project compilation and deployment--while not restricting developers' capability to use other external tools for maximum flexibility. Being initially focused on supporting Rust based programming and Markdown based documentation--while ensuring intuitiveness that rivals beginner visual programming languages like Scratch, while producing production-grade solutions.

## REFERENCE: Tech Architecture

- `python` (version: 3.13.3)
  - **Purpose:** Serves as the "core"
  - **Rationale**: Python offers unmatched flexibility and velocity for building complex middleware tools and apps. Though future versions of KATKE may transition to Rust for performance and consistency with our priorities. Currently Python's mature ecosystem and rapid prototyping capabilities make it the pragmatic choice for these crucial early stages.
  - **Docs:** https://docs.python.org/3.13/
- `pygame-ce` (version: 2.5.3)
  - **Purpose:** Serves as the "frontend-framework"
  - **Rationale**: After evaluating frameworks like Electron and Flet, we found them too constraining for our vision. We need pixel-perfect control and the freedom to craft custom UI behaviors that make development not just efficient, but enjoyable. Pygame-ce provides the low-level control and deterministic behavior essential for building the innovative interface we envision.
  - **Docs:** https://pyga.me/docs/

## REFERENCE: Contributing to KATKE

We welcome contributions. If you wish to contribute to KATKE please consider opening a GitHub Issue first to discuss your contribution ideas and how they fit into the wider project and its priorities before contributing.

We intend to swiftly respond to any Issues and Pull Requests opened in our GitHub repository (https://github.com/KATKE-GROUP/KATKE).

As this project (KATKE) matures we will especially focus on making this an amazing project to contribute to for all kinds of contributors.

## REFERENCE: License

KATKE is a permissive open-source project licensed under the Apache 2.0 license.

## REFERENCE: TODO for this `README.md`

- [ ] Add "practical" section on installing KATKE
- [ ] Add "practical" section on setting up a dev environment for working on developing KATKE
