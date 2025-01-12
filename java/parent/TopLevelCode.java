package parent;

import java.util.ArrayList;
import java.util.List;
import parent.child.ArrayListExample;

public class TopLevelCode {
  public void execute() {
    ArrayListExample<String> example = ArrayListExample.getInstance(
        List.of("Hello world again!", "Goodbye"));
    ArrayList<String> values = example.getExample();
    for (String v : values) {
      System.out.println(v);
    }
  }
}
