# Changelog

## [1.2.0] - 2024-04-12

### Added

- Users can output preprocessing results to an attribute
- Added `drepr:blank` to automatically merge duplicated blank nodes
- Unpack relative URI of static properties if the datatype is `drepr:uri`

### Fixed

- Fixed errors for models that have missing values and optional property
- Fixed topological sort for execution planning
- Fixed processing non-optional object property
- Fixed bugs in `drepr.utils.attr_data` and `rdfgraph_writer` that write after abort records.
- Fixed bugs in auto align and alignment between single-value attributes (using IdenticalAlign).
- Fixed not processing static properties

## [1.1.3] - 2024-03-26

### Fixed

- Fixed `drepr:uri` does not generate the URI.

## [1.1.2] - 2024-03-22

### Added

- Added comparing TTL output when verifying the correctness of the generated program

### Changed

- Improved the performance of alignment inference by using a more efficient algorithm

## [1.1.1] - 2024-03-21

### Fixed

- Fixed concurrency issue when executing `python -m drepr` in parallel (writing to the same file in `/tmp/drepr`) directory

## [1.1.0] - 2024-03-21

### Added

- Added basic preprocessing (pmap)

### Fixed

- Fixed bugs and updated testcases and examples
- Fixed datatype relative uri wrapped with `<>` issue

### Changed

- Update codegen to version 2 to use new variable creation & scoping features.
