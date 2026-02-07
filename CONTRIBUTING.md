# Wkład w System Wykrywania Stresu / Contributing to Stress Detection System

Dziękujemy za zainteresowanie wkładem w projekt Systemu Wykrywania Stresu w Czasie Rzeczywistym! Witamy wkład od społeczności i jesteśmy wdzięczni za Wasze wsparcie.

Thank you for your interest in contributing to the Real-Time Stress Detection System! We welcome contributions from the community and are grateful for your support.

**Dla początkujących / For Beginners:**
Jeśli to Twój pierwszy raz z projektem open-source, nie martw się! Ten dokument poprowadzi Cię krok po kroku.
If this is your first time with an open-source project, don't worry! This document will guide you step by step.

## Spis treści / Table of Contents

1. [Kodeks postępowania / Code of Conduct](#code-of-conduct)
2. [Pierwsze kroki / Getting Started](#getting-started)
3. [Przepływ pracy deweloperskiej / Development Workflow](#development-workflow)
4. [Standardy kodowania / Coding Standards](#coding-standards)
5. [Wytyczne testowania / Testing Guidelines](#testing-guidelines)
6. [Wytyczne prywatności i bezpieczeństwa / Privacy & Security Guidelines](#privacy--security-guidelines)
7. [Proces Pull Request / Pull Request Process](#pull-request-process)
8. [Wytyczne dla zgłoszeń / Issue Guidelines](#issue-guidelines)
9. [Społeczność / Community](#community)

---

## Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inclusive environment for all contributors, regardless of:
- Age, body size, disability, ethnicity, gender identity and expression
- Level of experience, education, socio-economic status
- Nationality, personal appearance, race, religion
- Sexual identity and orientation

### Our Standards

**Positive behavior includes:**
- Using welcoming and inclusive language
- Being respectful of differing viewpoints and experiences
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members

**Unacceptable behavior includes:**
- Harassment, trolling, or derogatory comments
- Publishing others' private information without permission
- Any conduct that could reasonably be considered inappropriate

### Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be reported to the project maintainers at conduct@nuvai.io. All complaints will be reviewed and investigated promptly and fairly.

---

## Getting Started

### Prerequisites

Before contributing, ensure you have:

- **Python 3.10+** installed
- **Node.js 18+** and npm
- **Git** for version control
- **A GitHub account**
- **Webcam and microphone** (for testing facial/voice modules)

### Fork and Clone

1. **Fork** the repository on GitHub
2. **Clone** your fork locally:

```bash
git clone https://github.com/YOUR-USERNAME/stress-detection-system.git
cd stress-detection-system
```

3. **Add upstream remote**:

```bash
git remote add upstream https://github.com/Nuvai/stress-detection-system.git
```

### Set Up Development Environment

```bash
# Create Python virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install Python dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt  # Development dependencies

# Install pre-commit hooks
pre-commit install

# Set up frontend
cd src/frontend
npm install
cd ../..

# Download ML models (if available)
python scripts/download_models.py
```

### Verify Setup

```bash
# Run tests
pytest

# Run linters
flake8 src/backend
pylint src/backend

# Frontend checks
cd src/frontend
npm run lint
npm run type-check
```

---

## Development Workflow

### Branching Strategy

We use **Git Flow** with the following branches:

- **`main`** - Production-ready code (protected)
- **`develop`** - Integration branch for features (protected)
- **`feature/*`** - New features (e.g., `feature/voice-analysis`)
- **`bugfix/*`** - Bug fixes (e.g., `bugfix/memory-leak`)
- **`hotfix/*`** - Urgent production fixes
- **`release/*`** - Release preparation

### Creating a Feature Branch

```bash
# Ensure you're on develop and up-to-date
git checkout develop
git pull upstream develop

# Create feature branch
git checkout -b feature/your-feature-name

# Work on your feature...
git add .
git commit -m "feat: add voice pitch analysis"

# Push to your fork
git push origin feature/your-feature-name
```

### Commit Message Convention

We follow **[Conventional Commits](https://www.conventionalcommits.org/)**:

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code formatting (no logic change)
- `refactor`: Code restructuring (no feature/fix)
- `test`: Adding or updating tests
- `chore`: Maintenance tasks (dependencies, config)
- `perf`: Performance improvements

**Examples:**

```bash
feat(behavioral): add typing error rate tracking
fix(facial): resolve MediaPipe initialization crash
docs(readme): update installation instructions
test(fusion): add unit tests for signal normalization
```

---

## Coding Standards

### Python (Backend)

#### Style Guide
- Follow **PEP 8**
- Use **type hints** for all functions
- Maximum line length: **100 characters**
- Use **4 spaces** for indentation (no tabs)

#### Example

```python
from typing import List, Dict, Optional

def calculate_stress_score(
    behavioral_score: float,
    facial_score: Optional[float] = None,
    voice_score: Optional[float] = None
) -> Dict[str, float]:
    """
    Calculate final stress score from multi-modal inputs.

    Args:
        behavioral_score: Behavioral module score (0-100)
        facial_score: Facial module score (0-100), optional
        voice_score: Voice module score (0-100), optional

    Returns:
        Dictionary with final score and confidence
    """
    scores: List[float] = [behavioral_score]
    weights: List[float] = [0.5]

    if facial_score is not None:
        scores.append(facial_score)
        weights.append(0.3)

    if voice_score is not None:
        scores.append(voice_score)
        weights.append(0.2)

    # Normalize weights
    total_weight = sum(weights)
    normalized_weights = [w / total_weight for w in weights]

    final_score = sum(s * w for s, w in zip(scores, normalized_weights))

    return {
        "final_score": final_score,
        "confidence": calculate_confidence(scores)
    }
```

#### Tools
- **Formatter**: `black src/backend`
- **Linter**: `flake8 src/backend`
- **Type Checker**: `mypy src/backend`
- **Import Sorter**: `isort src/backend`

### TypeScript/React (Frontend)

#### Style Guide
- Follow **Airbnb JavaScript Style Guide**
- Use **TypeScript** (strict mode)
- Use **functional components** with hooks
- Maximum line length: **100 characters**
- Use **2 spaces** for indentation

#### Example

```typescript
import React, { useState, useEffect } from 'react';

interface StressGaugeProps {
  score: number;
  level: 'low' | 'medium' | 'high' | 'critical';
}

export const StressGauge: React.FC<StressGaugeProps> = ({ score, level }) => {
  const [displayScore, setDisplayScore] = useState<number>(0);

  useEffect(() => {
    // Animate score transition
    const timer = setTimeout(() => setDisplayScore(score), 100);
    return () => clearTimeout(timer);
  }, [score]);

  const getColor = (): string => {
    switch (level) {
      case 'low': return 'green';
      case 'medium': return 'yellow';
      case 'high': return 'orange';
      case 'critical': return 'red';
      default: return 'gray';
    }
  };

  return (
    <div className="stress-gauge">
      <div className="score" style={{ color: getColor() }}>
        {displayScore}
      </div>
      <div className="level">{level.toUpperCase()}</div>
    </div>
  );
};
```

#### Tools
- **Formatter**: `npm run format` (Prettier)
- **Linter**: `npm run lint` (ESLint)
- **Type Checker**: `npm run type-check` (TypeScript)

---

## Testing Guidelines

### Test Coverage Requirements

- **Minimum coverage**: 80% for all modules
- **Critical modules**: 95%+ (fusion, security, privacy)
- **Every PR must maintain or improve coverage**

### Writing Tests

#### Unit Tests (Python)

```python
# tests/unit/test_fusion.py
import pytest
from src.backend.modules.fusion import calculate_stress_score

def test_behavioral_only_score():
    result = calculate_stress_score(behavioral_score=70.0)
    assert result["final_score"] == 70.0
    assert result["confidence"] >= 0.5

def test_multimodal_score():
    result = calculate_stress_score(
        behavioral_score=70.0,
        facial_score=60.0,
        voice_score=80.0
    )
    expected = 0.5 * 70 + 0.3 * 60 + 0.2 * 80
    assert result["final_score"] == pytest.approx(expected, rel=0.01)
```

#### Integration Tests

```python
# tests/integration/test_end_to_end.py
def test_stress_detection_pipeline():
    # Simulate behavioral data
    behavioral_data = {"typing_speed": 65, "error_rate": 0.15}

    # Run through pipeline
    behavioral_score = behavioral_module.process(behavioral_data)
    final_score = fusion_engine.calculate(behavioral_score)

    assert 0 <= final_score <= 100
    assert final_score > 50  # High error rate should elevate stress
```

### Running Tests

```bash
# All tests
pytest

# Specific module
pytest tests/unit/test_fusion.py

# With coverage
pytest --cov=src/backend --cov-report=html

# Frontend tests
cd src/frontend
npm test
npm run test:coverage
```

---

## Privacy & Security Guidelines

### Critical Rules

#### 1. No Data Transmission
```python
# ❌ NEVER DO THIS
import requests
requests.post("https://analytics.com", data=user_data)

# ✅ CORRECT
# All processing happens locally, no network calls
```

#### 2. No Content Logging
```python
# ❌ NEVER DO THIS
logger.info(f"User typed: {keystroke_content}")

# ✅ CORRECT
logger.info(f"Typing speed: {typing_speed} WPM")
```

#### 3. Encryption Required
```python
# ❌ NEVER DO THIS
with open("user_profile.json", "w") as f:
    json.dump(profile_data, f)

# ✅ CORRECT
encrypted_data = encrypt_aes256(json.dumps(profile_data))
with open("user_profile.enc", "wb") as f:
    f.write(encrypted_data)
```

#### 4. Sanitize Error Messages
```python
# ❌ NEVER DO THIS
except Exception as e:
    logger.error(f"Failed to process: {user_data}")

# ✅ CORRECT
except Exception as e:
    logger.error(f"Failed to process data, error type: {type(e).__name__}")
```

### Security Checklist

Before submitting a PR involving user data:

- [ ] No user content (keystrokes, screenshots, audio) is stored
- [ ] All sensitive data is encrypted at rest
- [ ] No network requests to external servers
- [ ] Error messages don't leak user information
- [ ] User can delete all data
- [ ] Permissions are requested explicitly
- [ ] Code has been reviewed for SQL injection, XSS, command injection

---

## Pull Request Process

### Before Submitting

1. **Update from upstream**:
```bash
git fetch upstream
git rebase upstream/develop
```

2. **Run all checks**:
```bash
# Backend
pytest
flake8 src/backend
mypy src/backend

# Frontend
cd src/frontend
npm test
npm run lint
npm run type-check
```

3. **Update documentation** if needed

4. **Add tests** for new features

### PR Template

When creating a PR, use this template:

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix (non-breaking change fixing an issue)
- [ ] New feature (non-breaking change adding functionality)
- [ ] Breaking change (fix or feature causing existing functionality to change)
- [ ] Documentation update

## Related Issues
Closes #123

## Testing
- [ ] Unit tests added/updated
- [ ] Integration tests added/updated
- [ ] Manual testing completed

## Privacy/Security Impact
- [ ] No user data is transmitted
- [ ] No sensitive data is logged
- [ ] Encryption is used where needed
- [ ] No new permissions required
- [ ] NA - No privacy/security impact

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex logic
- [ ] Documentation updated
- [ ] Tests pass locally
- [ ] No new warnings generated

## Screenshots (if applicable)
```

### Review Process

1. **Automated checks** must pass (CI/CD)
2. **At least 1 maintainer approval** required
3. **All review comments addressed**
4. **No merge conflicts**
5. **Squash commits** before merge (if requested)

### After Merge

- Delete your feature branch
- Pull latest develop:
```bash
git checkout develop
git pull upstream develop
```

---

## Issue Guidelines

### Reporting Bugs

**Before creating an issue:**
1. Search existing issues to avoid duplicates
2. Update to the latest version
3. Verify it's reproducible

**Bug Report Template:**

```markdown
**Description**
Clear description of the bug

**Steps to Reproduce**
1. Go to '...'
2. Click on '...'
3. See error

**Expected Behavior**
What should happen

**Actual Behavior**
What actually happens

**Screenshots**
If applicable

**Environment**
- OS: [e.g., Windows 11, macOS 14.2, Ubuntu 22.04]
- Python version: [e.g., 3.10.5]
- App version: [e.g., 0.1.0-alpha]

**Additional Context**
Any other relevant information
```

### Requesting Features

**Feature Request Template:**

```markdown
**Problem Statement**
What problem does this solve?

**Proposed Solution**
How would you like it to work?

**Alternatives Considered**
Other approaches you've thought about

**Privacy Considerations**
Any privacy implications?

**Additional Context**
Mockups, examples, etc.
```

### Issue Labels

- `bug` - Something isn't working
- `enhancement` - New feature or request
- `documentation` - Docs improvements
- `good first issue` - Good for newcomers
- `help wanted` - Extra attention needed
- `privacy` - Privacy-related issue
- `security` - Security-related issue
- `performance` - Performance optimization
- `ui/ux` - User interface/experience

---

## Community

### Communication Channels

- **GitHub Discussions**: For questions and ideas
- **GitHub Issues**: For bugs and feature requests
- **Discord** (coming soon): Real-time chat
- **Email**: dev-team@nuvai.io (for security issues)

### Getting Help

- Check the [README](README.md) and [PRD](docs/PRD_Stress_Detection_System.md) first
- Search existing GitHub issues
- Ask in GitHub Discussions
- Join our Discord community (coming soon)

### Recognition

We value all contributions! Contributors will be:
- Listed in our README
- Mentioned in release notes
- Invited to our private contributor Discord

### First-Time Contributors

Look for issues labeled `good first issue`. These are:
- Well-documented
- Limited in scope
- Good introduction to the codebase

**We're here to help!** Don't hesitate to ask questions in the issue comments.

---

## Development Tips

### Debugging

```bash
# Backend debugging
python -m pdb src/backend/main.py

# Enable verbose logging
export LOG_LEVEL=DEBUG
python src/backend/main.py

# Frontend debugging (React DevTools)
cd src/frontend
npm run dev  # Opens with React DevTools enabled
```

### Performance Profiling

```bash
# Python profiling
python -m cProfile -o profile.prof src/backend/main.py
python -m pstats profile.prof

# Memory profiling
python -m memory_profiler src/backend/main.py
```

### Documentation

When adding new features, update:
- Docstrings (Python functions)
- JSDoc comments (TypeScript functions)
- README.md (if user-facing)
- API documentation (if applicable)

---

## License

By contributing, you agree that your contributions will be licensed under the MIT License with additional privacy and ethical use terms (see [LICENSE](LICENSE)).

---

## Questions?

If you have questions about contributing, please:
1. Check this document thoroughly
2. Search GitHub Discussions
3. Open a new Discussion (not an Issue)
4. Email dev-team@nuvai.io for sensitive topics

---

**Thank you for contributing to a more stress-aware future!** 🙏

Your efforts help millions of workers detect stress early and maintain better work-life balance.

*Built with ❤️ by the Nuvai community*
