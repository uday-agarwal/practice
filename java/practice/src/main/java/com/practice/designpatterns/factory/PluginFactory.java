package com.practice.designpatterns.factory;

// XFactory class for X abstract class / interface.
// Returns X.
// The implementation selected can depend on an input to the getInstance method.
public interface PluginFactory {
  public Plugin createPlugin(PluginType type);
}
