package com.practice.designpatterns.singleton;

public class SingletonWithDoubleCheckedLocking {
  // Lazy initialization.
  // Uses a volatile to ensure the compiler or JVM don't optimize this variable
  // and changes to it are quickly visible to other threads.
  private static volatile SingletonWithDoubleCheckedLocking instance;

  private SingletonWithDoubleCheckedLocking() {
  }

  // Double checked locking idiom.
  // Uses a local variable to access the volatile only once if the initialization
  // is already done.
  // Attempt to see if the initialization is already done.
  // If not, try to acquire lock.
  // If acquired lock, see if init is done.
  // If not, initialize.
  // Release lock.
  public static SingletonWithDoubleCheckedLocking getInstance() {
    SingletonWithDoubleCheckedLocking localInstance = instance;

    if (localInstance == null) {
      synchronized (SingletonWithDoubleCheckedLocking.class) {
        localInstance = instance;
        if (localInstance == null) {
          localInstance = instance = new SingletonWithDoubleCheckedLocking();
        }
      }
    }
    return localInstance;
  }
}
