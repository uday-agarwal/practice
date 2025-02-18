package com.practice;

import com.practice.ds.DSMain;

public class Main {
  public static void main(String[] args) {
    System.out.println("Hello world");

    // Top level for general testing
    // TopLevelCode tlc = new TopLevelCode();
    // tlc.execute();

    // Record
    Record point = new Record(5, 7);
    System.out.println(point);

    // DS logic
    DSMain.execute();

  }
}