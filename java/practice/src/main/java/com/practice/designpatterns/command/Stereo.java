package com.practice.designpatterns.command;

public class Stereo {
  private int volume;
  private String cd;
  private boolean state;

  public void turnOn() {
    System.out.println("Stereo turned on :)");
    state = true;
  }

  public void turnOff() {
    System.out.println("Stereo turned off :(");
    state = false;
    cd = "";
    volume = 0;
  }

  public void insertCd(String cd) {
    System.out.println("CD inserted: " + cd);
    this.cd = cd;
  }

  public void setVolume(int volume) {
    System.out.println("Volume set to " + volume);
    this.volume = volume;
  }
}
