import logging

###

# https://docs.python.org/3/library/logging.html#logrecord-attributes#

###


# import os
# path = os.path.dirname(os.path.abspath(__file__))
# logfile =f'{path}\\app1.log'
logging.basicConfig(level=logging.DEBUG ,
                    #format="%(message)s hi" ,
                    filename='app1.log',
                    #filename = logfile
                    filemode='a',
                    format='%(levelname)s -- %(asctime)s -- %(filename)s:%(lineno)d -- %(message)s',
                    datefmt='%Y-%m-%d  %H-%M-%S'

)

logging.debug(f'This is a debug{logging.DEBUG} level log.')
logging.info((f'This is a info {logging.INFO} level log.'))
logging.warning((f'This is a warning {logging.WARNING} level log.'))
logging.error((f'This is a error {logging.ERROR} level log.'))
logging.critical((f'This is a critical {logging.CRITICAL} level log.'))