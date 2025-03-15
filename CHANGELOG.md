# Changelog

## [1.6.3] - 2025-03-15

### Fixed

- Avoid using attribute IDs as variable names since IDs can be numeric

## [1.6.2] - 2024-12-22

### Fixed

- Update the Turtle writer to avoid writing multiline strings to ensure compatibility with Virtuoso
- Use `orjson.dumps` for proper string escaping, as `rdflib` does a poor job with N3 format

## [1.6.0] - 2024-10-20

### Added

- Allow passing Python objects directly as resources when calling DRepr programmatically

## [1.5.5] - 2024-08-08

### Fixed

- Fix bug in writing blank objects from classes with same URIs

## [1.5.4] - 2024-08-08

### Fixed

- Update validators and error messages

## [1.5.3] - 2024-07-19

### Fixed

- Fix turtle writer (buffered record)

## [1.5.2] - 2024-07-12

### Added

- Version 3 of the language. Mostly to support inplace creating of new attributes and classes.
- Add TurtleWriter and use it as the default writer for ttl format

### Fixed

- Support classes of only static properties

## [1.3.14] - 2024-06-18

### Changed

- Allow class id in Semantic Model to contain `_`

## [1.3.13] - 2024-06-15

### Fixed

- Fix auto alignments should only be applied to attributes that from or derived from the same resource

## [1.3.12] - 2024-05-28

### Fixed

- Preprocessing function support optional path
- Support `+=` expression and function defined inside UDF

## [1.3.11] - 2024-05-22

### Fixed

- Subject Inference: allow choosing a less restricted optional path [#4](https://github.com/binh-vu/drepr-v2/issues/4)

## [1.3.10] - 2024-05-22

### Fixed

- The version field now accepts a number

## [1.3.8] - 2024-05-14

### Changed

- `drepr.main` can be used to only generate the program.

## [1.3.7] - 2024-05-13

### Added

- CLI can be used to only generate the program.

## [1.3.6] - 2024-05-13

### Fixed

- Fix `typer` dependency issue

## [1.3.4] - 2024-05-13

### Added

- Add more supported ast types to `drepr.utils.udf`

## [1.3.3] - 2024-05-13

### Fixed

- fix serializing drepr model

## [1.3.2] - 2024-05-13

### Changed

- Clean up the data and fix annotations

## [1.3.1] - 2024-05-13

### Changed

- Support passing resource data in a string directly to `drepr.main.convert`

## [1.3.0] - 2024-05-13

### Added

- Add `drepr.main.convert` to convert data programmatically

## [1.2.4] - 2024-05-03

### Fixed

- Fix bug from RDFLib for integer but formatted as float zero decimal `.0`

## [1.2.3] - 2024-05-03

### Changed

- Attribute annotated with `drepr:uri` and `drepr:blank` should always be the subject of a class

## [1.2.2] - 2024-05-03

### Added

- Support bool and None as missing values

## [1.2.1] - 2024-04-12

### Fixed

- Fixed not parsing for-loop in user-defined functions in the preprocessing step

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
