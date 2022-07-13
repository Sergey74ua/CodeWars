// Find the smallest integer in the array

public class SmallestIntegerFinder {
  public static int findSmallestInt(int[] args) {
    int m = args[0];
    for (int i = 0; i < args.length; i++) {
       if (args[i] < m)
        m = args[i];
    }
    return m;
  }
}

// Лучшее решение
/*
public class SmallestIntegerFinder {
    public static int findSmallestInt(int[] args) {
        return java.util.Arrays.stream(args).min().getAsInt();
    }
}
*/