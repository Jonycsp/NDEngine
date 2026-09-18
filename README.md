# NDEngine

An experimental N-dimensional geometry and visualization engine written in Python.

NDEngine began as a mathematical prototype in Desmos, initially focused on 3D and 4D visualization. It is now being rebuilt as a proper Python engine with a more general architecture.

The long-term goal is to make higher-dimensional geometry feel as natural to work with as ordinary 3D geometry.

## Current Status

Early development.

The engine is currently being built from the mathematical core upward.

The first major target is a fully interactive 4D visualization engine, while keeping the underlying mathematics general enough to extend naturally to arbitrary dimensions.

## Goals

- Represent points and geometry in arbitrary dimensions.
- Implement generic rotations in any coordinate plane.
- Support composition of multiple rotations.
- Project higher-dimensional geometry into lower dimensions.
- Render 3D and higher-dimensional geometry interactively.
- Provide a foundation for experimenting with unusual geometric objects and projections.
- Eventually support arbitrary N-dimensional geometry.

## Design Philosophy

The project prioritizes mathematical clarity and architectural generality over premature optimization.

A solution that naturally works for N dimensions is preferred over separate implementations for 3D, 4D, 5D, etc. whenever practical.

Performance improvements will be introduced when they become useful rather than optimizing the engine before its architecture is established.

## Planned Technologies

The core engine will initially use standard Python.

Additional libraries may be introduced as the project develops, including:

- NumPy — numerical and vectorized computation
- Pygame — interactive rendering and input
- OpenGL or similar technologies — potentially for future high-performance rendering

Dependencies will be added only when they provide a meaningful benefit.

## Project Structure

```text
NDEngine/
├── engine/
│   ├── __init__.py
│   ├── geometry.py
│   └── transforms.py
│
├── tests/
│   └── test_transforms.py
│
├── docs/
│   └── ROADMAP.md
│
├── main.py
├── requirements.txt
├── CHANGELOG.md
├── LICENSE
└── README.md
```

## Origin

NDEngine evolved from an earlier Desmos project exploring:

- 3D rotations
- 4D rotations
- 4D → 3D projection
- 3D → 2D projection
- Perspective projection
- Higher-dimensional geometry

The Desmos prototype remains useful as a mathematical reference and testing ground.

## License

This project is licensed under the MIT License.