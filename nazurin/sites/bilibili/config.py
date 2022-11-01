from nazurin.config import env

PRIORITY = 4
COLLECTION = 'bilibili'

with env.prefixed('BILIBILI'):
    with env.prefixed('FILE_'):
        DESTINATION: str = env.str('PATH', default='Bilibili')
