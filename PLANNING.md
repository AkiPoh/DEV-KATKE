# Planning 2025 MVP of KATKE

## First MVP step

One might think we should focus on creating a usable text editor first. We do not agree with that approach.

We will be making an ASCII art editor first. That should be our initial feature.

**Why?**

The ASCII art editor serves as our UX innovation laboratory - a controlled environment for discovering and refining the cutting-edge interaction paradigms that will define KATKE's approach to making coding genuinely fun and intuitive.

**Strategic Rationale:**
- **UX Research Lab**: We need to learn how to create novel, delightful interactions before applying them to the complexities of a full development environment
- **Immediate Coding Relevance**: ASCII art directly serves core development workflows - creating diagrams, flowcharts, system architecture sketches, and visual documentation that renders natively across all platforms
- **Low-Stakes Innovation**: We can experiment with radical interface ideas without the pressure of maintaining compatibility with existing coding conventions
- **Demonstration of Capability**: Proves our ability to create tools that feel fundamentally different and more engaging than conventional development software

We do not need to immediately begin worrying about file browsing, syntax highlighting, or project management. We can initially offer a powerful "scratchpad" from which people can copy ASCII art as needed, while we discover what makes interfaces feel magical.

This demonstrates our commitment to redefining developer experiences through genuinely innovative interaction design.

## Strategic Development Approach

### The Experimental Phase

The ASCII art tool will exist as a native extension within KATKE - clearly part of the application but intentionally using proprietary approaches and remaining somewhat disconnected from other components. This "everything a bit disconnected" approach is deliberate:

- **Exploration Over Integration**: We need space to discover new paradigms before architecting them into cohesive systems
- **Learning Through Making**: The most important insights will emerge from building and using, not from theoretical design
- **Freedom to Innovate**: Disconnected components allow us to chase promising discoveries without breaking existing functionality

### The Vision Connection

Every interaction pattern we discover in the ASCII art editor contributes to our larger goal of creating a "newspaper-inspired" development environment that rivals Scratch's intuitiveness while producing production-grade results. The spatial reasoning, assembly management, and layering concepts we develop will inform how we approach:
- Code organization and navigation
- Project structure visualization  
- Multi-file editing workflows
- Visual programming elements

## Technical Implementation Plan

### Core Features

- **Brush System**
  - Basic brush with adjustable size and character sets
  - Intelligent brush for contextual characters (diagonal connectors, corners, etc.)
  - Single character precision with assembly awareness

- **Shape Creation Tools**
  - Rectangle creator (square and rectangular forms)
  - Circle creator with proper ASCII approximation
  - Arc creator for complex diagrams
  - Basic textbox/text writer integration

- **Advanced Manipulation**
  - Eraser (requires research into intuitive erasing behavior)
  - Paint bucket (requires exploration of ASCII flood-fill patterns)
  - Move operations:
    - Move complete assemblies as units
    - Move individual elements (breaks assembly relationships)
    - Move assembly anchor points for resizing

### Assembly Architecture

Everything in KATKE operates as an "assembly" - a coherent unit that maintains its identity and relationships even when partially obscured or modified.

**Assembly Characteristics:**
- **Layered by Default**: A rectangle assembly remains a complete rectangle even when other elements are drawn over it
- **Keyboard Accessible**: Every assembly and operation is fully keyboard-navigable
- **Implicit Intelligence**: Assemblies understand their context and can be manipulated intuitively
- **Breakable Structure**: Assemblies can be dissolved into individual character elements when needed

### Layering System

**Intuitive Depth Management:**
- **"None" as Valid State**: Empty spaces don't interfere with underlying layers - they remain transparent
- **Assembly Panel**: Visual interface for adjusting layer order and assembly relationships  
- **Drag-Through Capability**: Complete assemblies can be pulled out from under other elements without pixel-by-pixel editing

The goal is extreme intuitiveness - enabling complex diagram creation in under 30 seconds through natural, discoverable interactions.

## Success Metrics

**30-Second Diagram Goal**: A developer should be able to create a reasonably complex system diagram from scratch in under 30 seconds using intuitive, keyboard-accessible commands.

This metric drives every design decision and validates our approach to making development tools that feel genuinely different - fast, fun, and friction-free.

## Research Questions

As we build, we're exploring fundamental questions about interface design:
- How should spatial manipulation feel when everything is character-based?
- What makes assembly selection and modification feel natural?
- How can layering be both powerful and intuitive?
- What interaction patterns make tool switching feel seamless?

These discoveries will inform KATKE's entire approach to reimagining development environments.

The ASCII art editor isn't just our first feature - it's our laboratory for discovering what coding tools could become.
