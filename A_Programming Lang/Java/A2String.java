
import java.nio.CharBuffer;
import java.util.*;

class A2String {
  public static void main(String[] args) {

    // CharBuffer Example
    int capacity = 4; // Declaring capacity of CharBuffer

    try {
      CharBuffer charbuffer = CharBuffer.allocate(capacity); // Allocating size capacity
      charbuffer.append('a').append('b').rewind();      // Append value in CharBuffer
      System.out.println("Original CharBuffer: " + Arrays.toString(charbuffer.array())); 
    }
    catch (Exception e) {
      System.out.println("Exception throws : " + e);
    }


    // StringBuffer Example :-
    StringBuffer buffer = new StringBuffer();
    System.out.println(buffer.capacity());

    StringBuffer strBuffer = new StringBuffer("Bhavin Bhesaniya");
    System.out.println(strBuffer.capacity() + " " + strBuffer.length());


    // StringBuilder 
    try {
      StringBuilder sb = new StringBuilder(); // Default Constructor
      sb.append("Bhavin");
      System.out.println(sb.toString());

      StringBuilder sb2 = new StringBuilder("CharSequence Constructor"); 
      System.out.println(sb2.toString());

      StringBuilder sb3 = new StringBuilder(sb.toString()); // String pass in construtor
      boolean checkStr = sb3.equals(sb);
      System.out.println(checkStr);

    } catch (Exception e) {
      System.out.println(e);
    }

    // StringTokenizer
    try {
      StringTokenizer st1 = new StringTokenizer("Hello Geeks How are you", " ");
      // StringTokenizer st1 = new StringTokenizer("Hello : Geeks : How are you", " :");
      // StringTokenizer st1 = new StringTokenizer("Hello : Geeks : How are you", " :", true);
      while (st1.hasMoreTokens())
        System.out.println(st1.nextToken()); // Without loop print first hello token only
    } catch (Exception e) {
      System.out.println(e);
    }


    // StringJoiner
    ArrayList<String> al = new ArrayList<>();
    al.add("Ram");
    al.add("Shyam");

    StringJoiner sj1 = new StringJoiner(",");
    sj1.setEmptyValue("sj1 is empty");
    System.out.println(sj1);
    sj1.add(al.get(0)).add(al.get(1));
    System.out.println(sj1);
    System.out.println("Length of sj1 : " + sj1.length());

  }
}