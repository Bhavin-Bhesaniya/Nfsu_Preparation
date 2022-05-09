
class Bca {
    public void subject() {
        System.out.println("Java,c++,python");
    }
}

class Sem1 extends Bca {
    public void subject() {
        System.out.println("Student 1 ask oop lanaguage : we say Java,c++,python");
    }
}

class Sem2 extends Bca {
    public void subject() {
        System.out.println("Student 2 ask oop lanaguage : we say Java,c++,python");
    }
}

public class O4Polymorphisam {

    public static void main(String[] args) {
        Bca firstobj = new Bca();
        Sem1 secondobj = new Sem1();
        Sem2 thirdobj = new Sem2();
        firstobj.subject();
        secondobj.subject();
        thirdobj.subject();
    }

}
