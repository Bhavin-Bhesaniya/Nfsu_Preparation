#include <stdio.h> // Tells compiler to include contents of stdio.h (standard input and output) file
int main()
{
    // My Comment

    int age;
    printf("Enter Your Age : "); // library function to send formatted output to the screen
    scanf("%d", &age);
    printf("Your Age : %d\nSize Of int : %zu", age, sizeof(age));

    /*
    float num1, num2, addition;
    printf("\nEnter Number1 and Number2 : ");
    scanf("%f\n %f", &num1, &num2);
    addition = num1 + num2;
    printf("Your addition : %.2f\n", addition); // Result rounded off to second decimal place using %.2lf conversion character


    char c;
    printf("Enter Character: ");
    scanf("%c", &c);
    printf("ASCII value of %c = %d", c, c);
    printf("\nSize Of Character : %zu ", sizeof(c));
    */
    int swap1, swap2, temp;
    printf("\nEnter Swap Value 1 and Swap Value 2 : ");
    scanf("%d\n %d", &swap1, &swap2);
    printf("Befor Swap Value : %d  %d", swap1, swap2);
    temp = swap1;
    swap1 = swap2;
    swap2 = temp;
    printf("\nAfter Swap Value : %d  %d", swap1, swap2);

    swap1 = swap1 - swap2;
    swap2 = swap1 + swap2;
    swap1 = swap2 - swap1;

    printf("\nAfter Swap Value : %d  %d", swap1, swap2);

    return 0; //  "Exit status" program ends with this statement
}