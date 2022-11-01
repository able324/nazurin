from nazurin.config import env

PRIORITY = 5
COLLECTION = 'weibo'

with env.prefixed('WEIBO_'):
    with env.prefixed('FILE_'):
        DESTINATION: str = env.str('PATH', default='Weibo')
