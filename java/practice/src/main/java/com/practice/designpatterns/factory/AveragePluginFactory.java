package com.practice.designpatterns.factory;

public class AveragePluginFactory implements PluginFactory {
  public Plugin createPlugin(PluginType type) {
    // I just return the old plugin since this is all I know.
    return new OldPlugin();
  }
}
