# Changelog

## Unreleased

### Fixed

- Fix errors for models that have missing values and optional property

## [1.1.3] - 2024-03-26

### Fixed

- Fix `drepr:uri` does not generate the URI.

## [1.1.2] - 2024-03-22

### Added

- Added comparing TTL output when verifying the correctness of the generated program

### Changed

- Improve the performance of alignment inference by using a more efficient algorithm

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
