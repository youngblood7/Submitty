import os
import json
import shutil
import sys
import unittest
import contextlib

# Done to avoid making the base autograder directory a module.
# This import must be done inside of the class for the mock to take affect
sys.path.append("..")
import autograder
from autograder import config
import submitty_autograding_shipper as shipper

# The directory in which this script will be run
SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
# Equivalent to install dir
TEST_ENVIRONMENT = os.path.join(SCRIPT_DIR, 'test_environment')

# Directory to which system configuration files will be installed
CONFIG_DIR = os.path.join(TEST_ENVIRONMENT, 'config')

# Directories in which autograding will take place
DATA_DIR = os.path.join(TEST_ENVIRONMENT, 'autograding')
TODO_DIR = os.path.join(DATA_DIR, 'autograding_TODO')
DONE_DIR = os.path.join(DATA_DIR, 'autograding_DONE')
TO_BE_GRADED = os.path.join(DATA_DIR, 'to_be_graded_queue')
GRADING = os.path.join(DATA_DIR, "grading")

# Autograding log directories
LOG_PATH = os.path.join(TEST_ENVIRONMENT, 'logs')
STACK_TRACES = os.path.join(LOG_PATH, 'autograding_stack_traces')
AUTOGRADING_LOGS = os.path.join(LOG_PATH, 'autograding')

# JSON files to be installed into the CONFIG_DIR

SUBMITTY_JSON = {
    'submitty_data_dir' : DATA_DIR,
    'submitty_install_dir' : TEST_ENVIRONMENT,
    'autograding_log_path' : AUTOGRADING_LOGS,
    'site_log_path' : LOG_PATH,
    'submission_url' : '/fake/url/for/submission/',
    'vcs_url' : '/fake/url/for/vcs/submission/'
}
USERS_JSON = {
    # Pretend that we are the daemon user.
    'daemon_uid': os.getuid()
}
# The database json is required by autograder/insert_database_version_data.py
# When we test that script, a mock database may be needed, and these
# values will have to be updated.
DATABASE_JSON = {
    'database_user' : 'foo',
    'database_host' : 'bar',
    'database_password' : 'password'
}


class TestAutogradingShipper(unittest.TestCase):
    """Unittest TestCase."""

    @classmethod
    def setUpClass(cls):
        """
        Sets up a mock environment roughly equivalent to the production server.
        As more features are needed, they should be added here
        """

        # Remove the test environment if it is left over from a previous run.
        # Should be handled by the tearDownClass function.
        with contextlib.suppress(FileNotFoundError):
            shutil.rmtree(TEST_ENVIRONMENT)

        # All testing will take place within the TEST_ENVIRONMENT directory
        os.mkdir(TEST_ENVIRONMENT)

        # A mock of /usr/local/submitty/config
        os.mkdir(CONFIG_DIR)

        for filename, json_file in [
            ('submitty', SUBMITTY_JSON),
            ('submitty_users', USERS_JSON),
            ('database', DATABASE_JSON)
        ]:
            with open(os.path.join(CONFIG_DIR, f'{filename}.json'), 'w') as outfile:
                json.dump(json_file, outfile, indent=4)

        # A mock directory for /var/local/submitty
        os.mkdir(DATA_DIR)
        for directory in [TODO_DIR, DONE_DIR, TO_BE_GRADED, GRADING]:
            os.mkdir(directory)

        # A mock directory for /var/local/submitty/logs
        os.mkdir(LOG_PATH)
        for directory in [STACK_TRACES, AUTOGRADING_LOGS]:
            os.mkdir(directory)

    @classmethod
    def tearDownClass(cls):
        """ Removes the environment created for these testcases """

        with contextlib.suppress(FileNotFoundError):
            shutil.rmtree(TEST_ENVIRONMENT)

    def test_can_short_circuit_no_testcases(self):
        autograding_config = {
            "testcases" : []
        }
        self.assertTrue(shipper.can_short_circuit(autograding_config))

    def test_can_short_circuit_max_submission(self):
        """ We should be able to short circuit if the only testcase is max_submission """
        with open(os.path.join(SCRIPT_DIR, 'data', 'complete_config_upload_only.json')) as infile:
            autograding_config = json.load(infile)
        self.assertTrue(shipper.can_short_circuit(autograding_config))

    def test_cannot_short_circuit_single_non_file_submission_testcase(self):
        """
        If there is only one testcase, but it is non-file submission, we cannot short circuit.
        """
        with open(os.path.join(SCRIPT_DIR, 'data', 'complete_config_cpp_cats.json')) as infile:
            autograding_config = json.load(infile)
        # Create an autograding_config that is a copy of cpp cats but with only one testcase.
        autograding_config['testcases'] = [autograding_config['testcases'][0]]

        self.assertFalse(shipper.can_short_circuit(autograding_config))

    def test_cannot_short_circuit_many_testcases(self):
        """ We cannot short circuit if there are multiple testcases. """

        with open(os.path.join(SCRIPT_DIR, 'data', 'complete_config_cpp_cats.json')) as infile:
            autograding_config = json.load(infile)
        self.assertFalse(shipper.can_short_circuit(autograding_config))

