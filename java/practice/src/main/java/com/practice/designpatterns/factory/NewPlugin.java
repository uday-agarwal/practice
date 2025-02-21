package com.practice.designpatterns.factory;

public class NewPlugin implements Plugin {
  public void play() {
    System.out.println("Playing using the new plugin!");
  }

  public void stream() {
    System.out.println("Streaming using the new plugin!");
  }
}
