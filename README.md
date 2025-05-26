# KATKE

The goal of KATKE is to redefine how modern coding tools function.

KATKE will be an app that seamlessly integrates code editing, compilation, and deployment through an intuitive interface--bringing the cohesiveness of modern creative tools to software development.

We intend to employ, enhance, and augment existing solutions wherever possible, building upon established foundations like Rust, Python, Git, and semantically correct project structures.

KATKE is a permissive open-source project licensed under the Apache 2.0 license.

## REFERENCE: The Current Project Status for KATKE

**CURRENTLY IN EARLY DEVELOPMENT / UNVERIFIED**

**Current status**: Project is in its very initial development and planning phase. We currently have really nothing concrete to show you guys--but we hope for that to change in the near-future.

## REFERENCE-TABLE: Table of Contents

- [KATKE](#katke)
  - [REFERENCE: The Current Project Status for KATKE](#reference-the-current-project-status-for-katke)
  - [REFERENCE-TABLE: Table of Contents](#reference-table-table-of-contents)
  - [REFERENCE: Our Current Roadmap for KATKE](#reference-our-current-roadmap-for-katke)
    - [First Alpha Version (Targeting: 2025 Q4) of KATKE](#first-alpha-version-targeting-2025-q4-of-katke)
  - [REFERENCE: Our Current Vision for KATKE](#reference-our-current-vision-for-katke)
    - [REFERENCE: Core Principles for KATKE](#reference-core-principles-for-katke)
    - [REFERENCE: Target Audience for KATKE](#reference-target-audience-for-katke)
    - [REFERENCE: Tech Architecture for KATKE](#reference-tech-architecture-for-katke)
    - [REFERENCE: Our Current Development Practices for KATKE](#reference-our-current-development-practices-for-katke)
      - [REFERENCE: Philosophy Behind Our Current Development Practices for KATKE](#reference-philosophy-behind-our-current-development-practices-for-katke)
      - [REFERENCE: "Main" Branch Development Practices for KATKE](#reference-main-branch-development-practices-for-katke)
  - [REFERENCE: Communication Channels for KATKE and Contributing to KATKE](#reference-communication-channels-for-katke-and-contributing-to-katke)
    - [REFERENCE: Official Communication Channels for KATKE](#reference-official-communication-channels-for-katke)
    - [REFERENCE: Contributing to KATKE](#reference-contributing-to-katke)
  - [REFERENCE: License for the KATKE project](#reference-license-for-the-katke-project)
  - [REFERENCE: TODO for this `README.md`](#reference-todo-for-this-readmemd)

## REFERENCE: Our Current Roadmap for KATKE

### First Alpha Version (Targeting: 2025 Q4) of KATKE

Our first official Alpha release demonstrating at least some level of functionality; and demonstrating our vision for what's to come

**In This Version We Plan to Demonstrate:**
  - Basic text editing with first glimpses of our vision for a newspaper-inspired interface
  - Syntax highlighting for Rust
  - Project structure visualization
  - At least one "magical" and "fun" feature that shows why KATKE is different
  - Proof that Scratch-like intuitiveness and production-grade output can coexist

## REFERENCE: Our Current Vision for KATKE

A code editor not too different from a newspaper in looks and feel. Designed to be intuitive, while not being restrictive. Designed to be an integrated solution from code writing, to project compilation and deployment--while not restricting developers' capability to use other external tools for maximum flexibility. Being initially focused on supporting Rust based programming and Markdown based documentation--while ensuring intuitiveness that rivals beginner visual programming languages like Scratch, while producing production-grade solutions.

### REFERENCE: Core Principles for KATKE

1. **Pixel-Perfect Control**: Every visual element serves a purpose and behaves predictably
2. **Deterministic Behavior**: Same input, same output, always
3. **Reproducibility First**: Projects should work identically across time and machines
4. **Joy in Development**: Tools should make programming feel creative and fun, not tedious
5. **Innovation is Necessary**: We'll choose to enhance or not-employ existing conventions when such leads to a better developer experience

### REFERENCE: Target Audience for KATKE

KATKE is being built for:
- **Rust developers** seeking a more intuitive development experience
- **Beginners and Students** who find current tools intimidating but want to use a tool capable of achieving professional results
- **Experienced developers** frustrated by the friction in existing workflows
- **Teams** needing reproducible and enjoyable development environments and tooling without significant overhead

### REFERENCE: Tech Architecture for KATKE

- `python` (version: 3.13.3)
  - **Purpose:** Serves as the "core"
  - **Rationale**: Python offers unmatched flexibility and velocity for building complex middleware tools and apps. Though future versions of KATKE may transition to Rust for performance and consistency with our priorities. Currently Python's mature ecosystem and rapid prototyping capabilities make it the pragmatic choice for these crucial early stages.
  - **Docs:** https://docs.python.org/3.13/
- `pygame-ce` (version: 2.5.3)
  - **Purpose:** Serves as the "frontend-framework"
  - **Rationale**: After evaluating frameworks like Electron and Flet, we found them too constraining for our vision. We need pixel-perfect control and the freedom to craft custom UI behaviors that make development not just efficient, but enjoyable. Pygame-ce provides the low-level control and deterministic behavior essential for building the innovative interface we envision.
  - **Docs:** https://pyga.me/docs/

### REFERENCE: Our Current Development Practices for KATKE

#### REFERENCE: Philosophy Behind Our Current Development Practices for KATKE

We believe in continuous innovation. This means we prioritize breakthrough features over maintaining legacy code. By extension, we believe that backwards compatibility on the "main" branch version is not a major priority--due to the need to have the flexibility required to innovate with low-friction, and not be limited by past decisions, that might not fit our and our users modern needs the best.

We believe true and transparent reproducibility comes from using the same tool version, the same way, to achieve the same outcome. We intend to with native solutions to enable such rapid version hopping between tool versions, to ensure smooth usage experience for project developers, across multiple projects.

Looking ahead, we currently plan to employ bi-annual LTS "branch" edition "fork" releases that will receive indefinite support. This approach allows us to maintain momentum and agility on the "main" branch. While ensuring we can offer tooling that serves the need for longer (especially security update) supported versions for longer projects.

Cross compatibility between LTS editions will not be a priority. But for updates within specific LTS editions backwards and forwards compatibility is an absolute priority.

#### REFERENCE: "Main" Branch Development Practices for KATKE

We employ squash merges exclusively for the main branch of this project on our GitHub repository (https://github.com/KATKE-GROUP/KATKE). Every merge represents a complete unit--code, documentation, tests--all fully up-to-date for that specific commit. This ensures every commit on main is a coherent and logical snapshot of the project.

## REFERENCE: Communication Channels for KATKE and Contributing to KATKE

### REFERENCE: Official Communication Channels for KATKE

All discussion currently happens through GitHub in our repository (https://github.com/KATKE-GROUP/KATKE):
- **GitHub Issues**: For bugs, features, and general discussion
- **GitHub Pull Requests**: For code contributions and reviews

### REFERENCE: Contributing to KATKE

We welcome contributions. If you wish to contribute to KATKE please consider opening a GitHub Issue first to discuss your contribution ideas and how they fit into the wider project and its priorities before contributing.

We intend to swiftly respond to any Issues and Pull Requests opened in our GitHub repository (https://github.com/KATKE-GROUP/KATKE).

As this project (KATKE) matures we will especially focus on making this an amazing project to contribute to for all kinds of contributors.

## REFERENCE: License for the KATKE project

KATKE is a permissive open-source project licensed under the Apache 2.0 license.

## REFERENCE: TODO for this `README.md`

- [ ] Add "practical" section on installing KATKE
- [ ] Add "practical" section on setting up a dev environment for working on developing KATKE
- [ ] Add "reference" section on minimum viable functionality for Alpha release
- [ ] Add "reference" section "Why KATKE?"
