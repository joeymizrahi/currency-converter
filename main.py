import logging
import logging.config
import json
from Converter import Converter
import sys
logger = logging.getLogger(__name__)


def logger_configuration():
    """
    define the logger for this program
    """
    try:
        with open("configs/logger_configuration.json", 'r') as logging_configuration_file:
            config_dict = json.load(logging_configuration_file)
        logging.config.dictConfig(config_dict)
        logger.debug("Logger has been configured")
    except Exception:
        print('Exception occurred while reading logger_configuration JSON file')


def convert_from_file(filename):
    converter = Converter()
    with open(filename, "r")as f:
        lines = [line.rstrip() for line in f.readlines()]
    from_currency = lines[0]
    to_currency = lines[1]
    for ammount in lines[2:]:
        print(converter.convert(from_currency, to_currency, float(ammount)))


def main():
    logger_configuration()
    logger.info("Starting the Currency Converter program")
    assert len(sys.argv) == 2, "Did you give me a filename?"
    convert_from_file(sys.argv[1])


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        logger.exception(e)
