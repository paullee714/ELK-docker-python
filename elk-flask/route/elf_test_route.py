from flask import Blueprint

from elk_lib import elk_logger

elk_test = Blueprint('elk_test', __name__)


@elk_test.route('/', methods=['GET'])
def elk_test_show():

    logger = elk_logger.create_logger('elk-test-logger')
    logger.info('hello elk-test-logstash')

    return "hello world!"
