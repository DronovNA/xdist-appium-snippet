EMULATOR_UDIDS = [
    "emulator-5554",
    "emulator-5556",
    "emulator-5558",
    "emulator-5560",
    "emulator-5562"
]

APPIUM_PORTS = [
    4723,
    4725,
    4727,
    4729,
    4731
]

def pytest_configure(config):
    worker_id = os.environ.get('PYTEST_XDIST_WORKER', 'gw0')
    index = int(worker_id.replace('gw', '0'))

    config.udid = EMULATOR_UDIDS[index]
    config.appium_port = APPIUM_PORTS[index]

@pytest.fixture(scope="session")
def device_config(request):
    config = request.config
    return {
        "udid": config.udid,
        "port": config.appium_port,
    }


@pytest.fixture(scope='function')
def driver(request: FixtureRequest, device_config: Dict[str, Any]):
  appium_port = request.config.getoption("appium_port") or device_config["appium_port"]
  udid = request.config.getoption("udid") or device_config["udid"]
