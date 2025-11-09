# Changelog

All notable changes to PyAndroid will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned
- WebView component
- SQLite database integration
- Enhanced animations
- More layout types
- Plugin system

## [1.2.0] - 2025-11-09

### Added
- Comprehensive test suite with pytest
- GitHub Actions CI/CD workflows for automated testing and deployment
- Custom PyAndroid License v1.0
- Modern `pyproject.toml` configuration
- Version management with `__version__.py`
- MANIFEST.in for proper package distribution
- CONTRIBUTING.md with contribution guidelines
- DEPLOYMENT.md with deployment instructions
- Enhanced README with badges, examples, and comprehensive documentation
- FAQ section in README
- Roadmap for future versions

### Changed
- Migrated from setup.py to pyproject.toml
- Updated package name from `pyandroid-dev` to `pyandroid` for PyPI
- Improved documentation with emojis and better formatting
- Enhanced error messages and logging
- Better code organization

### Fixed
- Various bug fixes in UI rendering
- Improved error handling in backend
- Fixed import issues

## [1.1.0] - 2025-11-09

### Added
- Kivy backend for actual GUI rendering
- Real graphical interface support
- KivyRenderer class for translating PyAndroid components to Kivy widgets
- Cross-platform desktop support (Windows, Mac, Linux)
- Automatic color conversion (hex to RGBA)
- GUI enable/disable option in AndroidApp
- Backend module structure

### Changed
- AndroidApp now accepts `use_gui` parameter
- Updated core.py to integrate with rendering backend
- Enhanced Activity class for GUI support
- Updated requirements to include Kivy

### Fixed
- Console mode fallback when Kivy is not available
- Import errors when Kivy is missing

## [1.0.0] - 2024-10-24

### Added
- Initial release
- Core Android components:
  - AndroidApp: Main application class
  - Activity: Screen management with lifecycle methods
  - Intent: Inter-component communication
- Complete UI framework:
  - View: Base class for all UI components
  - TextView: Text display
  - Button: Interactive buttons
  - EditText: Text input fields
  - LinearLayout: Linear arrangement of children
  - RelativeLayout: Relative positioning
  - Widget: Helper class for creating widgets
- Utility classes:
  - Logger: Application logging
  - FileManager: File operations
  - NetworkManager: HTTP requests
- Comprehensive documentation
- Example applications
- MIT License

### Core Features
- Pythonic API design
- Event handling system
- View styling (colors, sizes, fonts)
- Layout system
- Click listeners
- Activity lifecycle management
- State persistence

## [0.1.0] - 2024-10-01 (Pre-release)

### Added
- Initial project structure
- Basic proof of concept
- Core class definitions

---

## Version History Summary

- **v1.2.0**: Production-ready with tests, CI/CD, and custom license
- **v1.1.0**: Added real GUI support with Kivy
- **v1.0.0**: Initial stable release with core features
- **v0.1.0**: Early development version

## Upgrade Guide

### From 1.1.x to 1.2.x

No breaking changes. Simply upgrade:

```bash
pip install --upgrade pyandroid
```

Note: Package name changed from `pyandroid-dev` to `pyandroid` on PyPI.

### From 1.0.x to 1.1.x

Minor API additions. No breaking changes. Update your installation:

```bash
# Old installation
pip uninstall pyandroid-dev

# New installation with GUI
pip install "pyandroid[gui]"
```

If you don't need GUI, the library still works in console mode.

## License Changes

As of v1.2.0, PyAndroid uses a custom license. See [LICENSE](LICENSE) for details.

Previous versions (1.0.x, 1.1.x) were under MIT License.

## Contributors

Thank you to all contributors who helped make PyAndroid better!

- [@subhobhai943](https://github.com/subhobhai943) - Creator and maintainer

[Unreleased]: https://github.com/subhobhai943/pyandroid-dev/compare/v1.2.0...HEAD
[1.2.0]: https://github.com/subhobhai943/pyandroid-dev/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/subhobhai943/pyandroid-dev/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/subhobhai943/pyandroid-dev/releases/tag/v1.0.0
[0.1.0]: https://github.com/subhobhai943/pyandroid-dev/releases/tag/v0.1.0
