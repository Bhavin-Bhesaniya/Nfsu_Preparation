class FullName {
    protected String name = "Bhavin";

    public void FName() {
        System.out.println("Bhesaniya");
    }
}

class Details extends FullName {
    private int age = 21;

    public static void main(String[] args) {
        Details myobj = new Details();
        myobj.FName();
        System.out.println(myobj.name + " " + myobj.age);
    }

}
