import java.util.*;

public class A3Array {
    // Array of objects class for testing
    static class Student {
        public int roll_no;
        public String name;

        Student(int roll_no, String name) {
            this.roll_no = roll_no;
            this.name = name;
        }
    }

    public static void main(String[] args) {

        System.out.println("Print One-Dimensional Array with user input :-  ");
        Scanner userInputInsert = new Scanner(System.in);
        System.out.print("Enter no of input you need to add : ");

        int[] arrayVar = new int[10]; // Declare Array

        int NoOfInput;
        NoOfInput = userInputInsert.nextInt();

        for (int i = 0; i < NoOfInput; i++) {
            arrayVar[i] = userInputInsert.nextInt();
        }
        System.out.println("Print Array after user input :-  ");
        for (int i = 0; i < NoOfInput; i++) {
            System.out.println(arrayVar[i]);
        }
        userInputInsert.close();
        
        

        System.out.println("Array Of Object/ declare class and access his method :-");
        Student[] arrayOfObj = new Student[2];
        arrayOfObj[0] = new Student(12, "Bhavin");


        System.out.println("Multi-Dimensional Array / Jagged Array :- ");
        int[][] myNum = { {2,7,9},{3,6,1},{7,4,2}};
        for (int i = 0; i < myNum.length; ++i) {
            for (int j = 0; j < myNum[i].length; ++j) {
                System.out.print(myNum[i][j] + " ");
            }
            System.out.println();
        }
        System.out.println("Print Single value from multidimensional array : "+ myNum[0][2]);

        System.out.println("Passing Array to method :- ");
        int[] sumVar = {3,4,5,6,7,8,9,10,11};
        sum(sumVar);

        System.out.println("Return Array from method :- ");
        int[] retrunSum = m1();
        System.out.println("Return Array length : " + retrunSum.length );
        
        System.out.println("Class Object of arrays :- ");
        int intArray[] = new int[3];
        System.out.println(intArray.getClass() + " Diffrence : " + intArray.getClass().getSuperclass());
        

        System.out.println("Cloneing Array Methods :- ");
        int intArrays[] = {1,2,3};          
        int cloneArray[] = intArrays.clone();
        // will print false as deep copy is created for one-dimensional array
        System.out.println(intArrays == cloneArray);// in multidimensional [0][1] added after intArrays
        for (int i = 0; i < cloneArray.length; i++) {
            System.out.print(cloneArray[i]+" ");
        }
        System.out.println();


        System.out.println("Jagged array in java :-");
        int r = 5;
        int arr[][] = new int[r][]; // Declaring 2-D array with 5 rows
 

        // Creating 2D array such that first row has 1 element, second row has two element
        for (int i = 0; i < arr.length; i++)
            arr[i] = new int[i + 1];
 
        // Initializing array
        int count = 0;
        for (int i = 0; i < arr.length; i++)
            for (int j = 0; j < arr[i].length; j++)
                arr[i][j] = count++;
 
        // Displaying the values of 2D Jagged array
        System.out.println("Contents of 2D Jagged Array");
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[i].length; j++)
                System.out.print(arr[i][j] + " ");
            System.out.println();
        }
    }

    public static void sum(int[] sumVar) {
        int sum = 0;
        for (int i = 0; i < sumVar.length;i++) {
            sum = sum + sumVar[i];
        }
        System.out.println("Total sum is :" + sum);    
    }
    
    public static int[] m1() 
    {
        // returning  array
        return new int[]{1,2,3};
    }

}
