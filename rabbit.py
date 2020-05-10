try:
    import configparser
    import json
    import pika
    from pika.exceptions import UnroutableError, NackError
    import configparser
    import json
except Exception as e:
    print('some Python modules are missing {}'.format_map(e))
try:
    parser = configparser.ConfigParser()
    parser.read('config.ini')
except configparser.ParsingError as err:
    print("Config not Found {}".format_map(err))

# set up the receiver
def receive():
