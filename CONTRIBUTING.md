# Contributing to PyAndroid

Thank you for your interest in contributing to PyAndroid! This document provides guidelines and instructions for contributing.

## Code of Conduct

Be respectful, constructive, and professional in all interactions.

## How to Contribute

### Reporting Bugs

1. Check if the bug has already been reported
2. Create a detailed issue with:
   - Clear title and description
   - Steps to reproduce
   - Expected vs actual behavior
   - Environment details (OS, Python version)
   - Code samples

### Suggesting Features

1. Check existing issues and discussions
2. Create an issue describing:
   - The problem it solves
   - Proposed implementation
   - Potential impact

### Pull Requests

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes
4. Add tests for new functionality
5. Run tests: `pytest tests/`
6. Format code: `black pyandroid/`
7. Commit: `git commit -m "Add amazing feature"`
8. Push: `git push origin feature/amazing-feature`
9. Open a Pull Request

## Development Setup

```bash
# Clone repository
git clone https://github.com/subhobhai943/pyandroid-dev.git
cd pyandroid-dev

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e ".[dev,gui]"

# Run tests
pytest tests/
```

## Coding Standards

- Follow PEP 8
- Use type hints where possible
- Write docstrings for all public APIs
- Add tests for new features
- Keep line length under 100 characters

## Testing

```bash
# Run all tests
pytest tests/

# Run with coverage
pytest --cov=pyandroid tests/

# Run specific test
pytest tests/test_core.py::TestActivity::test_activity_lifecycle
```

## License

By contributing, you agree that your contributions will be licensed under the PyAndroid Custom License v1.0.

## Questions?

Open an issue or start a discussion on GitHub!
