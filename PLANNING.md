# Planning 2025 MVP of KATKE

## First MVP step

One might think we should focus on creating an usable text editor first. I do not agree with that appoach.

We should be making an ASCII art editor first. That should be our initial feature.

**Why?**

Cause its immidiate, low stakes, and also helps us create a solid text editor first with advanced text modification features from the first day.

We do not need to immidietely begin to start worrying about file browsing, etc. We can just initially offer a quick "scratchpad" from which people can copy the ASCII art as they wish.

This will help demonstrate the prowess of pygame and Python in creating a complex application easily.

## So Actual Plan

### Features

- Brush
  - Basic brush, size adjustable, etc
- Fancy brush for select characters
  - Handles proper characters, for drawing for example "diagnals", etc,
  - ~single character width
- Rectance creator
  - Square box
  - Rectangle
- Circle creator
  - Circle
- Arc cretor
- Basic textbox/textwriter
- Erased
  - Needs thought
- Paint bucket
  - Needs thought
- Move
  - Move whole assemblies
  - Move individual pixels (implicitly breaks the assembly)
  - Move individual assembly points

Everything is an assembly and keayboard mapped too.

An assembly can be for example anything from a squate to a circle drawn using the Available tools. This assembly structure allows for easy editing and resizing of common objects, etc.

An assembly uses an implicity layered approach. By default a rectangle assembly is a full rectange assembly, even if parts of it are behind other characters, the full assembly can be dragged out from under them.

Assemblies can be broken to an individual characters too. Though still that individual character is an assembly.

A panel is available from which the user can see and adjust assembly layer positions.

Though as previosly established such would often be unnecessary due to the intuitive nature and easily commandable layered approach.

Unlike some other situation a "none" will be a valid character "unit" for us. None defaults to none changes applied, no affect on below or above layers. So if a pixel thoughout layers is defined as none, it'll be left as a space, or respective default character.

The goal is for everything to be extremely intuitive, enabling fast and universal behaviour.

The dream is to make it possible to create a relatively complex diagram in under 30 seconds, basically on the fly.

Enhancing the developer experience by offering native tooling for such.
