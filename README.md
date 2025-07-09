Pytest xdist: Emulator and Appium Port Distribution Snippet for Workers
This snippet automatically assigns a udid and appium_port to each pytest-xdist worker based on its ID (gw0, gw1, ...).

Used for parallel Android UI test execution on multiple emulators
Provides a device_config fixture with per-worker parameters
Supports override via CLI (--appium_port, --udid)
Simplifies parallel test runs: pytest -n 5 tests/
Suitable for both local development and CI environments (e.g. GitLab Runner).
