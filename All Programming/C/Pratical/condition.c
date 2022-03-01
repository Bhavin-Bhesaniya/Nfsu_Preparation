#include <stdio.h>
# include<ctype.h>
int main(){
    /*
    // Odd Even Number
    float Val1, _val2;
    printf("Enter Value1 and Value2 : ");
    scanf("%f %f",&Val1 , &_val2);
    
    // Type Casting
    int num1 = (int)Val1;
    
    
    if(num1%2 == 0){
        printf("No %d is Even", num1);
    }else{
        printf("No %d is Odd", num1);
    }

    // Odd Even Number Using Ternary Operators
    (num1 % 2 == 0) ? printf("No %d is Even", num1) : printf("No %d is Odd", num1);
    */ 

    /*
     Vowel Or Consonants 
     - A, E, I, O and U are called vowels
     - All other alphabets except these 5 vowels are called consonants.  
    */
    char c;
    int lowerVowel, upperVowel;
    printf("Enter Alphabets : ");
    scanf("%c", &c);

    lowerVowel = (c == 'a'|| c == 'e'||c == 'i'|| c == 'o'|| c == 'u');
    upperVowel = (c == 'A'|| c == 'E'|| c == 'I'|| c == 'O'|| c == 'U');

    
    if(lowerVowel || upperVowel){
        printf("Character %c is vowels", c);
    }else if(!isalpha(c)){
        printf("%c is Not Alphabet", c);  // For these we need #include<ctype.h> library
    }else{
        printf("Character %c is vowels", c);
    }



    return 0;
}