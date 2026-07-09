from .bases import BATIMTestBase

class TestBasics(BATIMTestBase):
    options = {
        "dummy_option": False,
    }

    run_default_tests = False