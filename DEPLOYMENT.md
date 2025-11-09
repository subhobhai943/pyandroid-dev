# PyAndroid Deployment Guide

This guide walks you through deploying PyAndroid to PyPI (Python Package Index).

## Prerequisites

1. **PyPI Account**: Register at [pypi.org](https://pypi.org/account/register/)
2. **TestPyPI Account**: Register at [test.pypi.org](https://test.pypi.org/account/register/)
3. **Python 3.7+**: Ensure you have Python installed
4. **Git**: Repository must be on GitHub

## Setup

### 1. Configure Trusted Publishing on PyPI

#### For TestPyPI (Testing):
1. Go to https://test.pypi.org/manage/account/publishing/
2. Click "Add a new publisher"
3. Fill in:
   - **PyPI Project Name**: `pyandroid`
   - **Owner**: `subhobhai943`
   - **Repository name**: `pyandroid-dev`
   - **Workflow name**: `publish-to-pypi.yml`
   - **Environment name**: `testpypi`
4. Click "Add"

#### For PyPI (Production):
1. Go to https://pypi.org/manage/account/publishing/
2. Click "Add a new publisher"
3. Fill in:
   - **PyPI Project Name**: `pyandroid`
   - **Owner**: `subhobhai943`
   - **Repository name**: `pyandroid-dev`
   - **Workflow name**: `publish-to-pypi.yml`
   - **Environment name**: `pypi`
4. Click "Add"

### 2. Configure GitHub Environments

#### Create TestPyPI Environment:
1. Go to repository Settings > Environments
2. Click "New environment"
3. Name: `testpypi`
4. Click "Configure environment"
5. No protection rules needed (for testing)

#### Create PyPI Environment:
1. Go to repository Settings > Environments
2. Click "New environment"
3. Name: `pypi`
4. Click "Configure environment"
5. Enable "Required reviewers" (add yourself)
6. This prevents accidental production releases

## Manual Deployment (For Testing)

### Build the Package

```bash
# Install build tools
pip install build twine

# Build distributions
python -m build

# This creates:
# dist/pyandroid-1.2.0.tar.gz (source)
# dist/pyandroid-1.2.0-py3-none-any.whl (wheel)
```

### Upload to TestPyPI

```bash
# Upload to TestPyPI
twine upload --repository testpypi dist/*

# You'll be prompted for username and password
# Or use API token: __token__ as username
```

### Test Installation from TestPyPI

```bash
# Create clean environment
python -m venv test_env
source test_env/bin/activate  # Windows: test_env\Scripts\activate

# Install from TestPyPI
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ pyandroid

# Test it
python -c "import pyandroid; print(pyandroid.__version__)"
```

### Upload to Production PyPI

```bash
# Upload to PyPI
twine upload dist/*

# Enter your PyPI credentials
```

## Automated Deployment (GitHub Actions)

The repository is configured for automated deployment:

### Trigger Automatic Deployment

```bash
# 1. Update version in pyproject.toml and pyandroid/__version__.py

# 2. Commit changes
git add .
git commit -m "Bump version to 1.2.0"

# 3. Create and push tag
git tag v1.2.0
git push origin main
git push origin v1.2.0

# GitHub Actions will automatically:
# - Build the package
# - Upload to TestPyPI
# - Wait for approval
# - Upload to PyPI
```

### Workflow Stages

1. **Build**: Triggered on every push
   - Runs tests
   - Builds distributions
   - Stores artifacts

2. **TestPyPI**: Triggered on every push
   - Downloads artifacts
   - Publishes to TestPyPI
   - No approval needed

3. **PyPI**: Triggered only on tags (v*)
   - Downloads artifacts  
   - Requires manual approval
   - Publishes to PyPI

## Version Management

### Semantic Versioning

Follow [SemVer](https://semver.org/): MAJOR.MINOR.PATCH

- **MAJOR**: Breaking changes
- **MINOR**: New features, backward compatible
- **PATCH**: Bug fixes

Examples:
- `1.0.0` → `1.0.1` (bug fix)
- `1.0.1` → `1.1.0` (new feature)
- `1.1.0` → `2.0.0` (breaking change)

### Update Version

Update in TWO places:

1. **pyproject.toml**:
```toml
[project]
name = "pyandroid"
version = "1.2.0"  # Update here
```

2. **pyandroid/__version__.py**:
```python
__version__ = "1.2.0"  # Update here
```

## Pre-Release Checklist

- [ ] All tests pass: `pytest tests/`
- [ ] Version updated in both files
- [ ] CHANGELOG.md updated
- [ ] README.md up to date
- [ ] Examples work correctly
- [ ] Documentation updated
- [ ] License file included
- [ ] No debug code or TODOs

## Release Process

### 1. Prepare Release

```bash
# Create release branch
git checkout -b release/v1.2.0

# Update version numbers
# Edit pyproject.toml
# Edit pyandroid/__version__.py

# Update changelog
# Edit CHANGELOG.md

# Commit changes
git add .
git commit -m "Prepare release v1.2.0"

# Push and create PR
git push origin release/v1.2.0
```

### 2. Merge and Tag

```bash
# After PR approval, merge to main
git checkout main
git pull origin main

# Create tag
git tag -a v1.2.0 -m "Release version 1.2.0"

# Push tag (triggers deployment)
git push origin v1.2.0
```

### 3. Monitor Deployment

1. Go to GitHub Actions tab
2. Watch the workflow run
3. Check TestPyPI: https://test.pypi.org/project/pyandroid/
4. Approve PyPI deployment (if on tag)
5. Verify on PyPI: https://pypi.org/project/pyandroid/

### 4. Create GitHub Release

1. Go to repository Releases
2. Click "Draft a new release"
3. Select tag: `v1.2.0`
4. Title: `PyAndroid v1.2.0`
5. Description: Copy from CHANGELOG.md
6. Attach built files from dist/
7. Click "Publish release"

## Troubleshooting

### Build Fails

```bash
# Check for syntax errors
python -m py_compile pyandroid/*.py

# Lint code
flake8 pyandroid/

# Run tests locally
pytest tests/
```

### Upload Fails

**Error: File already exists**
- You can't overwrite existing versions on PyPI
- Increment version number and try again

**Error: Invalid credentials**
- Check your PyPI username/token
- Regenerate API token if needed

**Error: Package name already taken**
- Choose a different name in pyproject.toml
- Current name: `pyandroid`

### Trusted Publishing Issues

1. Verify repository settings match exactly
2. Check environment names are correct
3. Ensure workflow file name matches
4. Verify you pushed the tag

## Post-Release

### Announce Release

1. **Twitter/X**: Share release announcement
2. **Reddit**: Post in r/Python
3. **Dev.to**: Write release article
4. **LinkedIn**: Professional announcement

### Update Documentation

```bash
# Update wiki with new features
# Update installation instructions
# Add migration guide if breaking changes
```

### Monitor

1. Watch PyPI download stats
2. Monitor GitHub issues
3. Check for bug reports
4. Respond to questions

## Hotfix Process

For urgent bug fixes:

```bash
# Create hotfix branch from tag
git checkout -b hotfix/v1.2.1 v1.2.0

# Fix bug
# Update version to 1.2.1
# Commit fix

# Merge to main
git checkout main
git merge hotfix/v1.2.1

# Tag and push
git tag v1.2.1
git push origin main v1.2.1
```

## Resources

- [PyPI Publishing Guide](https://packaging.python.org/)
- [Trusted Publishing](https://docs.pypi.org/trusted-publishers/)
- [Semantic Versioning](https://semver.org/)
- [GitHub Actions](https://docs.github.com/en/actions)

---

**Questions?** Open an issue on GitHub!
