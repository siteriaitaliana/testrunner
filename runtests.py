import unittest
import logging
import argparse

def load_tests(loader, tests, pattern):
    ''' Discover and load all unit tests in all files named ``*.py`` in ``test_folder``
    '''
    test_folder = 'basket'
    suite = unittest.TestSuite()
    for all_test_suite in unittest.defaultTestLoader.discover(test_folder, pattern='*.py'):
        for test_suite in all_test_suite:
            suite.addTests(test_suite)
    return suite

if __name__ == '__main__':
    import skypeqa.apps.configuration_provider as cp
    config = cp.ConfigurationProvider()
    logging.config.fileConfig(cp.get_conf_file_path(config.get("log_properties")))

    ''' Command line argument parser '''
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                   help='an integer for the accumulator')
    parser.add_argument('--sum', dest='accumulate', action='store_const',
                   const=sum, default=max,
                   help='sum the integers (default: find the max)')

    args = parser.parse_args()

    logging.disable(logging.DEBUG)
    logging.disable(logging.INFO)
    logging.disable(logging.CRITICAL)
    logging.disable(logging.ERROR)

#    unittest.TextTestRunner(verbosity=2).run(suite())
    unittest.main(failfast=False)

#TODO: failfast=True optional sys.arg
#TODO: less verbose test logs
#TODO: run tests locally against dev environment
#TODO: find a way to run this from maven or ant
