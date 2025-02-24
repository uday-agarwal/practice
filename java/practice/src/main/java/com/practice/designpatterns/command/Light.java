package com.practice.designpatterns.command;

public class Light {
  private enum STATE {
    OFF,
    ON,
  }

  private STATE state;

  public void turnOn() {
    state = STATE.ON;
    System.out.println("Light turned on.");
  }

  public void turnOff() {
    state = STATE.OFF;
    System.out.println("Light turned off.");
  }

  public STATE getState() {
    return state;
  }
}
