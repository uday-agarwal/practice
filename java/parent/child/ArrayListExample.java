package parent.child;

import java.util.ArrayList;
import java.util.List;

public class ArrayListExample<T> {
  private ArrayList<T> myExample;

  private ArrayListExample(List<T> values) {
    myExample = new ArrayList<>(values);
  }

  public static ArrayListExample<String> getInstance(List<String> values) {
    ArrayListExample<String> instance = new ArrayListExample<String>(values);

    return instance;
  }

  public ArrayList<T> getExample() {
    return myExample;
  }
}