package com.practice.ds;

import java.util.LinkedList;

public class LinkedListExample<T> {
  private LinkedList<T> data;

  public LinkedListExample() {
    data = new LinkedList<>();
  }

  public LinkedListExample(LinkedList<T> data) {
    this.data = data;
  }

  public void add(T value) {
    data.add(value);
  }

  public void operate() {
    System.out.println(data);
  }
}
