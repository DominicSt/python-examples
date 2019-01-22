import base64
import sys
import logging

logger = logging.getLogger('decode_base64')
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.info("Checking file: " + sys.argv[1])
input_file = open(sys.argv[1], 'r').read()


def is_base64(str):
    try:
        base64.b64decode(str)
        return True
    except Exception as e:
        return False


def decode(file):
    logger.info("Decoding Secret.")
    decoded_file = base64.b64decode(file)
    print(decoded_file)

    return decoded_file


def save_file(file):
    logger.info("Saving decoded secret.")
    open(sys.argv[1], 'w').write(file.decode("utf-8"))


if is_base64(input_file):
    logger.info("input is Base64-encoded.")
    decoded_file = decode(input_file)
    save_file(decoded_file)
else:
    logger.info("input is NOT Base64-encoded.")
