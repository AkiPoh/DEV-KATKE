# KATKE

The goal of KATKE is to redefine what modern programming looks like. Our goal is to make programming intuitive, powerful and flexible.

KATKE will be an app that seamlessly integrates code editing, compilation, deployment and various other features through an intuitive interface.

We intend to employ, enhance, and augment existing solutions wherever possible, building upon established foundations like Python, Markdown, and Git.

**Table of Contents:**

- [KATKE](#katke)
  - [Project Status of KATKE](#project-status-of-katke)
  - [License of KATKE](#license-of-katke)
  - [Tech Architecture of KATKE](#tech-architecture-of-katke)
  - [Planned Roadmap for KATKE](#planned-roadmap-for-katke)
    - [First Major Alpha Release of KATKE, (Targeting: End of 2025 Q3), (v0.0.0)](#first-major-alpha-release-of-katke-targeting-end-of-2025-q3-v000)
    - [Second Major Alpha Release of KATKE, (Targeting: End of 2025 Q4), (v1.0.0)](#second-major-alpha-release-of-katke-targeting-end-of-2025-q4-v100)
  - [Our Current Vision for KATKE](#our-current-vision-for-katke)
    - [Core Principles for KATKE](#core-principles-for-katke)
    - [Target Audience for KATKE](#target-audience-for-katke)
    - [Philosophy Behind Our Development Practices for KATKE](#philosophy-behind-our-development-practices-for-katke)
    - [Looking Ahead: LTS Editions of KATKE](#looking-ahead-lts-editions-of-katke)
    - [`main` Branch Development Practices for KATKE](#main-branch-development-practices-for-katke)
  - [Communication Channels for KATKE and Contributing to KATKE](#communication-channels-for-katke-and-contributing-to-katke)
    - [Official Communication Channels for KATKE](#official-communication-channels-for-katke)
    - [Contributing to KATKE](#contributing-to-katke)
  - [TODO for this `README.md`](#todo-for-this-readmemd)

## Project Status of KATKE

**CURRENTLY IN EARLY DEVELOPMENT / UNVERIFIED**

**Current status**: Project is in its very initial development and planning phase. We currently have really nothing concrete to show you guys--but we hope for that to change in the near-future.

## License of KATKE

KATKE is a permissive open-source project licensed under the Apache 2.0 license.

## Tech Architecture of KATKE

- `python` (version: 3.13.3)
  - **Purpose:** Serves as the "core"
  - **Rationale**: Python offers unmatched flexibility and velocity for building complex middleware tools and apps. Though future versions of KATKE may transition to Rust for performance and consistency with our priorities. Currently Python's mature ecosystem and rapid prototyping capabilities make it the pragmatic choice for these crucial early stages.
  - **Docs:** https://docs.python.org/3.13/
- `pygame-ce` (version: 2.5.3)
  - **Purpose:** Serves as the "frontend-framework"
  - **Rationale**: After evaluating frameworks like Electron and Flet, we found them too constraining for our vision. We need pixel-perfect control and the freedom to craft custom UI behaviors that make development not just efficient, but enjoyable. Pygame-ce provides the low-level control and deterministic behavior essential for building the innovative interface we envision.
  - **Docs:** https://pyga.me/docs/
- `uv`
  - **Purpose:** Serves as the "python package and project manager"
  - **Docs:** https://docs.astral.sh/uv/

## Planned Roadmap for KATKE

### First Major Alpha Release of KATKE, (Targeting: End of 2025 Q3), (v0.0.0)

Our very first (major) Alpha release. Demonstrating at least some level of polished functionality; and demonstrating our vision for what's to come.

Currently we plan for this version to be a light-weight but relatively powerful ASCII Art Creator that is especially optimized for quickly creating inline diagrams for code documentation.

### Second Major Alpha Release of KATKE, (Targeting: End of 2025 Q4), (v1.0.0)

Our second major Alpha release. Demonstrating that we can scale.

Currently we plan for this version to build upon our previous versions by integrating a new light-weight code editor for Python and Markdown with *some* more powerful and novel features, especially focused on powering a more intuitive programming experience.

We intend to also integrate a light-weight approach to running Python programs and displaying Markdown files in a rendered format.

## Our Current Vision for KATKE

A code editor not too different from a newspaper in looks and feel. Designed to be intuitive, while not being restrictive. Designed to be an integrated solution from code writing, to project compilation and deployment--while not restricting developers' capability to use other external tools for maximum flexibility. Being initially focused on supporting Python based programming and Markdown based documentation--while ensuring intuitiveness that rivals beginner visual programming languages like Scratch, while producing production-grade solutions.

### Core Principles for KATKE

1. **Pixel-Perfect Control**: Every visual element serves a purpose and behaves predictably
2. **Deterministic Behavior**: Same input, same output, always
3. **Reproducibility First**: Projects should work identically across time and machines
4. **Joy in Development**: Tools should make programming feel creative and fun, not tedious
5. **Innovation is Necessary**: We'll choose to enhance or not-employ existing conventions when such leads to a better developer experience

### Target Audience for KATKE

KATKE is being built for:
- **Beginners and Students** who find current tools intimidating but want to use a tool capable of achieving professional results
- **Experienced developers** frustrated by the friction in existing workflows
- **Teams** needing reproducible and enjoyable development environments and tooling without significant overhead

### Philosophy Behind Our Development Practices for KATKE

We believe in continuous innovation. This means we prioritize breakthrough features over maintaining legacy code. By extension, we believe that backwards compatibility on the `main` branch version is not a major priority--due to the need to have the flexibility required to innovate with low-friction, and not be limited by past decisions, that might not fit our and our users' modern needs the best.

**We believe true and transparent reproducibility comes from using the same tool version, the same way, to achieve the same outcome.** We intend to provide native solutions to enable such rapid version hopping between tool versions, to ensure smooth usage experience for project developers, across multiple projects.

### Looking Ahead: LTS Editions of KATKE

Looking ahead, when the time is right to begin implementing such routine. Every two years we plan to initiate a new LTS edition branch off of the `main` branch that will receive indefinite support. This approach allows us to maintain momentum and agility on the `main` branch. This also ensures we can offer tooling that serves the need for longer supported versions with relevant security updates for longer projects.

Cross compatibility between LTS editions will not be a priority. But for updates within a specific LTS branch backwards and forwards compatibility is an absolute priority.

### `main` Branch Development Practices for KATKE

We employ squash merges exclusively for the `main` branch of this project on our GitHub repository (https://github.com/KATKE-GROUP/KATKE). Every merge represents a complete unit--code, documentation, tests--all fully up-to-date for that specific commit. This ensures every commit on `main` is a coherent and logical snapshot of the project.

## Communication Channels for KATKE and Contributing to KATKE

### Official Communication Channels for KATKE

All discussion currently happens through GitHub in our repository (https://github.com/KATKE-GROUP/KATKE):
- **GitHub Issues**: For bugs, features, and general discussion
- **GitHub Pull Requests**: For code contributions and reviews

### Contributing to KATKE

We welcome contributions. If you wish to contribute to KATKE please consider opening a GitHub Issue first to discuss your contribution ideas and how they fit into the wider project and its priorities before contributing.

We intend to swiftly respond to any Issues and Pull Requests opened in our GitHub repository (https://github.com/KATKE-GROUP/KATKE).

As this project (KATKE) matures we will especially focus on making this an amazing project to contribute to for all kinds of contributors.

## TODO for this `README.md`

- [ ] Add "practical" section on installing KATKE
- [ ] Add "practical" section on setting up a dev environment for working on developing KATKE
- [ ] Add "reference" section "Why KATKE?"
