# Changelog

All notable changes to NDEngine will be documented in this file.

---

## [Unreleased]

### Added

- Initial project structure.
- Initial project documentation.
- Development roadmap.
- Git repository and GitHub remote.
- Generic N-dimensional plane rotation function.
- Initial transformation tests.
- Pytest-based test suite.
- Rotation operation representation with immutable `Rotation` objects.
- Ordered rotation composition through `apply_rotations()`.
- Validation for rotation coordinate indices.
- Mathematical property tests for rotations and ordered composition.
- Generic N-dimensional perspective projection function.
- Arbitrary-axis projection from N dimensions to N-1 dimensions.
- Immutable `Projection` objects for describing projection operations.
- Ordered projection composition through `apply_projections()`.
- Projection validation and explicit handling of projection singularities.
- Projection tests covering dimensional reduction, scaling, axis selection, composition, immutability, and near-singular cases.

### Planned

- Mathematical core for N-dimensional geometry.
- Generalized projection pipelines.
- Basic 3D rendering.
- 4D visualization.
- General N-dimensional geometry primitives.
- Interactive controls.
