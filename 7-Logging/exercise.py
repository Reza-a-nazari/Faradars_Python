print('Enter your name : ')
user_ = input() # input name
print()
print("EnterYourPassword")

password_ = input()

import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename='UserPass.log',
    format='%(levelname)s -- %(asctime)s -- %(message)s.',
    datefmt='%Y-%m-%d  %H:%M:%S'
)

logging.debug(f'User With Username {hash(user_)} and Password {hash(password_)}')
logging.info(f'User With Username {hash(user_)} and Password {hash(password_)}')
logging.warning(f'User With Username {hash(user_)} and Password {hash(password_)}')
logging.error(f'User With Username {hash(user_)} and Password {hash(password_)}')
logging.critical(f'User With Username {hash(user_)} and Password {hash(password_)}')





