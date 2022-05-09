class RunnableY implements Runnable {
    // @Override run method
    public void run() {
        try {
            while (true) {
                Thread.sleep(1000);
                System.out.println("Thread with runnable interface implements");
            }
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}

class ThreadX extends Thread {
    // Override run method
    public void run() {
        try {
            int i = 5;
            while (i > 0) // while (true) Condition true so infinte time print
            {
                Thread.sleep(3000);
                System.out.println("Hello This is first thread program");
                i--;
                /*
                 * Excercise - 2 Question
                 * int max = 10,min = 5;
                 * int range = max - min + 1;
                 * int rand = (int)(Math.random() * range) + min;
                 * System.out.println(rand);
                 */

            }
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}

class T1Thread {
    public static void main(String[] args) {
        ThreadX tx = new ThreadX(); // Create threadx class object
        tx.start();                 // start thrad

        RunnableY runnable = new RunnableY(); // Create runnable object
        Thread tx1 = new Thread(runnable); // Pass runnable object to thread constructor
        tx1.start();
    }
}
