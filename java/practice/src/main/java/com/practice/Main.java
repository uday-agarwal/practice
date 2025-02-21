package com.practice;

import com.practice.designpatterns.DesignPatterns;
import com.practice.designpatterns.singleton.SingletonSingleThreaded;
import com.practice.ds.DSMain;

public class Main {
  private static void cacheTest() {
    CacheExample cacheExample = CacheExample.getCacheExample();
    cacheExample.insert("Peter", "Pan");
    cacheExample.insert("Paul", "Pale");
    cacheExample.insert("Parker", "Paper");
    cacheExample.insert("Panther", "Proper");
    cacheExample.insert("Pulitzer", "Prosper");
    cacheExample.invalidate("Paul");
    System.out.println(cacheExample);

    // Singleton instance - we get the same instance back.
    CacheExample anotherExample = CacheExample.getCacheExample();
    System.out.println(anotherExample);
  }

  public static void main(String[] args) {
    System.out.println("Hello world");

    // Top level for general testing
    // TopLevelCode tlc = new TopLevelCode();
    // tlc.execute();

    // Record
    // Record point = new Record(5, 7);
    // System.out.println(point);

    // Cache
    // cacheTest();

    // Design Patterns
    DesignPatterns.testDesignPatterns();

    // DS logic
    // DSMain.execute();

  }
}