# Planning 2025 MVP of KATKE

**Notes:**
- **One-pass rendering** is an absolute priority, for enabling rather deterministic and explicit behaviour
- **Variable names** and code flows should **should be clear** within reason 
- **No speculative implementation**

## Table of Contents
- [Planning 2025 MVP of KATKE](#planning-2025-mvp-of-katke)
  - [Table of Contents](#table-of-contents)
  - [Implementation Roadmap](#implementation-roadmap)
    - [Stage 1: Font Rendering and Hard-Coded Character Box and Keyboard Cursor Navigation](#stage-1-font-rendering-and-hard-coded-character-box-and-keyboard-cursor-navigation)
    - [Stage 3: Hard-Coded Character Placement](#stage-3-hard-coded-character-placement)
    - [Stage 4: Continuous Drawing Mode](#stage-4-continuous-drawing-mode)
    - [Stage 5: Character Overwriting System](#stage-5-character-overwriting-system)
  - [First MVP Step](#first-mvp-step)
  - [Strategic Development Approach](#strategic-development-approach)
    - [How Will This Integrate to KATKE as it Matures?](#how-will-this-integrate-to-katke-as-it-matures)
    - [The Vision Connection](#the-vision-connection)
  - [Technical Implementation Plan](#technical-implementation-plan)
    - [Core Features](#core-features)
    - [Assembly Architecture](#assembly-architecture)
    - [Layering System](#layering-system)
  - [Advanced and Intuitive UI Systems](#advanced-and-intuitive-ui-systems)
    - [Philosophy: Hardened Intuitive UI](#philosophy-hardened-intuitive-ui)
    - [Context-Aware UI](#context-aware-ui)
  - [Success Metrics](#success-metrics)
  - [Research Questions](#research-questions)

## Implementation Roadmap

### Stage 1: Font Rendering and Hard-Coded Character Box and Keyboard Cursor Navigation

**Sub-Stages:**

1. **Custom Bitmap Font Rendering:**
   - Implement custom bitmap character rendering using boolean arrays for pixel-perfect control
   - **Future Implications:** We should consider whether to at an unspecified time in the future create a custom font creator integrated to KATKE, for our propietary format,
   - [x] ***COMPLETED:*** 2025-5-30

2. **Render a Row of Characters:**
   - Render a row of characters as decided by a one-dimensional binary bitmap array
   - Spacing of characters choosable in pixels
   - [x] ***COMPLETED:*** 2025-5-30

3. **Render a Grid of Characters**
   - Render a grid of characters as decide by a two-dimensional binary bitmap array
   - You choose the spacing of the characters both for the vertical and hozintal axis
   - [x] ***COMPLETED:*** 2025-5-30

4. **Boolean Bitmap Inversion Function:**
   - Implement general purpose `invert_boolean_bitmap()` function for any-dimensional bitmaps
   - Supports 0D (single boolean), 1D, 2D, and higher dimensional bitmap inversion
   - Foundation for cursor color inversion functionality for displaying the blinking cursor box
   - [x] ***COMPLETED:*** 2025-5-31

5. **Unified Multi-Dimensional Character Grid Bitmap Rendering System:**
   - Unified `render_character_grid_bitmap()` to handle 0D (single character), 1D (row), and 2D (grid) rendering through a single interface
   - Takes character bitmaps instead of binary True or False as elements within grid bitmpas. This will enable for us to flexibly, and precisely handle character rendering, as we move towards implementing more abstracted and functional character grids.
   - **DEPRECATED FUNCTION: `render_character_row_bitmap()`**
   - [x] ***COMPLETED:*** 2025-5-31

6. **Implement Advanced Character Row Manager With Cursor Position Support:**
   - Implement `manager_character_row(screen_surface, character_dictionary, character_row_bitmap, cursor_position_index, cursor_blink_toggle_time_ms, spacingbetween_characters_horizontal, spacing_between_characters_vertical, begin_position_horizontal, begin_position_vertical)`
     - The cursor is a blinking box style, levereging `invert_boolean_bitmap()`
     - Leverages `render_character_grid_bitmap()` for actual downstream rendering
     - Handles cursor blinking timing, etc
   - **Future Considerations** like happened with the `render_character_row_bitmap()` this will likely be deprecated in the near future, in favour of a more unified system

7. **Basic Text Cursor Movement via Keyboard Input:**
   - Move text cursor with keyboard arrow keys
     - Moving within the character row constrains

### Stage 3: Hard-Coded Character Placement

**Sub-Stages:**
1. **Display a Hard-Coded Character at a Specified Position:**
   - Display a hard-coded character (like "#") at a position specified before application launch.
2. **Place a Character Text Cursor Postion**
   - Place a hard-coded character at the text cursor position when the user pressed the "spacebar"

### Stage 4: Continuous Drawing Mode

**Sub-Stages:**
1. **Toggle an Indicator by Pressing "E"**
   - Enable/disable with specific key (maybe 'E' for continious mode toggle)
   - Visual indicator showing when continuous mode is active
2. **Actual Continuous Drawing Mode Implementation**
- Based on toggle status automatically place characters where the text cursor is, even when it moves

### Stage 5: Character Overwriting System

**Sub-Stages:**
1. **More Characters - Freedom!**
   - Introduce second character option (like '*' alongside '#', and of course space ' ')
   - Key to switch between the two character types (maybe mapped to "1", "2" and "0" on keyboard)
2. **Overwriting characters**
   - Any new character placement on top of an old one overwrites whatever was previously at that position

## First MVP Step

One might think we should focus on creating a usable text editor first. *But we choose to think different!*

We will be making an ASCII art creator first. This will be our very first "full" feature.

**Why?**

The ASCII art creator serves as our very first UX innovation experiment - as a low-stakes environment for discovering and refining the cutting-edge interaction standards that will define KATKE's approach to making coding genuinely fun and intuitive.

**Strategic Rationale:**
- **UX Research Experiment**: We need to learn how to create novel, delightful interactions before applying them to the complexities of a full development environment
- **Immediate Coding Relevance**: ASCII art directly serves core development workflows - quickly creating on-the-go diagrams, flowcharts, system architecture sketches, and visual documentation that renders natively across practically all platforms
- **Low-Stakes Innovation**: We can experiment with radical interface ideas without the pressure of dealing with existing coding conventions
- **Demonstration of Capability**: Proves our ability to create tools that feel fundamentally different and more engaging than conventional modern software

By choosing this as our first experiment, we do not need to immediately begin worrying about file browsing, syntax highlighting, or project management.

We can initially offer a powerful "scratchpad" from which people can copy ASCII art as needed, while we discover and hone what makes interfaces feel magical.

This experiment will demonstrate our commitment to redefining developer experiences through genuinely innovative interaction design.

## Strategic Development Approach

### How Will This Integrate to KATKE as it Matures?

The ASCII art creator will exist as a native extension within KATKE - clearly part of the application but intentionally--at least initially--using proprietary approaches and remaining somewhat disconnected from other components. This "everything a bit disconnected" approach is deliberate, allowing for:

- **Exploration Over Integration**: We need space to discover new paradigms before architecting them into cohesive systems
- **Learning Through Making**: The most important insights will emerge from building and using, not from theoretical design
- **Freedom to Innovate**: Disconnected components allow us to chase promising discoveries without breaking existing functionality

### The Vision Connection

Work done on the ASCII art creator will contribute to our larger goal of creating a "newspaper-inspired" development environment that rivals Scratch's intuitiveness while producing production-grade results. The spatial reasoning, assembly management, and layering concepts we develop will inform how we approach:

- Code organization and navigation
- Project structure visualization
- Multi-file editing workflows
- Visual programming elements

## Technical Implementation Plan

### Core Features

Everything keyboard and mouse mapped, based on preference. Accessibility will be somewhat of a priority, though not an overwhelming one yet.

- **Brush Stroke Tools**
  - **Types:**
    - Basic brush with adjustable size and character sets
    - Eraser (probably built similarly to the basic brush)
    - Intelligent brush for contextual characters (diagonal connectors, corners, etc.)
  - These will aim to feel amazing, being the default tools

- **Miscellaneous Tools**
  - **Types:**
    - Paint bucket

- **Shape Creation Tools**
  - **Types:**
    - Rectangle creator (square and rectangular forms)
    - Circle creator with proper ASCII approximation
    - Arc creator for complex diagrams

- **Text Creation Tools**
  - **Types:**
    - Basic label/text creator and modifier

- **Manipulation Tools**
  - **Types:**
    - Move complete assemblies as units
    - Move assembly anchor points for resizing
    - Move individual elements (breaks assembly relationships)
    - Delete assemblies tool

### Assembly Architecture

Everything in the ASCII art creator canvas is an "assembly" - a coherent unit that maintains its identity and relationships even when partially obscured or modified.

**Assembly Characteristics:**
- **Layered by Default**: A rectangle assembly remains a complete rectangle even when other elements are drawn over it
- **Keyboard Accessible**: Every assembly and operation is fully keyboard-navigable
- **Implicit Intelligence**: Assemblies understand their context and can be manipulated intuitively
- **Breakable Structure**: Assemblies can be dissolved into individual character elements when needed

### Layering System

**Intuitive Depth Management:**
- **"Transparent" as a Distinct Element/Character State**: "Transparent" elements don't interfere with underlying layers - they remain transparent
- **Assembly Panel**: Visual interface for adjusting layer order and assembly relationships
  - Also supports grouping assemblies for easier management
- **Drag-Through Capability**: Complete assemblies can be pulled out from under other elements without pixel-by-pixel editing

The goal is extreme intuitiveness - enabling complex diagram creation in under 30 seconds through natural, discoverable interactions.

## Advanced and Intuitive UI Systems

### Philosophy: Hardened Intuitive UI

The ASCII art creator will employ an advanced yet purposeful hardened UI system, creating an interface that collaborates with the user rather than simply responding to commands.

### Context-Aware UI

**Hierarchical X-Ray Vision:**
- **On-Demand**: When required or relevant, users can see "through" layers in a hierarchically logical manner, allowing for viewing elements behind others as they exist in the layering system
- **Powered by Smart Transparency**

**Non-ASCII UI Elements:**
- **Content vs. Guidance Distinction**: Clean ASCII output remains exportable while guiding elements (wireframes, crosshairs, alignment guides) exist in a separate paradigm
- **Operation-Specific Visualization**: Each tool reveals its own contextual visual language, for example:
  - Box creation can show alignment grids and snap points
  - Text placement can show guides
  - Arc creation can show radius center and curve non-rasterized previews
  - Delete operations can flash targeted elements for precision confirmation, and also show in X-ray for seeing all effects

**Highlighting:**
- **Text Background Color Selection**: Enables more intuitive features, such as highlighting selected elements with yellow, or elements with red highlights when hovering with the delete tool enabled

**Adaptive Guide Systems:**
- **Intelligent Crosshairs**: Advanced crosshair functionality that adapts to current tool and context
- **Arbitrary Line Drawing**: Support for drawing alignment guides and structural helpers
- **Assembly-Aware Snapping**: Grid overlays and snap guides that understand assembly boundaries and relationships

**Contextual Intelligence:**
- **Present When Needed**: Visual aids appear precisely when they add value to the current operation--or they can be nearly completely disabled
- **Out of the Way**: Structural elements hide gracefully when focus should be on content creation

This creates an interface that feels intuitive - revealing exactly what users need to see, when they need to see it, without creating visual overwhelm. The system becomes a collaborative partner in the creative process.

## Success Metrics

**30-Second Diagram Goal**: A developer should be able to create a reasonably complex system diagram from scratch in under 30 seconds using intuitive, keyboard-accessible commands.

This metric drives every design decision and validates our approach to making development tools that feel genuinely different - fast, fun, and friction-free.

## Research Questions

As we build, we're exploring fundamental questions about interface design:
- How should spatial manipulation feel when everything is character-based?
- What makes assembly selection and modification feel natural?
- How can layering be both powerful and intuitive?
- What interaction patterns make tool switching feel seamless?
- How can contextual visual intelligence enhance creativity without creating distraction?
- What makes an interface feel collaborative rather than merely responsive?

These discoveries will inform KATKE's entire approach to reimagining development environments.

The ASCII art creator isn't just our first feature - it's our laboratory for discovering what coding tools could become.
