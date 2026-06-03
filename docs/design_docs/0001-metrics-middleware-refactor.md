---
created: 2026-06-03
status: Proposed
---

# MetricsMiddleware Refactor

## Overview

Decouple `MetricsMiddleware` from hardcoded dependencies, fix known bugs, and achieve >90% test coverage. The middleware pattern is the right abstraction for telemetry (cross-cutting concern), but the current implementation violates Dependency Inversion, contains a logic bug in config path extraction, and is untestable in isolation.

## Objectives

- Make `MetricsMiddleware` testable by injecting all dependencies
- Prevent success metrics with "unknown" config data from being sent
- Fix config path extraction bug (`["--config", "-c"] in ctx.args` never matches)
- Achieve >90% test coverage on the middleware
- Keep the middleware pattern — telemetry stays as a cross-cutting concern outside business logic

## Requirements

### Functional Requirements

- Success metrics are only sent when the project config snapshot has real data
- Error metrics are always sent regardless of config state
- Custom `--config`/`-c` paths are correctly resolved when extracting the config snapshot
- The middleware delegates to `UsageMetricsSender` for both success and error paths

### Non-Functional Requirements

- Zero impact on existing CLI behavior or output
- All existing tests continue to pass
- `MetricsMiddleware` test coverage rises from 48% to >90%
- Metrics sending remains fire-and-forget (daemon thread with timeout)
- No additional latency on the CLI command — thread timeout stays at 5 seconds

## Usage Examples

### Before: Hardcoded dependencies

```python
class MetricsMiddleware(TyperGroup):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._config_snapshot_creator = ConfigSnapshotCreator(repository=YamlConfigRepository())
        self._metrics_sender = UsageMetricsSender(
            reporter=PostHogMetricsReporter(
                config=PostHogConfig(),
                user_identity_manager=UserIdentityManager(),
            ),
        )
```

### After: Injected dependencies

```python
class MetricsMiddleware(TyperGroup):
    def __init__(self, *args, config_snapshot_creator: ConfigSnapshotCreator, metrics_sender: UsageMetricsSender, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._config_snapshot_creator = config_snapshot_creator
        self._metrics_sender = metrics_sender
```

### Wiring in `cli.py`

```python
app = InstantPythonTyper(
    cls=lambda *args, **kwargs: MetricsMiddleware(
        *args,
        config_snapshot_creator=ConfigSnapshotCreator(repository=YamlConfigRepository()),
        metrics_sender=UsageMetricsSender(
            reporter=PostHogMetricsReporter(
                config=PostHogConfig(),
                user_identity_manager=UserIdentityManager(),
            ),
        ),
        **kwargs,
    )
)
```

Or use a factory function to keep `cli.py` clean:

```python
def _build_metrics_middleware(*args, **kwargs) -> MetricsMiddleware:
    return MetricsMiddleware(
        *args,
        config_snapshot_creator=ConfigSnapshotCreator(repository=YamlConfigRepository()),
        metrics_sender=UsageMetricsSender(
            reporter=PostHogMetricsReporter(
                config=PostHogConfig(),
                user_identity_manager=UserIdentityManager(),
            ),
        ),
        **kwargs,
    )

app = InstantPythonTyper(cls=_build_metrics_middleware)
```

## Implementation Steps

### Step 1 — Inject dependencies, add unknown-snapshot guard, and test

**Files:** `metrics_middleware.py`, `cli.py`, `test_metrics_middleware.py`

- Accept `ConfigSnapshotCreator` and `UsageMetricsSender` via constructor
- Update `cli.py` to pass them via `cls=` factory
- Keep the early return for unknown config snapshots (already in place)
- Write tests covering:
  - Successful command sends success metrics
  - Failed command sends error metrics
  - Unknown config snapshot skips success metrics
  - Guard is triggered for unknown snapshots

### Step 2 — Fix config path extraction

**Files:** `metrics_middleware.py`

- Replace `["--config", "-c"] in ctx.args` with proper access to the resolved parameter value
- Typer exposes `--config`/`-c` as a function parameter on the command callback, but the middleware can't access it directly since it runs at the group level. Alternative: use `ctx.params` after Click/Typer has resolved parameters, or inspect `ctx.args` with proper `"<value>" in ctx.args` for each string individually
- Write tests for:
  - Default path (`ipy.yml`) when no `--config` is passed
  - Custom path when `--config custom.yml` is passed
  - Custom path when `-c custom.yml` is passed

### Step 3 — Simplify thread/timeout strategy (optional)

**Files:** `metrics_middleware.py`

- Extract the daemon-thread-with-timeout pattern into a small utility to avoid duplication between `_send_metrics_data` and `_send_error_data`
- Keep `timeout=5.0` as configurable but defaulted
- Write tests for the utility

## Open Questions

- Should `MetricsMiddleware` stop extending `TyperGroup`? Click provides alternative hooks like `@app.result_callback` or wrapping at the `InstantPythonTyper` level. Dropping the inheritance would make the middleware purely compositional. However, `invoke()` override is the simplest hook — `result_callback` only fires on success, and there's no built-in error callback equivalent.
- Should the `_extract_config_path` bug be fixed separately or as part of this effort? It's technically independent, but the middleware is the only place that uses it, so fixing it now avoids a future iteration.

## Notes

- The `cls=` parameter in Typer accepts either a class or a callable. A `lambda` or factory function works cleanly for injecting dependencies.
- Already in place (from the live review session): the early return guard in `_send_success_metrics` for unknown snapshots.
- Existing technical debt items this addresses: DT-1 (hardcoded deps), DT-2 (config path bug), and partially DT-9 (missing tests).
