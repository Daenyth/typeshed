# Stubs for redis.client (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional, Text, Dict, Union, Callable, Type, TypeVar

import sys
from redis import ConnectionPool
import ssl

from redis.lock import Lock

if sys.version < (3, 6):
    _SslCertReq = int
else:
    _SslCertReq = ssl.VerifyMode

_TLock = TypeVar('_Tlock', Type[Lock])


class StrictRedis:
    @classmethod
    def from_url(cls, url: Text, db: Optional[int] = ..., **kwargs): ...
    def __init__(self, host: str = ..., port: int = ..., db: int = ..., password: Optional[str] = ...,
                 socket_timeout: Optional[float] = ..., socket_connect_timeout: Optional[float] = ..., socket_keepalive: Optional[bool] = ..., socket_keepalive_options: Optional[Dict[str, Union[int, bytes]]] = ...,
                 connection_pool: Optional[ConnectionPool] = ..., unix_socket_path: Optional[str] = ..., encoding: str = ..., encoding_errors: str = ..., charset: Optional[str] = ..., errors: Optional[str] = ...,
                 decode_responses: bool = ..., retry_on_timeout: bool = ...,
                 ssl: bool = ..., ssl_keyfile: Optional[str] = ..., ssl_certfile: Optional[str] = ..., ssl_cert_reqs: Optional[_SslCertReq] = ..., ssl_ca_certs: Optional[str] = ...,
                 max_connections: Optional[int] = ...) -> None: ...
    def set_response_callback(self, command: str, callback: Callable[..., Any]): ...
    def pipeline(self, transaction: bool = ..., shard_hint: Optional[Any] = ...): ...
    def transaction(self, func, *watches, **kwargs): ...
    def lock(self, name: str, timeout: Optional[float] = ..., sleep: float = ..., blocking_timeout: Optional[float] = ..., lock_class: Optional[_TLock] = ..., thread_local: bool = ...) -> _TLock: ...
    def pubsub(self, **kwargs): ...
    def execute_command(self, *args, **options): ...
    def parse_response(self, connection, command_name: str, **options): ...
    def bgrewriteaof(self): ...
    def bgsave(self): ...
    def client_kill(self, address): ...
    def client_list(self): ...
    def client_getname(self): ...
    def client_setname(self, name: str): ...
    def config_get(self, pattern: str = ...): ...
    def config_set(self, name: str, value): ...
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
    def sentinel_monitor(self, name: str, ip, port, quorum): ...
    def sentinel_remove(self, name: str): ...
    def sentinel_sentinels(self, service_name): ...
    def sentinel_set(self, name: str, option, value): ...
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
    def decr(self, name: str, amount: int = ...): ...
    def delete(self, *names): ...
    def __delitem__(self, name: str): ...
    def dump(self, name: str): ...
    def exists(self, name: str): ...
    __contains__ = ...  # type: Any
    def expire(self, name: str, time): ...
    def expireat(self, name: str, when): ...
    def get(self, name: str) -> Optional[Any]: ...
    def __getitem__(self, name: str): ...
    def getbit(self, name: str, offset): ...
    def getrange(self, key, start, end): ...
    def getset(self, name: str, value): ...
    def incr(self, name: str, amount: int = ...): ...
    def incrby(self, name: str, amount: int = ...): ...
    def incrbyfloat(self, name: str, amount: float = ...): ...
    def keys(self, pattern: str = ...): ...
    def mget(self, keys, *args): ...
    def mset(self, *args, **kwargs): ...
    def msetnx(self, *args, **kwargs): ...
    def move(self, name: str, db): ...
    def persist(self, name: str): ...
    def pexpire(self, name: str, time): ...
    def pexpireat(self, name: str, when): ...
    def psetex(self, name: str, time_ms, value): ...
    def pttl(self, name: str): ...
    def randomkey(self): ...
    def rename(self, src, dst): ...
    def renamenx(self, src, dst): ...
    def restore(self, name: str, ttl, value): ...
    def set(self, name: str, value, ex: Optional[Any] = ..., px: Optional[Any] = ..., nx: bool = ..., xx: bool = ...): ...
    def __setitem__(self, name: str, value): ...
    def setbit(self, name: str, offset, value): ...
    def setex(self, name: str, time, value): ...
    def setnx(self, name: str, value): ...
    def setrange(self, name: str, offset, value): ...
    def strlen(self, name: str): ...
    def substr(self, name: str, start, end: int = ...): ...
    def ttl(self, name: str): ...
    def type(self, name: str): ...
    def watch(self, *names): ...
    def unwatch(self): ...
    def blpop(self, keys, timeout: int = ...): ...
    def brpop(self, keys, timeout: int = ...): ...
    def brpoplpush(self, src, dst, timeout: int = ...): ...
    def lindex(self, name: str, index): ...
    def linsert(self, name: str, where, refvalue, value): ...
    def llen(self, name: str): ...
    def lpop(self, name: str): ...
    def lpush(self, name: str, *values): ...
    def lpushx(self, name: str, value): ...
    def lrange(self, name: str, start, end): ...
    def lrem(self, name: str, count, value): ...
    def lset(self, name: str, index, value): ...
    def ltrim(self, name: str, start, end): ...
    def rpop(self, name: str): ...
    def rpoplpush(self, src, dst): ...
    def rpush(self, name: str, *values): ...
    def rpushx(self, name: str, value): ...
    def sort(self, name: str, start: Optional[Any] = ..., num: Optional[Any] = ..., by: Optional[Any] = ..., get: Optional[Any] = ..., desc: bool = ..., alpha: bool = ..., store: Optional[Any] = ..., groups: bool = ...): ...
    def scan(self, cursor: int = ..., match: Optional[Any] = ..., count: Optional[Any] = ...): ...
    def scan_iter(self, match: Optional[Any] = ..., count: Optional[Any] = ...): ...
    def sscan(self, name: str, cursor: int = ..., match: Optional[Any] = ..., count: Optional[Any] = ...): ...
    def sscan_iter(self, name: str, match: Optional[Any] = ..., count: Optional[Any] = ...): ...
    def hscan(self, name: str, cursor: int = ..., match: Optional[Any] = ..., count: Optional[Any] = ...): ...
    def hscan_iter(self, name: str, match: Optional[Any] = ..., count: Optional[Any] = ...): ...
    def zscan(self, name: str, cursor: int = ..., match: Optional[Any] = ..., count: Optional[Any] = ..., score_cast_func: Any = ...): ...
    def zscan_iter(self, name: str, match: Optional[Any] = ..., count: Optional[Any] = ..., score_cast_func: Any = ...): ...
    def sadd(self, name: str, *values): ...
    def scard(self, name: str): ...
    def sdiff(self, keys, *args): ...
    def sdiffstore(self, dest, keys, *args): ...
    def sinter(self, keys, *args): ...
    def sinterstore(self, dest, keys, *args): ...
    def sismember(self, name: str, value): ...
    def smembers(self, name: str): ...
    def smove(self, src, dst, value): ...
    def spop(self, name: str): ...
    def srandmember(self, name: str, number: Optional[Any] = ...): ...
    def srem(self, name: str, *values): ...
    def sunion(self, keys, *args): ...
    def sunionstore(self, dest, keys, *args): ...
    def zadd(self, name: str, *args, **kwargs): ...
    def zcard(self, name: str): ...
    def zcount(self, name: str, min, max): ...
    def zincrby(self, name: str, value, amount: int = ...): ...
    def zinterstore(self, dest, keys, aggregate: Optional[Any] = ...): ...
    def zlexcount(self, name: str, min, max): ...
    def zrange(self, name: str, start, end, desc: bool = ..., withscores: bool = ..., score_cast_func: Any = ...): ...
    def zrangebylex(self, name: str, min, max, start: Optional[Any] = ..., num: Optional[Any] = ...): ...
    def zrevrangebylex(self, name: str, max, min, start: Optional[Any] = ..., num: Optional[Any] = ...): ...
    def zrangebyscore(self, name: str, min, max, start: Optional[Any] = ..., num: Optional[Any] = ..., withscores: bool = ..., score_cast_func: Any = ...): ...
    def zrank(self, name: str, value): ...
    def zrem(self, name: str, *values): ...
    def zremrangebylex(self, name: str, min, max): ...
    def zremrangebyrank(self, name: str, min, max): ...
    def zremrangebyscore(self, name: str, min, max): ...
    def zrevrange(self, name: str, start, end, withscores: bool = ..., score_cast_func: Any = ...): ...
    def zrevrangebyscore(self, name: str, max, min, start: Optional[Any] = ..., num: Optional[Any] = ..., withscores: bool = ..., score_cast_func: Any = ...): ...
    def zrevrank(self, name: str, value): ...
    def zscore(self, name: str, value): ...
    def zunionstore(self, dest, keys, aggregate: Optional[Any] = ...): ...
    def pfadd(self, name: str, *values): ...
    def pfcount(self, *sources): ...
    def pfmerge(self, dest, *sources): ...
    def hdel(self, name: str, *keys): ...
    def hexists(self, name: str, key): ...
    def hget(self, name: str, key): ...
    def hgetall(self, name: str): ...
    def hincrby(self, name: str, key, amount: int = ...): ...
    def hincrbyfloat(self, name: str, key, amount: float = ...): ...
    def hkeys(self, name: str): ...
    def hlen(self, name: str): ...
    def hset(self, name: str, key, value): ...
    def hsetnx(self, name: str, key, value): ...
    def hmset(self, name: str, mapping): ...
    def hmget(self, name: str, keys, *args): ...
    def hvals(self, name: str): ...
    def publish(self, channel, message): ...
    def eval(self, script, numkeys, *keys_and_args): ...
    def evalsha(self, sha, numkeys, *keys_and_args): ...
    def script_exists(self, *args): ...
    def script_flush(self): ...
    def script_kill(self): ...
    def script_load(self, script): ...
    def register_script(self, script): ...
