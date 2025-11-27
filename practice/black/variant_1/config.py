import os

# Настройки Redis
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
REDIS_DB = int(os.getenv("REDIS_DB", 0))

# TTL для кеша (в секундах)
CACHE_TTL = int(os.getenv("CACHE_TTL", 300))  # 5 минут по умолчанию

