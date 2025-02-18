package com.practice;

public record Record(int x, int y) {
  // hashCode, toString, and equals methods are already provided.
  // Can override them if needed, but don't have to.

  @Override
  public String toString() {
    return String.format("%d, %d", x, y);
  }
}
