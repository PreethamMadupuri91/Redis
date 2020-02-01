import redis

r = redis.StrictRedis(host='localhost', port=6379, password='', decode_responses=True)
r.set("msg:hello","Hello Redis!!!")
msg = r.get("msg:hello")
print(msg)


