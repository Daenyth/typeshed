# Stubs for redis.client (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional, Text


class StrictRedis:
    @classmethod
    def from_url(cls, url: Text, db: Optional[int] = ..., **kwargs): ...
    def __init__(self, host: str = ..., port: int = ..., db: int = ..., password: Optional[Any] = ..., socket_timeout: Optional[Any] = ..., socket_connect_timeout: Optional[Any] = ..., socket_keepalive: Optional[Any] = ..., socket_keepalive_options: Optional[Any] = ..., connection_pool: Optional[Any] = ..., unix_socket_path: Optional[Any] = ..., encoding: str = ..., encoding_errors: str = ..., charset: Optional[Any] = ..., errors: Optional[Any] = ..., decode_responses: bool = ..., retry_on_timeout: bool = ..., ssl: bool = ..., ssl_keyfile: Optional[Any] = ..., ssl_certfile: Optional[Any] = ..., ssl_cert_reqs: Optional[Any] = ..., ssl_ca_certs: Optional[Any] = ..., max_connections: Optional[Any] = ...) -> None: ...
    def set_response_callback(self, command, callback): ...
    def pipeline(self, transaction: bool = ..., shard_hint: Optional[Any] = ...): ...
    def transaction(self, func, *watches, **kwargs): ...
    def lock(self, name, timeout: Optional[Any] = ..., sleep: float = ..., blocking_timeout: Optional[Any] = ..., lock_class: Optional[Any] = ..., thread_local: bool = ...): ...
    def pubsub(self, **kwargs): ...
    def execute_command(self, *args, **options): ...
    def parse_response(self, connection, command_name, **options): ...
    def bgrewriteaof(self): ...
    def bgsave(self): ...
    def client_kill(self, address): ...
    def client_list(self): ...
    def client_getname(self): ...
    def client_setname(self, name): ...
    def config_get(self, pattern: str = ...): ...
    def config_set(self, name, value): ...
    def config_resetstat(self): ...
    def config_rewrite(self): ...
    def dbsize(self): ...
    def debug_object(self, key): ...
    def echo(self, value): ...
    def flushall(self): ...
    def flushdb(self): ...
    def info(self, section: Optional[Any] = ...): ...
    def lastsave(self): ...
    def object(self, infotype, key): ...
    def ping(self): ...
    def save(self): ...
    def sentinel(self, *args): ...
    def sentinel_get_master_addr_by_name(self, service_name): ...
    def sentinel_master(self, service_name): ...
    def sentinel_masters(self): ...
    def sentinel_monitor(self, name, ip, port, quorum): ...
    def sentinel_remove(self, name): ...
    def sentinel_sentinels(self, service_name): ...
    def sentinel_set(self, name, option, value): ...
    def sentinel_slaves(self, service_name): ...
    def shutdown(self): ...
    def slaveof(self, host: Optional[Any] = ..., port: Optional[Any] = ...): ...
    def slowlog_get(self, num: Optional[Any] = ...): ...
    def slowlog_len(self): ...
    def slowlog_reset(self): ...
    def time(self): ...
    def wait(self, num_replicas, timeout): ...
    def append(self, key, value): ...
    def bitcount(self, key, start: Optional[Any] = ..., end: Optional[Any] = ...): ...
    def bitop(self, operation, dest, *keys): ...
    def bitpos(self, key, bit, start: Optional[Any] = ..., end: Optional[Any] = ...): ...
    def decr(self, name, amount: int = ...): ...
    def delete(self, *names): ...
    def __delitem__(self, name): ...
    def dump(self, name): ...
    def exists(self, name): ...
    __contains__ = ...  # type: Any
    def expire(self, name, time): ...
    def expireat(self, name, when): ...
    def get(self, name): ...
    def __getitem__(self, name): ...
    def getbit(self, name, offset): ...
    def getrange(self, key, start, end): ...
    def getset(self, name, value): ...
    def incr(self, name, amount: int = ...): ...
    def incrby(self, name, amount: int = ...): ...
    def incrbyfloat(self, name, amount: float = ...): ...
    def keys(self, pattern: str = ...): ...
    def mget(self, keys, *args): ...
    def mset(self, *args, **kwargs): ...
    def msetnx(self, *args, **kwargs): ...
    def move(self, name, db): ...
    def persist(self, name): ...
    def pexpire(self, name, time): ...
    def pexpireat(self, name, when): ...
    def psetex(self, name, time_ms, value): ...
    def pttl(self, name): ...
    def randomkey(self): ...
    def rename(self, src, dst): ...
    def renamenx(self, src, dst): ...
    def restore(self, name, ttl, value): ...
    def set(self, name, value, ex: Optional[Any] = ..., px: Optional[Any] = ..., nx: bool = ..., xx: bool = ...): ...
    def __setitem__(self, name, value): ...
    def setbit(self, name, offset, value): ...
    def setex(self, name, time, value): ...
    def setnx(self, name, value): ...
    def setrange(self, name, offset, value): ...
    def strlen(self, name): ...
    def substr(self, name, start, end: int = ...): ...
    def ttl(self, name): ...
    def type(self, name): ...
    def watch(self, *names): ...
    def unwatch(self): ...
    def blpop(self, keys, timeout: int = ...): ...
    def brpop(self, keys, timeout: int = ...): ...
    def brpoplpush(self, src, dst, timeout: int = ...): ...
    def lindex(self, name, index): ...
    def linsert(self, name, where, refvalue, value): ...
    def llen(self, name): ...
    def lpop(self, name): ...
    def lpush(self, name, *values): ...
    def lpushx(self, name, value): ...
    def lrange(self, name, start, end): ...
    def lrem(self, name, count, value): ...
    def lset(self, name, index, value): ...
    def ltrim(self, name, start, end): ...
    def rpop(self, name): ...
    def rpoplpush(self, src, dst): ...
    def rpush(self, name, *values): ...
    def rpushx(self, name, value): ...
    def sort(self, name, start: Optional[Any] = ..., num: Optional[Any] = ..., by: Optional[Any] = ..., get: Optional[Any] = ..., desc: bool = ..., alpha: bool = ..., store: Optional[Any] = ..., groups: bool = ...): ...
    def scan(self, cursor: int = ..., match: Optional[Any] = ..., count: Optional[Any] = ...): ...
    def scan_iter(self, match: Optional[Any] = ..., count: Optional[Any] = ...): ...
    def sscan(self, name, cursor: int = ..., match: Optional[Any] = ..., count: Optional[Any] = ...): ...
    def sscan_iter(self, name, match: Optional[Any] = ..., count: Optional[Any] = ...): ...
    def hscan(self, name, cursor: int = ..., match: Optional[Any] = ..., count: Optional[Any] = ...): ...
    def hscan_iter(self, name, match: Optional[Any] = ..., count: Optional[Any] = ...): ...
    def zscan(self, name, cursor: int = ..., match: Optional[Any] = ..., count: Optional[Any] = ..., score_cast_func: Any = ...): ...
    def zscan_iter(self, name, match: Optional[Any] = ..., count: Optional[Any] = ..., score_cast_func: Any = ...): ...
    def sadd(self, name, *values): ...
    def scard(self, name): ...
    def sdiff(self, keys, *args): ...
    def sdiffstore(self, dest, keys, *args): ...
    def sinter(self, keys, *args): ...
    def sinterstore(self, dest, keys, *args): ...
    def sismember(self, name, value): ...
    def smembers(self, name): ...
    def smove(self, src, dst, value): ...
    def spop(self, name): ...
    def srandmember(self, name, number: Optional[Any] = ...): ...
    def srem(self, name, *values): ...
    def sunion(self, keys, *args): ...
    def sunionstore(self, dest, keys, *args): ...
    def zadd(self, name, *args, **kwargs): ...
    def zcard(self, name): ...
    def zcount(self, name, min, max): ...
    def zincrby(self, name, value, amount: int = ...): ...
    def zinterstore(self, dest, keys, aggregate: Optional[Any] = ...): ...
    def zlexcount(self, name, min, max): ...
    def zrange(self, name, start, end, desc: bool = ..., withscores: bool = ..., score_cast_func: Any = ...): ...
    def zrangebylex(self, name, min, max, start: Optional[Any] = ..., num: Optional[Any] = ...): ...
    def zrevrangebylex(self, name, max, min, start: Optional[Any] = ..., num: Optional[Any] = ...): ...
    def zrangebyscore(self, name, min, max, start: Optional[Any] = ..., num: Optional[Any] = ..., withscores: bool = ..., score_cast_func: Any = ...): ...
    def zrank(self, name, value): ...
    def zrem(self, name, *values): ...
    def zremrangebylex(self, name, min, max): ...
    def zremrangebyrank(self, name, min, max): ...
    def zremrangebyscore(self, name, min, max): ...
    def zrevrange(self, name, start, end, withscores: bool = ..., score_cast_func: Any = ...): ...
    def zrevrangebyscore(self, name, max, min, start: Optional[Any] = ..., num: Optional[Any] = ..., withscores: bool = ..., score_cast_func: Any = ...): ...
    def zrevrank(self, name, value): ...
    def zscore(self, name, value): ...
    def zunionstore(self, dest, keys, aggregate: Optional[Any] = ...): ...
    def pfadd(self, name, *values): ...
    def pfcount(self, *sources): ...
    def pfmerge(self, dest, *sources): ...
    def hdel(self, name, *keys): ...
    def hexists(self, name, key): ...
    def hget(self, name, key): ...
    def hgetall(self, name): ...
    def hincrby(self, name, key, amount: int = ...): ...
    def hincrbyfloat(self, name, key, amount: float = ...): ...
    def hkeys(self, name): ...
    def hlen(self, name): ...
    def hset(self, name, key, value): ...
    def hsetnx(self, name, key, value): ...
    def hmset(self, name, mapping): ...
    def hmget(self, name, keys, *args): ...
    def hvals(self, name): ...
    def publish(self, channel, message): ...
    def eval(self, script, numkeys, *keys_and_args): ...
    def evalsha(self, sha, numkeys, *keys_and_args): ...
    def script_exists(self, *args): ...
    def script_flush(self): ...
    def script_kill(self): ...
    def script_load(self, script): ...
    def register_script(self, script): ...
