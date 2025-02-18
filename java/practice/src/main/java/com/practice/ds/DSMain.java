package com.practice.ds;

import java.util.List;

public class DSMain {
  public static void execute() {
    // Arrays
    // ArrayExample.execute();

    // ArrayList
    System.out.println("Array list");
    ArrayListExample<String> students = ArrayListExample.getInstance(List.of());
    students.insert("Uday");
    students.insert("Anand");
    students.operate();

    // Linked List
    System.out.println("Linked list");
    LinkedListExample<String> linkedList = new LinkedListExample<>();
    linkedList.add("Test");
    linkedList.add("My");
    linkedList.add("Strength");
    linkedList.operate();
  }
}
