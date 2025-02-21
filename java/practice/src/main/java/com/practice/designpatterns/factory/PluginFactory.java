package com.practice.designpatterns.factory;

// XFactory class for X abstract class / interface.
// Returns X.
// The implementation selected can depend on an input to the getInstance method.
public class PluginFactory {
  public static Plugin getPlugin() {
    return new NewPlugin();
  }
}
