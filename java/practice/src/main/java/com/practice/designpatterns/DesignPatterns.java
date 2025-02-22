package com.practice.designpatterns;

import com.practice.designpatterns.factory.AveragePluginFactory;
import com.practice.designpatterns.factory.GreatPluginFactory;
import com.practice.designpatterns.factory.Plugin;
import com.practice.designpatterns.factory.PluginFactory;
import com.practice.designpatterns.factory.PluginType;
import com.practice.designpatterns.singleton.SingletonSingleThreaded;
import com.practice.designpatterns.singleton.SingletonWithDoubleCheckedLocking;
import com.practice.designpatterns.singleton.SingletonWithSynchronized;

public class DesignPatterns {
  public static void testDesignPatterns() {
    testSingletons();
    testFactory(new AveragePluginFactory(), PluginType.NEW_PLUGIN);
    testFactory(new GreatPluginFactory(), PluginType.NEW_PLUGIN);
  }

  private static void testSingletons() {
    SingletonSingleThreaded singleton = SingletonSingleThreaded.getSingleton();
    System.out.println("Singleton hashcode: " + singleton.hashCode());

    SingletonWithSynchronized synchronizedSingleton = SingletonWithSynchronized.getInstance();
    System.out.println("Synchronized Singleton hashcode: " + synchronizedSingleton.hashCode());

    SingletonWithDoubleCheckedLocking dclSingleton = SingletonWithDoubleCheckedLocking.getInstance();
    System.out.println("DCL singleton hashcode: " + dclSingleton.hashCode());
  }

  private static void testFactory(PluginFactory factory, PluginType type) {
    System.out.println("Testing factory method pattern.");
    Plugin plugin = factory.createPlugin(type);
    plugin.play();
    plugin.stream();
  }
}
