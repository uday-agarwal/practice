package com.practice;

import com.github.benmanes.caffeine.cache.*;

public class Cache<K, V> {
  private LoadingCache<K, V> loadingCache;

  private Cache() {
  }

  public static Cache getCache(K key, V value) {
    if (loadingCache == null) {
      loadingCache = new LoadingCache<K, V>() {

      };
    }
  }
}
