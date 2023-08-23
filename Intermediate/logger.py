# Default logger
import logging

logging.basicConfig(level=logging.DEBUG)

logging.info("You have 20 new messages.")
logging.critical("Severe damage sustained to engine. Address now.")
logging.warning("Your tank is below 30% filled.")


# Custom logger

logger = logging.getLogger('Seansama Logger')
logger.info('Logger succesfully created')
logger.critical('You did not code today.')
logger.log(logging.ERROR, 'An error occured')

# Logging into files

handler = logging.FileHandler('mylog.log')
handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(levelname)s - %(asctime)s: %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)
logger.debug("This is a logging test")
logger.info('Be careful.')
