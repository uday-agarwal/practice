
import java.util.ArrayList;
import java.util.List;

import ds.ArrayListExample;

public class TopLevelCode {
  public void execute() {
    System.out.println("Inside: " + this.getClass().getName());

    ArrayListExample<String> example = ArrayListExample.getInstance(
        List.of("Hello world again!", "Goodbye"));
    ArrayList<String> values = example.getExample();
    for (String v : values) {
      System.out.println(v);
    }
  }
}
