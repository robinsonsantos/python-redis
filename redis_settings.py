import sys
sys.path.append('/home/root/smaai')
import redis 

config = {
    'host': 'localhost',
    'port': 6379,
    'db': 0,
}

r = redis.StrictRedis(**config)
