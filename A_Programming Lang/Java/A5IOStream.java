import java.io.*;

public class A5IOStream {
    
    public static void main(String[] args) throws IOException {
    
    
        //Character StreamRead 
        FileReader sourceStream = null;
        try {
            sourceStream = new FileReader("./rem.txt");
            // Reading sourcefile and writing content to target file character by character
            int temp;
            while ((temp = sourceStream.read()) != -1)
                System.out.print((char) temp);
        }
        finally {
            if (sourceStream != null)
                sourceStream.close();   // Closing stream as no longer in use
        }

        // Byte Stream
        FileInputStream sourceStream1 = null;
        FileOutputStream targetStream = null;
        try 
        {
            sourceStream1 = new FileInputStream("./rem.txt");
            targetStream = new FileOutputStream ("TestingStream.txt");
            // Reading source file and writing content to target file byte by byte
            int temp;
            while ((temp = sourceStream1.read()) != -1)
                targetStream.write((byte)temp);            
        }
        finally 
        {
            if (sourceStream1 != null)
                sourceStream1.close();            
            if (targetStream != null)            
                targetStream.close();            
        }
    }
}
