import logging
import logging.config
import json

logger = logging.getLogger(__name__)


def logger_configuration():
    try:
        with open("configs/logger_configuration.json", 'r') as logging_configuration_file:
            config_dict = json.load(logging_configuration_file)
        logging.config.dictConfig(config_dict)
        logger.debug("Logger has been configured")
    except Exception:
        print('Exception occurred while reading logger_configuration JSON file')


def main():
    logger_configuration()
    logger.info("Starting the Currency Converter program")


if __name__ == '__main__':
    main()
