package com.practice.designpatterns.singleton;

public class SingletonWithSynchronized {
  // Lazy initialization.
  private static SingletonWithSynchronized instance;

  private SingletonWithSynchronized() {
  }

  // Synchronized idiom.
  // Works for concurrent threads too - with the synchronized keyword.
  // But affects concurrency - synchronizing a method is quite expensive.
  // Acquires a lock every time we need the instance, even after initialization.
  // Whereas we need the lock only at initialization time.
  public static synchronized SingletonWithSynchronized getInstance() {
    if (instance == null) {
      instance = new SingletonWithSynchronized();
    }
    return instance;
  }
}
