from .database import *
import redis

redis_db = redis.Redis(host=config["Redis"]["host"], port=config.get("Redis", "port"))
