import hashlib
from typing import Optional, Any

class CacheManager:
    """轻量级内存缓存 (生产环境可无缝替换底层字典为 Redis 客户端)"""
    def __init__(self):
        self._store = {}

    def generate_key(self, content: bytes, extra: str) -> str:
        combined = content + extra.encode('utf-8')
        return hashlib.md5(combined).hexdigest()

    def get(self, key: str) -> Optional[Any]:
        return self._store.get(key)

    def set(self, key: str, value: Any):
        self._store[key] = value