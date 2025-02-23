package com.practice.designpatterns.singleton;

// Enum based singleton.
// Main disadvantage is the eager initialization of enums when class is loaded.
// So lazy initialization is not possible, which means this can consume more
// resources than necessary.
public enum SingletonEnum {
  SINGLE_INSTANCE;

  private String property;

  private SingletonEnum() {
    property = "This is an Enum Singleton";
  }

  public String getProperty() {
    return property;
  }
}
