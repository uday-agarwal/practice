package ds;

public class ArrayExample {
  public static void execute() {
    System.out.println("Inside: " + ArrayExample.class.getName());
    // System.out.println(ArrayExample.class.getSimpleName());

    final int[] test = { 12, 13, 14 };

    System.out.println("test");
    for (var i : test) {
      System.out.println(i);
    }

    // Internals can change by a copied reference, even for final variables.
    int[] another = test;
    another[2] = 4;
    System.out.println("another");
    for (var i : another) {
      System.out.println(i);
    }
    System.out.println("test");
    for (var i : test) {
      System.out.println(i);
    }
  }
}
