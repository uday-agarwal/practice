package com.practice.designpatterns.command;

public class StereoOnCommand implements Command {
  private Stereo stereo;

  public StereoOnCommand(Stereo stereo) {
    this.stereo = stereo;
  }

  @Override
  public void execute() {
    stereo.turnOn();
    stereo.insertCd("Backstreet Boys");
    stereo.setVolume(10);
  }

  @Override
  public void undo() {
    stereo.turnOff();
  }

}
