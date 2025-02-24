package com.practice.designpatterns.command;

// Generic interface for each command.
public interface Command {
  public void execute();

  public void undo();
}
