---
name: mutation_testing_python
description: Mutation testing patterns for Python using mutmut. Use when analyzing Python code to find weak or missing tests, verifying pytest effectiveness, strengthening Python test suites, or validating TDD workflows in Python projects.
---

# Mutation Testing for Python

Mutation testing answers the question: **"Are my tests actually catching bugs?"**

Code coverage tells you what code your tests execute. Mutation testing tells you if your tests would **detect changes** to that code. A test suite with 100% coverage can still miss 40% of potential bugs.

---

## Core Concept

**The Mutation Testing Process:**

1. **Generate mutants**: Introduce small bugs (mutations) into production code
2. **Run tests**: Execute your test suite against each mutant
3. **Evaluate results**: If tests fail, the mutant is "killed" (good). If tests pass, the mutant "survived" (bad - your tests missed the bug)

**The Insight**: A surviving mutant represents a bug your tests wouldn't catch.

---

## When to Use This Skill

Use mutation testing analysis when:

- Reviewing code changes on a branch
- Verifying test effectiveness after TDD
- Identifying weak tests that appear to have coverage
- Finding missing edge case tests
- Validating that refactoring didn't weaken test suite

**Integration with TDD:**

```
TDD Workflow                    Mutation Testing Validation
┌─────────────────┐             ┌─────────────────────────────┐
│ RED: Write test │             │                             │
│ GREEN: Pass it  │──────────►  │ After GREEN: Verify tests   │
│ REFACTOR        │             │ would kill relevant mutants │
└─────────────────┘             └─────────────────────────────┘
```

---

## Systematic Branch Analysis Process

When analyzing code on a branch, follow this systematic process:

### Step 1: Identify Changed Code

```bash
# Get files changed on the branch
git diff main...HEAD --name-only | grep '\.py$' | grep -v 'test_'

# Get detailed diff for analysis
git diff main...HEAD -- src/
```

### Step 2: Generate Mental Mutants

For each changed function/method, mentally apply mutation operators (see Mutation Operators section below).

### Step 3: Verify Test Coverage

For each potential mutant, ask:

1. **Is there a test that exercises this code path?**
2. **Would that test FAIL if this mutation were applied?**
3. **Is the assertion specific enough to catch this change?**

### Step 4: Document Findings

Categorize findings:

| Category | Description | Action Required |
|----------|-------------|-----------------|
| Killed | Test would fail if mutant applied | None - tests are effective |
| Survived | Test would pass with mutant | Add/strengthen test |
| No Coverage | No test exercises this code | Add behavior test |
| Equivalent | Mutant produces same behavior | None - not a real bug |

---

## Mutation Operators

### Arithmetic Operator Mutations

| Original | Mutated | Test Should Verify |
|----------|---------|-------------------|
| `a + b` | `a - b` | Addition behavior |
| `a - b` | `a + b` | Subtraction behavior |
| `a * b` | `a / b` | Multiplication behavior |
| `a / b` | `a * b` | Division behavior |
| `a // b` | `a / b` | Integer division behavior |
| `a % b` | `a * b` | Modulo behavior |
| `a ** b` | `a * b` | Exponentiation behavior |

**Example Analysis:**

```python
# Production code
def calculate_total(price: float, quantity: int) -> float:
    return price * quantity

# Mutant: price / quantity
# Question: Would tests fail if * became /?

# ❌ WEAK TEST - Would NOT catch mutant
def test_calculates_total():
    assert calculate_total(10.0, 1) == 10.0  # 10 * 1 = 10, 10 / 1 = 10 (SAME!)

# ✅ STRONG TEST - Would catch mutant
def test_calculates_total():
    assert calculate_total(10.0, 3) == 30.0  # 10 * 3 = 30, 10 / 3 = 3.33 (DIFFERENT!)
```

### Conditional Expression Mutations

| Original | Mutated | Test Should Verify |
|----------|---------|-------------------|
| `a < b` | `a <= b` | Boundary value at equality |
| `a < b` | `a >= b` | Both sides of condition |
| `a <= b` | `a < b` | Boundary value at equality |
| `a <= b` | `a > b` | Both sides of condition |
| `a > b` | `a >= b` | Boundary value at equality |
| `a > b` | `a <= b` | Both sides of condition |
| `a >= b` | `a > b` | Boundary value at equality |
| `a >= b` | `a < b` | Both sides of condition |

**Example Analysis:**

```python
# Production code
def is_adult(age: int) -> bool:
    return age >= 18

# Mutant: age > 18
# Question: Would tests fail if >= became >?

# ❌ WEAK TEST - Would NOT catch boundary mutant
def test_returns_true_for_adults():
    assert is_adult(25) is True  # 25 >= 18 = True, 25 > 18 = True (SAME!)

# ✅ STRONG TEST - Would catch boundary mutant
def test_returns_true_for_exactly_18():
    assert is_adult(18) is True  # 18 >= 18 = True, 18 > 18 = False (DIFFERENT!)
```

### Equality Operator Mutations

| Original | Mutated | Test Should Verify |
|----------|---------|-------------------|
| `a == b` | `a != b` | Both equal and not equal cases |
| `a != b` | `a == b` | Both equal and not equal cases |
| `a is b` | `a is not b` | Identity check (especially for None) |
| `a is not b` | `a is b` | Identity check |
| `a in b` | `a not in b` | Membership testing |
| `a not in b` | `a in b` | Membership testing |

### Logical Operator Mutations

| Original | Mutated | Test Should Verify |
|----------|---------|-------------------|
| `a and b` | `a or b` | Case where one is true, other is false |
| `a or b` | `a and b` | Case where one is true, other is false |
| `not a` | `a` | Negation is necessary |

**Example Analysis:**

```python
# Production code
def can_access(is_admin: bool, is_owner: bool) -> bool:
    return is_admin or is_owner

# Mutant: is_admin and is_owner
# Question: Would tests fail if or became and?

# ❌ WEAK TEST - Would NOT catch mutant
def test_returns_true_when_both_conditions_met():
    assert can_access(True, True) is True  # True or True = True and True (SAME!)

# ✅ STRONG TEST - Would catch mutant
def test_returns_true_when_only_admin():
    assert can_access(True, False) is True  # True or False = True, True and False = False (DIFFERENT!)
```

### Boolean Literal Mutations

| Original | Mutated | Test Should Verify |
|----------|---------|-------------------|
| `True` | `False` | Both true and false outcomes |
| `False` | `True` | Both true and false outcomes |
| `not a` | `a` | Negation is necessary |

### Block Statement Mutations

| Original | Mutated | Test Should Verify |
|----------|---------|-------------------|
| Function body | Empty function | Side effects of the function |

**Example Analysis:**

```python
# Production code
def process_order(order: Order) -> None:
    validate_order(order)
    save_order(order)
    send_confirmation(order)

# Mutant: Empty function body
# Question: Would tests fail if all statements removed?

# ❌ WEAK TEST - Would NOT catch mutant
def test_processes_order_without_error():
    process_order(order)  # Empty function also doesn't raise!

# ✅ STRONG TEST - Would catch mutant
def test_saves_order_to_database(mock_database):
    process_order(order)
    mock_database.save.assert_called_once_with(order)
```

### String Literal Mutations

| Original | Mutated | Test Should Verify |
|----------|---------|-------------------|
| `"text"` | `""` | Non-empty string behavior |
| `""` | `"mutmut was here"` | Empty string behavior |
| `"text"` | `"XX"` | Specific string value matters |

### List/Dict/Set Mutations

| Original | Mutated | Test Should Verify |
|----------|---------|-------------------|
| `[1, 2, 3]` | `[]` | Non-empty list behavior |
| `{}` (dict) | `{None: None}` | Empty dict behavior |
| `{1, 2, 3}` | `set()` | Non-empty set behavior |

**Example Analysis:**

```python
# Production code
def get_default_tags() -> list[str]:
    return ["python", "testing"]

# Mutant: return []
# Question: Would tests fail if list was empty?

# ❌ WEAK TEST - Would NOT catch mutant
def test_returns_list():
    result = get_default_tags()
    assert isinstance(result, list)  # Empty list is still a list!

# ✅ STRONG TEST - Would catch mutant
def test_returns_default_tags():
    assert get_default_tags() == ["python", "testing"]
```

### Assignment Operator Mutations

| Original | Mutated | Test Should Verify |
|----------|---------|-------------------|
| `a += b` | `a -= b` | Addition assignment |
| `a -= b` | `a += b` | Subtraction assignment |
| `a *= b` | `a /= b` | Multiplication assignment |
| `a /= b` | `a *= b` | Division assignment |

### Control Flow Mutations

| Original | Mutated | Test Should Verify |
|----------|---------|-------------------|
| `break` | `continue` | Loop termination behavior |
| `continue` | `break` | Loop iteration behavior |

### Python-Specific Method Mutations

| Original | Mutated | Test Should Verify |
|----------|---------|-------------------|
| `.startswith()` | `.endswith()` | Correct string position |
| `.endswith()` | `.startswith()` | Correct string position |
| `.upper()` | `.lower()` | Case transformation |
| `.lower()` | `.upper()` | Case transformation |
| `.strip()` | `.lstrip()` | Correct trim behavior |
| `.strip()` | `.rstrip()` | Correct trim behavior |
| `.append()` | (removed) | List modification matters |
| `.extend()` | `.append()` | Correct list operation |
| `any()` | `all()` | Partial vs full match |
| `all()` | `any()` | Full vs partial match |
| `min()` | `max()` | Correct extremum |
| `max()` | `min()` | Correct extremum |
| `.get()` | `[]` (indexing) | Dictionary key handling |

---

## Mutant States and Metrics

### Mutant States

| State | Meaning | Action |
|-------|---------|--------|
| **Killed** | Test failed when mutant applied | Good - tests are effective |
| **Survived** | Tests passed with mutant active | Bad - add/strengthen test |
| **No Coverage** | No test exercises this code | Add behavior test |
| **Timeout** | Tests timed out (infinite loop) | Counted as detected |
| **Equivalent** | Mutant produces same behavior | No action - not a real bug |

### Metrics

- **Mutation Score**: `killed / valid * 100` - The higher, the better
- **Detected**: `killed + timeout`
- **Undetected**: `survived + no coverage`

### Target Mutation Score

| Score | Quality |
|-------|---------|
| < 60% | Weak test suite - significant gaps |
| 60-80% | Moderate - many improvements possible |
| 80-90% | Good - but still gaps to address |
| > 90% | Strong - but watch for equivalent mutants |

---

## Equivalent Mutants

Equivalent mutants produce the same behavior as the original code. They cannot be killed because there is no observable difference.

### Common Equivalent Mutant Patterns

**Pattern 1: Operations with identity elements**

```python
# Mutant in conditional where both branches have same effect
if whatever:
    number += 0  # Can mutate to -= 0, *= 1, /= 1 - all equivalent!
else:
    number += 0
```

**Pattern 2: Boundary conditions that don't affect outcome**

```python
# When max equals min, condition doesn't matter
max_val = max(a, b)
min_val = min(a, b)
if a >= b:  # Mutating to <= or < has no effect when a == b
    result = 10 ** (max_val - min_val)  # 10 ** 0 = 1 regardless
```

**Pattern 3: Dead code paths**

```python
# If this path is never reached, mutations don't matter
if impossible_condition:
    do_something()  # Mutating this won't affect behavior
```

**Pattern 4: None handling equivalences**

```python
# When value is never None in practice
if value is None:  # Mutating to == None has same effect
    return default
```

### How to Handle Equivalent Mutants

1. **Identify**: Analyze if mutation truly changes observable behavior
2. **Document**: Note why mutant is equivalent
3. **Accept**: 100% mutation score may not be achievable
4. **Consider refactoring**: Sometimes equivalent mutants indicate unclear code

---

## Branch Analysis Checklist

When analyzing code changes on a branch:

### For Each Function/Method Changed:

- [ ] **Arithmetic operators**: Would changing +, -, *, /, //, %, ** be detected?
- [ ] **Conditionals**: Are boundary values tested (>=, <=)?
- [ ] **Boolean logic**: Are all branches of and, or tested?
- [ ] **Identity checks**: Is `is` vs `==` tested (especially for None)?
- [ ] **Membership**: Are `in` and `not in` tested?
- [ ] **Return statements**: Would changing return value be detected?
- [ ] **Method calls**: Would removing or swapping methods be detected?
- [ ] **String literals**: Would empty strings be detected?
- [ ] **List/dict/set operations**: Would empty collections be detected?
- [ ] **List comprehensions**: Would mutated comprehensions be detected?
- [ ] **Exception handling**: Would removed exception blocks be detected?

### Red Flags (Likely Surviving Mutants):

- [ ] Tests only verify "no exception raised"
- [ ] Tests only check one side of a condition
- [ ] Tests use identity values (0, 1, empty string, empty list)
- [ ] Tests only verify function was called, not with what
- [ ] Tests don't verify return values
- [ ] Boundary values not tested
- [ ] None cases not tested

### Questions to Ask:

1. "If I changed this operator, would a test fail?"
2. "If I negated this condition, would a test fail?"
3. "If I removed this line, would a test fail?"
4. "If I returned early here, would a test fail?"
5. "If I changed `is` to `==`, would a test fail?"

---

## Strengthening Weak Tests

### Pattern: Add Boundary Value Tests

```python
# Original weak test
def test_validates_age():
    assert is_adult(25) is True
    assert is_adult(10) is False

# Strengthened with boundary values
def test_validates_age_at_boundary():
    assert is_adult(17) is False  # Just below
    assert is_adult(18) is True   # Exactly at boundary
    assert is_adult(19) is True   # Just above
```

### Pattern: Test Both Branches of Conditions

```python
# Original weak test - only tests one branch
def test_returns_access_result():
    assert can_access(True, True) is True

# Strengthened - tests all meaningful combinations
def test_grants_access_when_admin():
    assert can_access(True, False) is True

def test_grants_access_when_owner():
    assert can_access(False, True) is True

def test_denies_access_when_neither():
    assert can_access(False, False) is False
```

### Pattern: Avoid Identity Values

```python
# Weak - uses identity values
def test_calculates():
    assert multiply(10, 1) == 10  # x * 1 = x / 1
    assert add(5, 0) == 5         # x + 0 = x - 0

# Strong - uses values that reveal operator differences
def test_calculates():
    assert multiply(10, 3) == 30  # 10 * 3 != 10 / 3
    assert add(5, 3) == 8         # 5 + 3 != 5 - 3
```

### Pattern: Verify Side Effects

```python
# Weak - no verification of side effects
def test_processes_order():
    process_order(order)
    # No assertions!

# Strong - verifies observable outcomes
def test_processes_order(mock_repository, mock_email):
    process_order(order)
    mock_repository.save.assert_called_once_with(order)
    mock_email.send.assert_called_once()
    assert mock_email.send.call_args[0][0].to == order.customer_email
```

### Pattern: Test None Handling Explicitly

```python
# Weak - doesn't test None case
def test_get_value():
    assert get_value("key") == "value"

# Strong - tests both None and non-None paths
def test_get_value_with_existing_key():
    assert get_value("key") == "value"

def test_get_value_with_missing_key():
    assert get_value("missing") is None
```

### Pattern: Test List Comprehension Logic

```python
# Production code
def get_active_users(users: list[User]) -> list[User]:
    return [user for user in users if user.is_active]

# Weak - doesn't verify filtering logic
def test_returns_list():
    users = [User(active=True), User(active=False)]
    result = get_active_users(users)
    assert isinstance(result, list)

# Strong - verifies filtering behavior
def test_returns_only_active_users():
    active = User(name="Alice", active=True)
    inactive = User(name="Bob", active=False)
    users = [active, inactive]

    result = get_active_users(users)

    assert result == [active]
    assert inactive not in result
```

---

## Python-Specific Patterns

### Dictionary Operations

```python
# Production code
def get_config(key: str, default=None):
    config = {"timeout": 30}
    return config.get(key, default)

# Mutant: config[key]  (removes .get, raises KeyError for missing keys)

# ❌ WEAK TEST - Doesn't test missing key case
def test_get_config():
    assert get_config("timeout") == 30

# ✅ STRONG TEST - Tests both paths
def test_get_config_existing_key():
    assert get_config("timeout") == 30

def test_get_config_missing_key():
    assert get_config("missing", "default") == "default"
```

### None Handling (is vs ==)

```python
# Production code
def process(value):
    if value is None:
        return "default"
    return value

# Mutant: if value == None

# ✅ STRONG TEST - Should pass for both (they're often equivalent)
# But test with empty string to verify behavior difference
def test_process_with_none():
    assert process(None) == "default"

def test_process_with_empty_string():
    assert process("") == ""  # Would fail if mutated to == None
```

### Exception Handling

```python
# Production code
def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Mutant: if b != 0 (inverts condition)

# ❌ WEAK TEST - Only tests happy path
def test_divide():
    assert divide(10, 2) == 5

# ✅ STRONG TEST - Tests both paths
def test_divide_normal():
    assert divide(10, 2) == 5

def test_divide_by_zero_raises():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)
```

### List Comprehensions with Conditions

```python
# Production code
def get_even_squares(numbers: list[int]) -> list[int]:
    return [n ** 2 for n in numbers if n % 2 == 0]

# Possible mutants:
# - n ** 2 → n * 2
# - n % 2 == 0 → n % 2 != 0

# ✅ STRONG TEST - Would catch both mutants
def test_get_even_squares():
    result = get_even_squares([1, 2, 3, 4, 5])
    assert result == [4, 16]  # 2**2=4, 4**2=16
    # Would fail if:
    # - n*2 was used: [4, 8]
    # - % != was used: [1, 9, 25]
```

---

## Integration with mutmut

For automated mutation testing, use mutmut:

### Installation

```bash
uv add mutmut --group test
```

### Configuration (pyproject.toml)

```toml
[tool.mutmut]
paths_to_mutate = "src/"
backup = false
runner = "pytest -x"
tests_dir = "tests/"
```

### Running mutmut

```bash
# Run mutation testing
mutmut run

# Show results summary
mutmut results

# Show specific mutant
mutmut show 1

# Generate HTML report
mutmut html
```

### Incremental Mode (for branches)

```bash
# Only mutate modified lines
mutmut run --paths-to-mutate=src/module.py
```

### Workflow Integration

```bash
# 1. Run mutation testing
mutmut run

# 2. Check results
mutmut results

# 3. View surviving mutants
mutmut show survived

# 4. View specific mutant details
mutmut show 5

# 5. Apply mutant to see the change
mutmut apply 5

# 6. Fix tests, then reset
git checkout -- .

# 7. Re-run to verify fix
mutmut run
```

---

## Summary: Mutation Testing Mindset

**The key question for every line of code:**

> "If I introduced a bug here, would my tests catch it?"

**For each test, verify it would catch:**
- Arithmetic operator changes (+, -, *, /, //, %, **)
- Boundary condition shifts (>=, <=)
- Boolean logic inversions (and, or, not)
- Identity check changes (is, ==)
- Membership test inversions (in, not in)
- Removed statements
- Changed return values
- Empty collections
- None values

**Remember:**
- Coverage measures execution, mutation testing measures detection
- A test that doesn't make assertions can't kill mutants
- Boundary values are critical for conditional mutations
- Avoid identity values that make operators interchangeable
- Test None explicitly with `is None`
- Test empty collections explicitly
- Verify side effects with mock assertions

---

## Quick Reference

### Operators Most Likely to Have Surviving Mutants

1. `>=` vs `>` (boundary not tested)
2. `and` vs `or` (only tested when both true/false)
3. `+` vs `-` (only tested with 0)
4. `*` vs `/` (only tested with 1)
5. `all()` vs `any()` (only tested with all matching)
6. `is` vs `==` (only tested with non-None values)
7. `in` vs `not in` (only tested one direction)

### Test Values That Kill Mutants

| Avoid | Use Instead |
|-------|-------------|
| 0 (for +/-) | Non-zero values |
| 1 (for */) | Values > 1 |
| Empty lists | Lists with multiple items |
| Identical values for comparisons | Distinct values |
| All True/False for logical ops | Mixed True/False |
| Only non-None values | Test both None and non-None |
| Only present keys | Test missing keys too |

### Python-Specific Gotchas

| Pattern | Why It's Weak | How to Strengthen |
|---------|---------------|-------------------|
| Testing `is None` only | Doesn't verify `== None` difference | Test with `""`, `0`, `[]` |
| Testing `.get()` only with existing keys | Doesn't verify default behavior | Test missing keys |
| Testing list comprehensions with all matches | Doesn't verify filter logic | Mix matching and non-matching items |
| Testing only happy path exceptions | Doesn't verify exception conditions | Use `pytest.raises()` |
| Testing only `and` with both True | Doesn't verify operator choice | Test with mixed True/False |