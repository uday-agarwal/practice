package com.practice.designpatterns.singleton;

public class SingletonWIthEagerInitialization {
  // Init at class load time in JVM.
  // Happens before any threads can access it.
  // So is thread safe.
  private static SingletonWIthEagerInitialization instance = new SingletonWIthEagerInitialization();

  private SingletonWIthEagerInitialization() {
  }

  public static SingletonWIthEagerInitialization getInstance() {
    return instance;
  }
}
