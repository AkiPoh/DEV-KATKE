# Planning 2025 v0 of KATKE

**First Major Alpha Release of KATKE, (Targeting: End of 2025 Q3), (v0.0.0)**

Our very first (major) Alpha release. Demonstrating at least some level of polished functionality; and demonstrating our vision for what's to come.

Currently we plan for this version to be a light-weight but relatively powerful ASCII Art Creator that is especially optimized for quickly creating inline diagrams for code documentation.

**Table of Contents**

- [Planning 2025 v0 of KATKE](#planning-2025-v0-of-katke)
  - [Notes:](#notes)
  - [New Implementation Roadmap](#new-implementation-roadmap)
    - [1. Unified Character Grid Rendering System](#1-unified-character-grid-rendering-system)
  - [Old Implementation Roadmap](#old-implementation-roadmap)
    - [Stage 1: Font Rendering and Hard-Coded Character Box and Keyboard Cursor Navigation](#stage-1-font-rendering-and-hard-coded-character-box-and-keyboard-cursor-navigation)
    - [Stage 3: Hard-Coded Character Placement](#stage-3-hard-coded-character-placement)
    - [Stage 4: Continuous Drawing Mode](#stage-4-continuous-drawing-mode)
    - [Stage 5: Character Overwriting System](#stage-5-character-overwriting-system)

## Notes:

- **One-pass rendering** is an absolute priority, for enabling rather deterministic and explicit behaviour
- **Variable names** and code flows should **should be clear** within reason 
- **No speculative implementation**
- ***MONOLITHIC CODING IS THE FUTURE 100%*** (jk, but only kinda)

## New Implementation Roadmap

### 1. Unified Character Grid Rendering System

## Old Implementation Roadmap

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
