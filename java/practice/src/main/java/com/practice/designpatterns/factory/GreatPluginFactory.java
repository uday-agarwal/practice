package com.practice.designpatterns.factory;

public class GreatPluginFactory implements PluginFactory {
  public Plugin createPlugin(PluginType type) {
    switch (type) {
      case OLD_PLUGIN:
        return new OldPlugin();
      case NEW_PLUGIN:
        return new NewPlugin();
      default:
        throw new UnsupportedOperationException("Unsupported plugin type chosen.");
    }
  }
}
