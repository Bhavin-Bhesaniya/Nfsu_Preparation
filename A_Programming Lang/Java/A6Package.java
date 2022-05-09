import java.util.Scanner;

public class A6Package {
    public static void main(String[] args) {
        Scanner obj = new Scanner(System.in);
        System.out.println("ENTER USERNAME : ");
        String username = obj.nextLine();
        System.out.println("User Name is : " + username);
        obj.close();
    }
}
