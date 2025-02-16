package ds;

import java.util.ArrayList;
import java.util.List;

public class ArrayListExample<T> {
  private ArrayList<T> students;

  private ArrayListExample(List<T> values) {
    students = new ArrayList<>(values);
  }

  public static ArrayListExample<String> getInstance(List<String> values) {
    ArrayListExample<String> instance = new ArrayListExample<String>(values);

    return instance;
  }

  public boolean insert(T value) {
    students.add(value);
    students.add(1, value); // adds at specific location
    return true;
  }

  @Override
  public String toString() {
    StringBuilder output = new StringBuilder();
    for (var name : students) {
      output.append(name);
    }
    return output.toString();
  }

  public void operate() {
    System.out.println(students);
    System.out.println("Size: " + students.size());
    System.out.println("toString: " + toString());
    System.out.println("At index 1: " + students.get(1));
  }
}