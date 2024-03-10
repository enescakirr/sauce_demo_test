import pytest

from base.database_controller import DatabaseController


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()
    if result.when == 'call' or (result.when == 'setup' and result.when != 'passed'):
        case_name = result.nodeid
        case_path = result.fspath
        if result.failed:
            stack_trace = result.longreprtext + "\n" + result.capstdout
        else:
            stack_trace = result.capstdout
        case_status = result.outcome
        duration = result.duration
        DatabaseController.insert_data(case_name, case_path, case_status)
