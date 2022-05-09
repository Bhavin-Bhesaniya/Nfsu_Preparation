/*
String Class :-
 - Sequence of characters treated as object in java which contain method that perform operation on string
 - String is immutabal, 
 - For modification to string use string buffer & string builder class
 
 Syntax :- String <string_variable> = "<sequence_of_string>";
           String str = new String("Value");      //Dynamically Allocated
 
 Package :- import java.io.*;
            import java.lang.*;


 Memory allocation of String :-
  - Whenever String Object is created as literal object created in String constant pool
  - It allow JVM to optimize initialization of String literal
  - In case of String are dynamically allocated they are assigned new memory location in heap
  - String will not be added to String constant pool(str.intern(); //store in constant pool)

 
  Note :- 
  - All objects in Java are stored in a heap
  - Reference variable is the object stored in stack area or they can be contained in other objects which puts them 
    in heap area also


 Methods :-                          Description	                                                      Return Type
  length()	            Number of characters in the string		                                          int
  charAt(int)           Character at the specified index (position)	                                    char
  substring(int,int)	  Return the substring from the ith  index character to end                       string
  concat()	            Appends a string to the end of another string	                                  string
  indexOf()	            Returns the position of the first found in string	                              int
  lastIndexOf()	        Returns the position of the last found in string	                              int
  equals()	            Compares two strings	                                                          boolean
  equalsIgnoreCase()	  Compares two strings                                                            boolean
  compareTo()	          Compares two strings lexicographically	                                        int
  compareToIgnoreCase()	Compares two strings lexicographically, ignoring case differences	              int
  toLowerCase()	        Converts a string to lower case letters	                                        String
  toUpperCase()	        Converts a string to upper case letters	                                        String
  trim()	              Removes whitespace from both ends of a string	                                  String
  replace()	            returns a new string where the specified values are replaced	                  String
  codePointAt()       	Returns the Unicode of the character at the specified index	                    int         
  codePointBefore()	    Returns the Unicode of the character before the specified index	                int
  codePointCount()	    Returns the Unicode in the specified text range of this String	                int
  subSequence()	        Returns a new character sequence that is a subsequence of this sequence	        CharSequence
  contains()	          Checks string contains a sequence of characters	                                boolean
  contentEquals()	      Checks CharSequence exactly matches the String                         	        boolean
  endsWith()	          Checks whether a string ends with the specified character(s)	                  boolean
  startsWith()	        Checks whether a string starts with specified characters	                      boolean
  getChars()	          Copies characters from a string to an array of chars	                          void
  toCharArray()	        Converts this string to a new character array	                                  char[]
  hashCode()	          Returns the hash code of a string	                                              int
  intern()	            Returns the canonical representation for the string object	                    String
  isEmpty()	            Checks whether a string is empty or not	                                        boolean
  format()	            Returns formatted string using the specified locale,, and arguments	            String
  matches()	            match String against a regular expression, and returns the matches	            boolean
  split()	              Splits a string into an array of substrings	                                    String[]
  replaceAll()	        Replaces each substring of this string that matches the                         String
  replaceFirst()	      Replaces the first occurrence of a substring that matches 	                    String
  copyValueOf()	        Returns a String that represents the characters of the character array	        String
  getBytes()	          Encode String into a sequence of bytes using the named charset, storing the 
                        result into a new byte array	                                                  byte[]
  regionMatches()	      Tests if two string regions are equal	                                          boolean
  toString()	          Returns the value of a String object	                                          String
  valueOf()	            Returns the string representation of the specified value	                      String


 Interface and Class in String :-
  CharBuffer :-
   - Holds sequence of integer values used in I/O operation
   - getmethod() read single chars / putmethod() write single chars

   Short buffers created by :-
    allocate() : Allocate space for buffer’s content
    wrap()     : Wrap existing long array into buffer


  StringBuffer :-
   - Represent growable and writeable character sequence
   - java.lang.StringBuffer extends (or inherits from) Object class 
   - All Implemented Interfaces of StringBuffer class :- Serializable, Appendable, CharSequence
   - Safe for use by multiple thread

   Constructor :-
    StringBuffer() :- Reserve room for 16 character without reallocation
    StringBuffer() :- Accept integer argument that explicitly set size of the buffer
    StringBuffer() :- Accept String argument that sets initial contents of StringBuffer object 
                      and reserves room for 16 more characters without reallocation

   Method :-
    capacity()  |  insert()  |  reverse()  |  delete()  |  deletCharAt()      
    ensureCapacity()    - Increase string capacity
    appendCodePoint     - appends the string representation of the codePoint argument     
    offsetByCodePoint() - Return index within this sequence that offset from given index by codePointOffset code point


  String Builder :-
   - Represent mutable sequence of character
   - Use drop-in replacement for StringBuffer in places where StringBuffer was being used by single thread
   - Faster in most of implementations
   - If synchronization required then its recommended that StringBuffer used

   Syntax :- public final class StringBuilder extends Object implements Serializable, CharSequence

   Construtor :-
    StringBuilder() :- With no characters in it and initial capacity of 16 characters
    StringBuilder() :- Initial capacity specified by capacity argument
    
   Method :-
    append            Join new charater in old string                                      
    appendCodePoint   Append string representation of codePoint argument          
    capacity          Return current capacity of string                           


  StringTokenizer :- 
   - Used to break string into tokens
   - Maintain current position within string to be tokenized
   - Token returned by taking substring of string that was used to create StringTokenizer object

   Construtor :-
    StringTokenizer() 
    StringTokenizer() :- Delim is set of delimiters that used to tokenize given string
    StringTokenizer() :- True considerd token, false serve to separate token


  StringJoiner :-
   - Used to construct sequence of characters(strings) separated by delimiter and optionally starting with 
     supplied prefix and ending with supplied suffix
   - prefix - Sequence of character used at beginning
   - suffix - Sequence of character used at the end  
     Throws :-  NullPointerException - if prefix, delimiter, or suffix is null    
*/

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