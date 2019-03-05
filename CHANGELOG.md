-# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic
Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added
- `install_requires` key-value in `setup.py` to let pip know to install requests
  as this API wrapper depends on it!

### Changed


## [1.0.2]
### Changed
- Added an `__init__.py` to make `rescue_api/` an actual Python package. This
  resolves all import issues.


## [1.0.1]
### Changed
- Modified `setup.py` in an effort to make imports work.

## [1.0.0]
### Added
- Fully implemented RescueTime API (to the extent of their documentation!)
- Added package to PyPi - <https://pypi.org/project/rescue-api/>

## [0.9.0] - 2019-01-25
### Added
- Implemented support for the rest of the RescueTime API
  - Daily Summary API!
  - Alerts Feed API!
  - Highlights Feed API!
  - Highlights Post API!

[Unreleased]: https://git.sr.ht/~mjorgensen/rescue-api/
[1.0.2]: https://git.sr.ht/~mjorgensen/rescue-api/refs/1.0.2
[1.0.1]: https://git.sr.ht/~mjorgensen/rescue-api/refs/1.0.1
[1.0.0]: https://git.sr.ht/~mjorgensen/rescue-api/refs/1.0.0
[0.9.0]: https://git.sr.ht/~mjorgensen/rescue-api/refs/0.9.0