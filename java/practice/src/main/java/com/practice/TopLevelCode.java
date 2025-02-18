package com.practice;

import java.util.List;

import com.practice.ds.ArrayListExample;

public class TopLevelCode {
  public void execute() {
    System.out.println("Inside: " + this.getClass().getName());

    ArrayListExample<String> example = ArrayListExample.getInstance(
        List.of("Hello world again!", "Goodbye"));
    System.out.println(example.getClass());
  }
}
