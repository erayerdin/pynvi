# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased
### Changed
 - Moved package docstring to the top.
 - `dedent`ed some strings.
 - `verify_identity` raises `TypeError` instead of `ValueError` now

## [0.1.0pre4] - 2019-03-13
### Added
 - `NVIException`

### Changed
 - `verify_identity` now raises `NVIException` on server-based errors instead of
 a plain `Exception`

## [0.1.0pre3] - 2019-03-13
### Added
 - `3.7` tests on Travis

### Changed
 - Test stages (their names and versions) on Travis
 - Download URL to corresponding version in `setup.py`

## [0.1.0pre2] - 2019-03-13
### Added
 - `dev.requirements.txt` to `MANIFEST.in`

## [0.1.0pre1] - 2019-03-12
### Added
 - `verify_identity` method
