# Changelog

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
