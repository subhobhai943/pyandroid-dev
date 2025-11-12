# Migration Guide: v1.3.0 → v1.4.0

This guide helps you migrate your pyandroid-dev code from version 1.3.0 to 1.4.0.

## Overview

Version 1.4.0 includes:
- ✅ Fixed test failures
- ✅ Better error handling with custom exceptions
- ✅ Activity lifecycle state validation
- ✅ Enhanced type hints
- ⚠️ Dropped Python 3.7 support

## Required Changes

### 1. Python Version Requirement

**Action Required**: Ensure you're using Python 3.8 or higher.

```bash
# Check your Python version
python --version
# Should output: Python 3.8.x or higher

# If you're on Python 3.7, upgrade:
# - Update your system Python
# - Update your virtual environment
# - Update CI/CD configurations
```

### 2. Activity Lifecycle Validation

**What Changed**: Activity state transitions are now validated.

**Before (v1.3.0)** - This could cause undefined behavior:
```python
activity = Activity("MyActivity")
activity.resume()  # Would work but was incorrect
```

**After (v1.4.0)** - This now raises an error:
```python
from pyandroid.core import Activity, InvalidStateError

activity = Activity("MyActivity")
try:
    activity.resume()  # Raises InvalidStateError
except InvalidStateError as e:
    print(f"Invalid transition: {e}")
```

**Correct Way**:
```python
activity = Activity("MyActivity")
activity.start()    # created -> started
activity.resume()   # started -> resumed
```

**Valid State Transitions**:
```
created → started
started → resumed or stopped
resumed → paused
paused  → resumed or stopped
stopped → started or destroyed
```

### 3. Exception Handling

**What Changed**: More specific exception types are now available.

**Before (v1.3.0)**:
```python
try:
    app.start_activity("unknown")
except ValueError as e:
    print(e)
```

**After (v1.4.0)** - More specific:
```python
from pyandroid.core import ActivityNotFoundError

try:
    app.start_activity("unknown")
except ActivityNotFoundError as e:
    print(f"Activity not found: {e}")
    # Error message now includes available activities
```

## Optional Enhancements

### 1. Use Activity Extras

**New Feature**: Pass data to activities during initialization.

```python
# v1.4.0: Pass data as kwargs
app.start_activity("details", user_id=123, mode="edit")

# In your Activity subclass:
class DetailsActivity(Activity):
    def on_start(self):
        user_id = self.extras.get("user_id")
        mode = self.extras.get("mode")
        print(f"Loading user {user_id} in {mode} mode")
```

### 2. Enhanced Intent Usage

**New Methods**: Check for extras and get all at once.

```python
from pyandroid.core import Intent

intent = Intent("ACTION_VIEW")
intent.put_extra("user_id", 123)
intent.put_extra("username", "alice")

# New in v1.4.0:
if intent.has_extra("user_id"):
    user_id = intent.get_extra("user_id")

# Get all extras as dict:
all_data = intent.get_all_extras()
print(all_data)  # {'user_id': 123, 'username': 'alice'}
```

### 3. View Management

**New Method**: Remove views from activities.

```python
from pyandroid.ui import TextView

activity = Activity("Main")
text_view = TextView("text1", "Hello")

activity.add_view("text1", text_view)

# New in v1.4.0:
if activity.remove_view("text1"):
    print("View removed successfully")
else:
    print("View not found")
```

## Testing Updates

If you have tests for your pyandroid-dev application:

### Update Test Requirements

**pyproject.toml** or **requirements-dev.txt**:
```toml
[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "pytest-cov>=4.0.0",
]
```

### Use Pytest Fixtures

**Before**:
```python
def test_something():
    app = AndroidApp("Test", "com.test", use_gui=False)
    # test code

def test_something_else():
    app = AndroidApp("Test", "com.test", use_gui=False)
    # test code
```

**After** (DRY - Don't Repeat Yourself):
```python
import pytest
from pyandroid.core import AndroidApp

@pytest.fixture
def test_app():
    return AndroidApp("Test", "com.test", use_gui=False)

def test_something(test_app):
    # test code using test_app

def test_something_else(test_app):
    # test code using test_app
```

## CI/CD Updates

### GitHub Actions

Update your workflow files:

**Before**:
```yaml
strategy:
  matrix:
    python-version: ["3.7", "3.8", "3.9", "3.10", "3.11"]
```

**After**:
```yaml
strategy:
  matrix:
    python-version: ["3.8", "3.9", "3.10", "3.11", "3.12"]
```

### Docker

Update Dockerfile base images:

**Before**:
```dockerfile
FROM python:3.7-slim
```

**After**:
```dockerfile
FROM python:3.8-slim
# or python:3.11-slim for latest stable
```

## Verification Checklist

After upgrading to v1.4.0, verify:

- [ ] Python version is 3.8 or higher
- [ ] All activity lifecycle calls follow valid transitions
- [ ] Exception handling uses specific exception types (optional but recommended)
- [ ] Tests pass with new version
- [ ] CI/CD pipelines updated
- [ ] Type hints work correctly in your IDE

## Troubleshooting

### Issue: Tests failing with InvalidStateError

**Cause**: Your code has invalid activity state transitions.

**Fix**: Review activity lifecycle calls and ensure proper order:
```python
# Correct order:
activity.start()
activity.resume()
activity.pause()
activity.stop()
activity.destroy()
```

### Issue: Import errors for custom exceptions

**Cause**: New exception classes not imported.

**Fix**: Update imports:
```python
from pyandroid.core import (
    AndroidApp,
    Activity,
    Intent,
    ActivityNotFoundError,  # New
    InvalidStateError,      # New
)
```

### Issue: Kivy import warnings

**Cause**: This is normal if you're running in console-only mode.

**Fix**: Either:
1. Install Kivy: `pip install pyandroid-dev[gui]`
2. Ignore warnings (they're informational only)
3. Suppress in tests with logging configuration

## Getting Help

If you encounter issues:

1. Check [IMPROVEMENTS.md](../IMPROVEMENTS.md) for detailed changes
2. Review the [test files](../tests/) for examples
3. [Open an issue](https://github.com/subhobhai943/pyandroid-dev/issues) on GitHub

## Summary

**Minimum Required Changes**:
1. ✅ Upgrade to Python 3.8+
2. ✅ Fix invalid activity state transitions (if any)

**Recommended Changes**:
1. Update exception handling to use specific types
2. Leverage new features (extras, remove_view, etc.)
3. Update tests to use fixtures

Most applications will work with minimal changes - primarily the Python version requirement.
