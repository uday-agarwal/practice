package com.practice.designpatterns.command;

// A one-stop command that can execute many commands inside.
public class MacroCommand implements Command {
  private Command[] commands;

  public MacroCommand(Command[] commands) {
    this.commands = commands;
  }

  @Override
  public void execute() {
    for (var command : commands) {
      command.execute();
    }
  }

  @Override
  public void undo() {
    for (var command : commands) {
      command.undo();
    }
  }

}
