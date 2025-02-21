package com.practice.designpatterns.factory;

public class OldPlugin implements Plugin {
  public void play() {
    System.out.println("Playing using the old plugin!");
  }

  public void stream() {
    System.out.println("Streaming using the old plugin!");
  }
}
