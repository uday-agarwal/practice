package com.practice.designpatterns.singleton;

import java.util.Objects;

// Private static instance of the same class.
// Public static get method.
// Private constructor.
// Works for single threaded application.
public class SingletonSingleThreaded {
  // Lazy initialization.
  private static SingletonSingleThreaded instance;

  private SingletonSingleThreaded() {
  }

  // Works only for a single thread.
  public static SingletonSingleThreaded getSingleton() {
    if (Objects.isNull(instance)) {
      instance = new SingletonSingleThreaded();
    }

    return instance;
  }
}
