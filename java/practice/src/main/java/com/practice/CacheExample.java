package com.practice;

import java.time.Duration;
import java.util.Objects;

import com.github.benmanes.caffeine.cache.Caffeine;
import com.github.benmanes.caffeine.cache.LoadingCache;

/**
 * Also used as an example of Singleton class.
 */
public class CacheExample {
  // Singleton - define a single private static instance.
  private static CacheExample instance;
  private final LoadingCache<String, String> loadingCache;

  private CacheExample() {
    loadingCache = Caffeine.newBuilder()
        .maximumSize(2)
        .expireAfterWrite(Duration.ofMinutes(5))
        .refreshAfterWrite(Duration.ofMinutes(1))
        .build(key -> key + 2);
  }

  public static CacheExample getCacheExample() {
    if (Objects.isNull(instance)) {
      instance = new CacheExample();
    }
    return instance;
  }

  public void insert(String key, String value) {
    loadingCache.put(key, value);
  }

  public void invalidate(String key) {
    loadingCache.invalidate(key);
  }

  @Override
  public String toString() {
    StringBuilder stringBuilder = new StringBuilder();

    for (var entry : loadingCache.asMap().entrySet()) {
      stringBuilder.append(entry.getKey() + ":" + entry.getValue() + "\n");
    }
    return stringBuilder.toString();
  }
}
