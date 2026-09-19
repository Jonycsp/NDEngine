# NDEngine Roadmap

This document outlines the planned development of NDEngine.

The roadmap is intentionally flexible. The order and scope of later phases may change as the project develops and new mathematical or technical ideas emerge.

---

## Phase 0 — Foundation

- [x] Create project repository
- [x] Establish project structure
- [x] Connect local repository to GitHub
- [x] Add MIT license
- [x] Establish testing workflow
- [x] Establish changelog workflow

---

## Phase 1 — Mathematical Core

Build the underlying transformation system independently of the renderer.

- [x] Define N-dimensional point representation
- [x] Implement generic plane rotation
- [x] Test rotations against the Desmos prototype
- [x] Implement composition of rotations
- [ ] Generate all possible rotation planes for N dimensions
- [x] Establish coordinate-axis conventions
- [x] Establish rotation-direction conventions
- [x] Add mathematical unit tests

### Target

A small, reliable transformation system capable of rotating points in arbitrary dimensions.

---

## Phase 2 — Projection

Implement the mathematical process of reducing dimensionality.

- [ ] Implement orthographic projection
- [x] Implement perspective projection
- [x] Implement configurable projection distance
- [x] Implement N → N-1 projection
- [x] Compose multiple projection stages
- [x] Test 4D → 3D → 2D projection
- [ ] Investigate alternative projection methods

### Target

Transform a point in N dimensions into a 2D screen position through a configurable transformation and projection pipeline.

---

## Phase 3 — Basic 3D Rendering

Build the first minimal renderer.

- [ ] Establish screen coordinates
- [ ] Implement a camera
- [ ] Render points
- [ ] Render lines
- [ ] Render basic wireframe geometry
- [ ] Connect the mathematical core to the renderer
- [ ] Add basic interaction

### Target

Display and manipulate ordinary 3D geometry in real time.

---

## Phase 4 — 4D Visualization

Make 4D the first major showcase of the engine.

- [ ] Implement a tesseract
- [ ] Generate tesseract vertices algorithmically
- [ ] Generate tesseract edges algorithmically
- [ ] Implement 4D rotation controls
- [ ] Implement 4D → 3D projection
- [ ] Implement 3D → 2D rendering
- [ ] Add interactive 4D rotation
- [ ] Add projection-distance controls

### Target

A functioning interactive 4D visualization engine.

---

## Phase 5 — General Geometry

Expand beyond the tesseract.

- [ ] General point collections
- [ ] General edge representation
- [ ] Faces and higher-dimensional cells
- [ ] Cubes and hypercubes
- [ ] Spheres and hyperspheres
- [ ] Torus and higher-dimensional analogues
- [ ] Parametric geometry
- [ ] Custom geometry generation

### Target

A reusable geometry system rather than a collection of hard-coded demonstrations.

---

## Phase 6 — N-Dimensional Generalization

Remove unnecessary assumptions about dimensionality.

- [x] Arbitrary-dimensional points
- [x] Arbitrary-dimensional rotations
- [ ] Automatic rotation-plane generation
- [ ] Arbitrary-dimensional hypercubes
- [x] General N → N-1 projection
- [x] N-dimensional transformation pipelines
- [ ] N-dimensional object generation

### Target

4D becomes one natural case of a genuinely N-dimensional system.

> Several capabilities listed here are being implemented earlier as part of the mathematical core and projection phases. Phase 6 represents their broader integration and generalization rather than their first implementation.

---

## Phase 7 — Interactive Engine

Improve the engine as an experimentation environment.

- [ ] Camera controls
- [ ] Rotation controls
- [ ] Translation controls
- [ ] Projection controls
- [ ] Object selection
- [ ] Multiple simultaneous objects
- [ ] User interface
- [ ] Configuration system
- [ ] Save/load scenes
- [ ] Configurable dimensional controls.
- [ ] Mouse-based rotation controls.
- [ ] Precise rotation sliders for individual rotation planes.
- [ ] Continuous automatic rotation with configurable angular velocities.
- [ ] Enable or disable rotation planes according to the active dimensionality.

---

## Phase 8 — Rendering Improvements

Improve performance and visual quality after the architecture is stable.

- [ ] Profile performance
- [ ] Identify actual bottlenecks
- [ ] Introduce NumPy where useful
- [ ] Batch numerical operations
- [ ] Investigate GPU rendering if necessary
- [ ] Improve rendering quality
- [ ] Investigate depth ordering
- [ ] Investigate surfaces and shading

Optimization should be driven by measured bottlenecks rather than assumptions.

---

## Phase 9 — Presentation

Turn the engine into a polished interactive experience.

- [ ] Visual themes
- [ ] Clean interface
- [ ] Object browser
- [ ] Help / controls screen
- [ ] Configuration menu
- [ ] Optional ambient music
- [ ] Optional sound effects
- [ ] Screenshots and demonstrations
- [ ] GitHub documentation and examples

Ambient music and other presentation features should remain separate from the mathematical and rendering core.

---

## Phase 10 — Experimental Mathematics

Explore mathematical features that are interesting beyond the core engine.

- [ ] Alternative projection methods
- [ ] Stereographic projection
- [ ] Matrix-based transformations
- [ ] Rotation matrices
- [ ] Quaternions
- [ ] Higher-dimensional rotation representations
- [ ] Non-Euclidean geometry experiments
- [ ] Procedural higher-dimensional objects
- [ ] Mathematical visualization experiments

---

# Development Principles

### 1. Mathematics first

The mathematical transformation system should remain understandable independently of the renderer.

### 2. Generality where practical

If a feature can naturally operate in N dimensions, prefer a general implementation over separate 3D and 4D versions.

### 3. No premature optimization

Performance matters, but optimization should follow actual profiling and real requirements.

### 4. Test before expanding

New mathematical functionality should be tested before becoming a dependency for larger systems.

### 5. Small commits

Development should proceed in small, meaningful stages.

Typical workflow:

1. Design
2. Implement
3. Test
4. Fix
5. Update documentation
6. Update changelog
7. Commit
8. Push

### 6. Separate mathematics from rendering

The visualization layer should consume the mathematical engine rather than define it.

---

# Long-Term Vision

NDEngine should eventually make it possible to define, transform, project, and visualize geometry in arbitrary dimensions without requiring separate implementations for every dimensionality.

The 4D engine is the first major milestone.

It is not necessarily the final destination.