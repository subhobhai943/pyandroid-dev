# PyAndroid-Dev Improvements and Fixes

This document outlines all the improvements and fixes applied to the pyandroid-dev library in version 1.4.0.

## Critical Bug Fixes

### 1. Test Workflow Fixed
**Problem**: Tests were failing because coverage XML file wasn't being generated.

**Solution**: 
- Updated `.github/workflows/tests.yml` to use `--cov-report=xml` flag
- Added `--cov-report=term` for console output during CI
- Limited codecov upload to one Python version (3.11) to avoid redundant uploads
- Removed Python 3.7 support (EOL)

### 2. Backend Import Error Handling
**Problem**: The backend module would crash when Kivy wasn't installed, even in console-only mode.

**Solution**:
- Updated `pyandroid/backend/__init__.py` to gracefully handle ImportError
- Set `KivyRenderer = None` when Kivy is unavailable
- Updated `AndroidApp` to properly check for None before using renderer

### 3. Activity Lifecycle State Validation
**Problem**: Activity state transitions weren't validated, allowing invalid transitions.

**Solution**:
- Added `VALID_TRANSITIONS` dictionary to Activity class
- Implemented `_validate_transition()` method
- All lifecycle methods now validate state transitions
- Raises `InvalidStateError` for invalid transitions

## New Features

### 1. Custom Exception Classes
Added three custom exception types for better error handling:

```python
from pyandroid.core import PyAndroidError, ActivityNotFoundError, InvalidStateError

# PyAndroidError - Base exception
# ActivityNotFoundError - Raised when activity not registered
# InvalidStateError - Raised on invalid state transitions
```

### 2. Enhanced Type Hints
- Added comprehensive type hints throughout `core.py`
- Added return type annotations to all methods
- Improved IDE autocomplete and static analysis support

### 3. Activity Extras Support
- Activities now accept `**kwargs` during initialization
- Extras stored in `activity.extras` dictionary
- Useful for passing data between activities

```python
activity = Activity("DetailActivity", user_id=123, username="alice")
print(activity.extras["user_id"])  # 123
```

### 4. Intent Enhancements
Added new Intent methods:
- `has_extra(key)` - Check if extra exists
- `get_all_extras()` - Get all extras as dictionary

### 5. Activity View Management
Added `remove_view()` method:

```python
activity.add_view("text1", text_view)
activity.remove_view("text1")  # Returns True if removed
```

## Code Quality Improvements

### 1. Comprehensive Documentation
- Added docstring examples to all major classes and methods
- Included usage examples in docstrings
- Better parameter descriptions

### 2. Test Suite Enhancements

**New Test Features**:
- Added pytest fixtures for common test objects
- Reduced code duplication across tests
- Added tests for exception handling
- Added tests for state validation
- Added tests for new features (extras, remove_view, etc.)
- Created `conftest.py` for shared test configuration

**Test Coverage Improvements**:
- Core tests increased from 3 to 9 test classes
- UI tests increased from 5 to 8 test classes
- Added edge case testing
- Added negative test cases

### 3. Better Error Messages
Improved error messages with context:

```python
# Before
ValueError: Activity not registered

# After
ActivityNotFoundError: Activity 'details' not registered. 
Available activities: ['main', 'settings']
```

### 4. Activity Switching
Improved activity switching logic:
- Properly stops and destroys previous activity
- Prevents resource leaks
- Maintains clean state transitions

## Configuration Updates

### 1. Python Version Support
- **Removed**: Python 3.7 (EOL since 2023-06-27)
- **Supported**: Python 3.8, 3.9, 3.10, 3.11, 3.12

### 2. PyProject.toml Improvements
- Updated to version 1.4.0
- Added "Typing :: Typed" classifier
- Improved description
- Added mypy configuration for `ignore_missing_imports`
- Added pytest strict markers

### 3. Test Configuration
- Added `conftest.py` for shared fixtures
- Configured logging to reduce test output noise
- Added verbose mode and strict markers to pytest

## Breaking Changes

### Python 3.7 No Longer Supported
If you're using Python 3.7, please upgrade to Python 3.8 or later.

### Activity State Validation
Code that relied on invalid state transitions will now raise `InvalidStateError`:

```python
# This will now raise InvalidStateError
activity = Activity("Test")
activity.resume()  # Can't resume without starting first

# Correct way
activity = Activity("Test")
activity.start()
activity.resume()  # Now works
```

## Migration Guide

### From Version 1.3.0 to 1.4.0

1. **Update Python Version** (if needed):
   ```bash
   # Check your Python version
   python --version
   
   # Should be 3.8 or higher
   ```

2. **Update Activity Lifecycle Calls**:
   ```python
   # Old code (may fail in 1.4.0)
   activity.resume()  # No start() call
   
   # New code (correct)
   activity.start()
   activity.resume()
   ```

3. **Use New Exception Types**:
   ```python
   # Old code
   try:
       app.start_activity("unknown")
   except ValueError as e:
       print(e)
   
   # New code (more specific)
   from pyandroid.core import ActivityNotFoundError
   
   try:
       app.start_activity("unknown")
   except ActivityNotFoundError as e:
       print(f"Activity not found: {e}")
   ```

4. **Leverage New Features**:
   ```python
   # Use activity extras
   app.start_activity("details", user_id=123, mode="edit")
   
   # Use Intent extras checking
   if intent.has_extra("user_id"):
       user_id = intent.get_extra("user_id")
   ```

## Testing

To run tests with the improvements:

```bash
# Install dev dependencies
pip install -e ".[dev]"

# Run tests with coverage
pytest --cov=pyandroid --cov-report=xml --cov-report=term tests/

# Run specific test file
pytest tests/test_core.py -v

# Run specific test
pytest tests/test_core.py::TestActivity::test_invalid_state_transition -v
```

## Performance

No significant performance changes. All improvements focus on:
- Reliability (better error handling)
- Developer experience (type hints, better errors)
- Code quality (comprehensive tests)

## Future Enhancements

Potential improvements for future versions:

1. **Async Support**: Add async/await support for I/O operations
2. **Fragment Support**: Implement Android-like fragments
3. **Navigation Component**: Add navigation graph support
4. **Data Binding**: Two-way data binding for UI components
5. **Dependency Injection**: Simple DI container for testing
6. **More Layouts**: Add ConstraintLayout, FrameLayout, GridLayout
7. **Animation Support**: Add view animation framework
8. **Resource Management**: Better resource loading and management

## Contributors

Thanks to all contributors who helped identify issues and suggest improvements.

## License

PyAndroid Custom License v1.0 - See LICENSE file for details.
