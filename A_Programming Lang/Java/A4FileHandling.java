import java.io.File; //import file class 
import java.io.IOException;
// import java.io.FileInputStream;
// import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.FileWriter;
// import java.io.FileWriter; // write in the file
import java.io.FileNotFoundException; //handle error if file not found
import java.util.Scanner; //read text files

public class A4FileHandling {
    public static void main(String[] args) {

        // createfile
        try {
            // File firstObj = new File("firstfile.txt"); //create file
            File firstObj = new File("D:\\firstfile.txt"); // specific directory file created
            if (firstObj.createNewFile()) { // createnewfile method have boolean if created true otherwise false
                System.out.println("File created: " + firstObj.getName());// getname method use to print filename
            } else {
                System.out.println("Files already exists");
            }
        } catch (IOException e) {
            System.out.println("an error occurred");
            e.printStackTrace();
        }

        // writing file
        try {
            FileWriter writeinfile = new FileWriter("firstfile.txt");
            writeinfile.write("I started first time writing");
            writeinfile.close();
            System.out.println("Successfully write");
        } catch (IOException e) {
            System.out.println("an error occurred");
            e.printStackTrace();
        }

        // reading file
        try {
            File readfile = new File("firstfile.txt");
            Scanner myread = new Scanner(readfile);
            while (myread.hasNextLine()) {
                String data = myread.nextLine();
                System.out.println(data);
            }
            myread.close();
        } catch (FileNotFoundException e) {
            System.out.println("filenot found");
            e.printStackTrace();
        }

        // get file info
        File firstObj = new File("firstfile.txt");
        if (firstObj.exists()) {
            System.out.println("File Name : " + firstObj.getName());
            System.out.println("File Path : " + firstObj.getAbsolutePath());
            System.out.println("Writeable : " + firstObj.canWrite());
            System.out.println("Readable  : " + firstObj.canRead());
            System.out.println("File size in bytes : " + firstObj.length());
        } else {
            System.out.println("file not found");
        }

        // list of file in directory
        try {
            File listFile = new File("D:\\");
            String[] paths = listFile.list();
            for (String path : paths) {
                System.out.println(path);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }

        // create directory
        File dir = new File("D:\\FirstDir");
        if (dir.mkdir()) {
            System.out.println("directory is created");
        } else {
            System.out.println("Cannot be created");
        }

        // delete file or delete directory
        File delObj = new File("D:\\FirstDir"); // firstfile.txt
        if (delObj.delete()) {
            System.out.println("delete the file: " + delObj.getName());
        } else {
            System.out.println("failed to delete");
        }

        // Copy file
        try {
            // Byte Stream
            // FileInputStream in = new FileInputStream("./firstfile.txt");
            // FileOutputStream out = new FileOutputStream("./secondfile.txt");
            // Character Stream
            FileReader in = new FileReader("./firstfile.txt");
            FileWriter out = new FileWriter("output.txt");

            int c;
            while ((c = in.read()) != -1) {
                out.write(c);
            }
            System.out.println("Done Copy File");
            in.close();
            out.close();

        } catch (Exception e) {
            System.out.println(e);
        }

    }
}
