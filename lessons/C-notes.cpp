/*   TYPES

1.	bool

      Stores either value true or false.

2.	char

      Typically a single octet (one byte). This is an integer type.

3.	int

      The most natural size of integer for the machine.

4.	float

      A  single-precision floating point value.

5.	double

      A double-precision floating point value.

6.	void

      Represents the absence of type.

7.	wchar_t

      A wide character type.

8. string

      Stores text, such as "Hello World". String values are surrounded by double quotes
           txt.size(); txt.length(); txt.append(txt2),  access:   myString[0];
           The <string> library also has an at():
               myString.at(0) = 'J';         Hello -> Jello
          string greeting1 = "Hello";  // Regular String
          char greeting2[] = "Hello";  // C-Style String (an array of characters)

    printf("Medium level");  ----- alternative echo for cout;  
C++ also allows to define various other types of variables, which we will cover in subsequent chapters like Enumeration, Pointer, Array, Reference, Data structures, and Classes.

# Length of types
boolean	1 byte	Stores true or false values
char	1 byte	Stores a single character/letter/number, or ASCII values
int	2 or 4 bytes	Stores whole numbers, without decimals
float	4 bytes	Stores fractional numbers, containing one or more decimals. Sufficient for storing 6-7 decimal digits
double	8 bytes	Stores fractional numbers, containing one or more decimals. Sufficient for storing 15 decimal digits
string  

Size of char : 1
Size of int : 4
Size of float : 4
Size of wchar_t : 4
Size of double : 8

Size of short int : 2
Size of long int : 4

# Define

int    i, j, k;
char   c, ch;
float  f, salary;
double d;

extern int a, b;
extern int c;
extern float f;

// function declaration
int func();
int main() {
   // function call
   int i = func();
}

// function definition
int func() {
   return 0;
}



85         // decimal
0213       // octal
0x4b       // hexadecimal
30         // int
30u        // unsigned int
30l        // long
30ul       // unsigned long

// CONSTANTS

sign '#define' preprocessor.
Using 'const' keyword.

#define LENGTH 10   
#define WIDTH  5
#define NEWLINE '\n'

   and

const int  LENGTH = 10;
const int  WIDTH  = 5;
const char NEWLINE = '\n';



===============


cin >> name;  (c input)
cout << nmae;
cerr << "Error message : " << str << endl;
clog << "Error message : " << str << endl;







*/


// IF ELSE  + function returning the max between two numbers

// ver 1
int time = 20;
if (time < 18) {
  cout << "Good day.";
} else {
  cout << "Good evening.";
}



int max(int num1, int num2) {
   // local variable declaration
   int result;
  // ver 2
   if (num1 > num2)
      result = num1;
   else
      result = num2;
 
   return result; 
}
#include <iostream>
using namespace std;
 
// function declaration
int max(int num1, int num2);
 
int main () {
   // local variable declaration:
   int a = 100;
   int b = 200;
   int ret;
 
   // calling a function to get max value.
   ret = max(a, b);
   cout << "Max value is : " << ret << endl;
 
   return 0;
}
 
// function returning the max between two numbers
int max(int num1, int num2) {
   // local variable declaration
   int result;
 
   if (num1 > num2)
      result = num1;
   else
      result = num2;
 
   return result; 
}

// ======================= LOOP =========================================



#include <iostream>
using namespace std;
 
int main () {
   for( ; ; ) {
      printf("This loop will run forever.\n");
   }

   return 0;
}

#include <ctime>
#include <cstdlib>

int main () {
   int i,j;
 
   // set the seed
   srand( (unsigned)time( NULL ) );

   /* generate 10  random numbers. */
   for( i = 0; i < 10; i++ ) {
      // generate actual random number
      j = rand();
      cout <<" Random Number : " << j << endl;
   }

   return 0;
}

// ==================================================

#include <iostream>
using namespace std;
void showstat( int curr ) {

   static int nStatic;    
   nStatic += curr;
   cout << "nStatic is " << nStatic << endl;
}



int main() {
   for ( int i = 0; i < 5; i++ )
      showstat( i );
}




/* =========== Arrays ===============

C++ Code Runner task, press Ctrl + Alt + M 

Declaring Arrays:
type arrayName [ arraySize ];
double balance[10];


Initializing Arrays
double balance[5] = {1000.0, 2.0, 3.4, 17.0, 50.0};

double balance[] = {1000.0, 2.0, 3.4, 17.0, 50.0};
balance[4] = 50.0;

--- imp:
string myStr = "Some Str"
for(char& c : myStr) {
    cout<<(c);
}
int l[] = {1,2,3,4,5,6};
string s = "Tokonbekov";

for (char i : s){
    cout<< i<< "\n";
}

int myNumbers[5] = {10, 20, 30, 40, 50};
for (int i : myNumbers) {
  cout << i << "\n";
}



*/

/* POINTERS and References in C++

C and C++ support pointers, which is different from most other programming languages such as Java, Python, Ruby, Perl and PHP as they only support references. 

Pointers:   A pointer is a variable that holds the memory address of another variable. A pointer needs to be dereferenced with the * operator to access the memory location it points to.
            t.e. pointer is new var which holds another var's mem address

References: A reference variable is an alias, that is, another name for an already existing variable. A reference, like a pointer, is also implemented by storing the address of an object. 
            A reference can be thought of as a constant pointer (not to be confused with a pointer to a constant value!) with automatic indirection, i.e., the compiler will apply the * operator for you.

Example:
            main(){

            string var = "Pizza";
            string &link_var = var;     // created reference or link (alias) to var called  link_var


            cout << link_var <<endl;   // Pizza  chygat

            cout << &var <<endl;        // Memory addres chygat    
            cout << &link_var <<endl;   // t.e.  & menen bashtalyp var kurulsa, reference.  & menen bashtalyp any var chakyrsan ==> mem address


            string *ptr = &var;      //   vardyn mem adressin ptr ga barabarladyk. 

            cout << ptr << "  ptr bul ozu ele called" <<endl;   // ptr bul ozu ele called"
            cout << *ptr << "  *ptr is called, we call it de-refernce" <<endl; // ptr is called, we call it de-reference


            return 0;


more examples:

int a = 10;
int *p = &a;
// OR 
int *p;
p = &a;

//or
   int&    r = i;
   double& s = d;

---------
int a = 5;
int b = 6;
int *p;
p = &a;
p = &b;









#include <bits/stdc++.h>
using namespace std;
void geeks() {
    int var = 20;

    // declare pointer variable
    int* ptr;

    // note that data type of ptr and var must be same
    ptr = &var;

    // assign the address of a variable to a pointer
    cout << "Value at ptr = " << ptr << "\n";
    cout << "Value at var = " << var << "\n";
    cout << "Value at *ptr = " << *ptr << "\n";
}
// Driver program
int main() { 
  geeks(); 
  return 0;
}

*/



/*   Classes and objects early start:

// static2.cpp
// compile with: /EHsc
#include <iostream>

using namespace std;

class CMyClass {

   public:
      static int m_i;

};


int CMyClass::m_i = 0;
CMyClass myObject1;
CMyClass myObject2;

int main() {
   cout << myObject1.m_i << endl;
   cout << myObject2.m_i << endl;

   myObject1.m_i = 1;
   cout << myObject1.m_i << endl;
   cout << myObject2.m_i << endl;

   myObject2.m_i = 2;
   cout << myObject1.m_i << endl;
   cout << myObject2.m_i << endl;

   CMyClass::m_i = 3;
   cout << myObject1.m_i << endl;
   cout << myObject2.m_i << endl;
}


*/

/*    ===================  Storage classes ===============

auto
register
static
extern
mutable


1.  auto - storage class is the default storage class for all local variables.

2.  register -  storage class is used to define local variables that should be stored in a register instead of RAM. This means that the variable has a maximum size equal 
                to the register size (usually one word) and can't have the unary '&' operator applied to it (as it does not have a memory location).

3.  static - storage class instructs the compiler to keep a local variable in existence during the life-time of the program instead of creating and destroying it each time 
             it comes into and goes out of scope. Therefore, making local variables static allows them to maintain their values between function calls.

                  #include <iostream>
                  
                  // Function declaration
                  void func(void);
                  
                  static int count = 10; // Global variable 
                  
                  main() {
                     while(count--) {
                        func();
                     }
                     
                     return 0;
                  }

                  # Function definition

                  void func( void ) {
                     static int i = 5; // local static variable
                     i++;
                     std::cout << "i is " << i ;
                     std::cout << " and count is " << count << std::endl;
                  }


4.  extern - storage class is used to give a reference of a global variable that is visible to ALL the program files. When you use 'extern' the variable cannot be initialized 
             as all it does is point the variable name at a storage location that has been previously defined.


             in first File: main.cpp:

               #include <iostream>
               int count ;
               extern void write_extern();
               
               main() {
                  count = 5;
                  write_extern();
               }
            ----------------------

              in second File: support.cpp
               #include <iostream>

               extern int count;

               void write_extern(void) {
                  std::cout << "Count is " << count << std::endl;
               }

              Now compile these two files:
                 g++ main.cpp support.cpp -o write
                 ./write

5.  mutable - specifier applies only to class objects, which are discussed later in this tutorial. It allows a member of an object to override const member function. 
              That is, a mutable member can be modified by a const member function.




*/


/*    =============== Arithmetic Operators ==========


---------------------------------------------------------------------------------------------------------
  Operator   |                   Description	                                |             Example      |
--------------------------------------------------------------------------------------------------------
     +	    |  Adds two operands	                                         |     A + B will give 30   |
     -	    |  Subtracts second operand from the first	                    |     A - B will give -10  |
     *	    |  Multiplies both operands	                                   |     A * B will give 200  |
     /	    |  Divides numerator by de-numerator	                          |     B / A will give 2    |
     %	    |  Modulus Operator and remainder of after an integer division  |     B % A will give 0    |
     ++	    |  Increment operator, increases integer value by one	        |     A++ will give 11     |
     --	    |  Decrement operator, decreases integer value by one	        |     A-- will give 9      |
---------------------------------------------------------------------------------------------------------


    =============== Logical Operators ==========

---------------------------------------------------------------------------------------------------------
  Operator   |                   Description	                                |             Example      |
--------------------------------------------------------------------------------------------------------
     &&	    |  Called Logical AND operator. 	                             |                          |
     	       |  If both the operands are non-zero then condition becomes true|     (A && B) is false.   |
      	    |                                                               |                          |
     ||	    |  Called Logical OR Operator. If any of the two                |                          |
     	       |  operands is non-zero, then condition becomes true            |     (A || B) is true.    |
      	    |                                                               |                          |
     !	    |  Called Logical NOT Operator. Use to reverses the             |                          |
     	       |  logical state of its operand. If a condition is, then        |                          |
      	    |  then Logical NOT operator will make false                    |      !(A && B) is true   |
---------------------------------------------------------------------------------------------------------









*/

/*  ==================  Structure ===================


C/C++ arrays allow you to define variables that combine several data items of the same kind, but structure is another user defined data type which 
allows you to combine data items of different kinds.

Structures are used to represent a record, suppose you want to keep track of your books in a library. You might want to track the following attributes about each book −

Title
Author
Subject
Book ID

Defining a Structure
To define a structure, you must use the struct statement. The struct statement defines a new data type, with more than one member, for your program. The format of the struct statement is this −

struct [structure tag] {
   member definition;
   member definition;
   ...
   member definition;
} [one or more structure variables];  
The structure tag is optional and each member definition is a normal variable definition, such as int i; or float f; or any other valid variable definition. At the end of the structure's definition, before the final semicolon, you can specify one or more structure variables but it is optional. Here is the way you would declare the Book structure −

struct Books {
   char  title[50];
   char  author[50];
   char  subject[100];
   int   book_id;
} book

EXAMPLE:
#include <iostream>
#include <cstring>
 
using namespace std;
 
struct Books {
   char  title[50];
   char  author[50];
   char  subject[100];
   int   book_id;
};
 
int main() {
   struct Books Book1;        // Declare Book1 of type Book
   struct Books Book2;        // Declare Book2 of type Book
 
   // book 1 specification
   strcpy( Book1.title, "Learn C++ Programming");
   strcpy( Book1.author, "Chand Miyan"); 
   strcpy( Book1.subject, "C++ Programming");
   Book1.book_id = 6495407;

   // book 2 specification
   strcpy( Book2.title, "Telecom Billing");
   strcpy( Book2.author, "Yakit Singha");
   strcpy( Book2.subject, "Telecom");
   Book2.book_id = 6495700;
 
   // Print Book1 info
   cout << "Book 1 title : " << Book1.title <<endl;
   cout << "Book 1 author : " << Book1.author <<endl;
   cout << "Book 1 subject : " << Book1.subject <<endl;
   cout << "Book 1 id : " << Book1.book_id <<endl;

   // Print Book2 info
   cout << "Book 2 title : " << Book2.title <<endl;
   cout << "Book 2 author : " << Book2.author <<endl;
   cout << "Book 2 subject : " << Book2.subject <<endl;
   cout << "Book 2 id : " << Book2.book_id <<endl;

   return 0;
}

OUTPUT:

Book 1 title : Learn C++ Programming
Book 1 author : Chand Miyan
Book 1 subject : C++ Programming
Book 1 id : 6495407
Book 2 title : Telecom Billing
Book 2 author : Yakit Singha
Book 2 subject : Telecom
Book 2 id : 6495700





2. 

// Create a structure variable called myStructure
struct {
  int myNum;
  string myString;
} myStructure;

// Assign values to members of myStructure
myStructure.myNum = 1;
myStructure.myString = "Hello World!";

// Print members of myStructure
cout << myStructure.myNum << "\n";
cout << myStructure.myString << "\n";


struct {
  string brand;
  string model;
  int year;
} myCar1, myCar2; // We can add variables by separating them with a comma here

// Put data into the first structure
myCar1.brand = "BMW";
myCar1.model = "X5";
myCar1.year = 1999;

// Put data into the second structure
myCar2.brand = "Ford";
myCar2.model = "Mustang";
myCar2.year = 1969;

// Print the structure members
cout << myCar1.brand << " " << myCar1.model << " " << myCar1.year << "\n";
cout << myCar2.brand << " " << myCar2.model << " " << myCar2.year << "\n";


*/

/*    =============== Class  ===========

#include <iostream>

using namespace std;

class Box {
   public:
      double length;   // Length of a box
      double breadth;  // Breadth of a box
      double height;   // Height of a box
};

int main() {
   Box Box1;        // Declare Box1 of type Box
   Box Box2;        // Declare Box2 of type Box
   double volume = 0.0;     // Store the volume of a box here
 
   // box 1 specification
   Box1.height = 5.0; 
   Box1.length = 6.0; 
   Box1.breadth = 7.0;

   // box 2 specification
   Box2.height = 10.0;
   Box2.length = 12.0;
   Box2.breadth = 13.0;
   
   // volume of box 1
   volume = Box1.height * Box1.length * Box1.breadth;
   cout << "Volume of Box1 : " << volume <<endl;

   // volume of box 2
   volume = Box2.height * Box2.length * Box2.breadth;
   cout << "Volume of Box2 : " << volume <<endl;
   return 0;




public - members are accessible from outside the class
private - members cannot be accessed (or viewed) from outside the class
protected - members cannot be accessed from outside the class, however, they can be accessed in inherited classes. You will learn more about Inheritance later.

Note: By default, all members of a class are private if you don't specify an access specifier:


class MyClass {
  public:    // Public access specifier
    int x;   // Public attribute
  private:   // Private access specifier
    int y;   // Private attribute
};

int main() {
  MyClass myObj;
  myObj.x = 25;  // Allowed (public)
  myObj.y = 50;  // Not allowed (private)
  return 0;
}



}

*/


/*   ++++ math +++

cout << max(5, 10);
min(5, 10);

#include <cmath>

cout << sqrt(64);
cout << round(2.6);
cout << log(2)


=== boolean ===:

cout << (10 > 9);  => true
int x = 10;
cout << (x == 10);  /

----------- IF ELSE ----------------

Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
Equal to a == b
Not Equal to: a != b


Use if            to specify a block of code to be executed, if a specified condition is true
Use else          to specify a block of code to be executed, if the same condition is false
Use else          if to specify a new condition to test, if the first condition is false
Use switch        to specify many alternative blocks of code to be executed

EXAMPLE:

int myAge = 25;
int votingAge = 18;

if (myAge >= votingAge) {
  cout << "Old enough to vote!";
} else {
  cout << "Not old enough to vote.";
}
---------

int time = 20;
if (time < 18) {
  cout << "Good day.";
} else {
  cout << "Good evening.";
}
// Outputs "Good evening."

----------------------


int time = 22;
if (time < 10) {
  cout << "Good morning.";
} else if (time < 20) {
  cout << "Good day.";
} else {
  cout << "Good evening.";
}
// Outputs "Good evening."

---------- short -- if else ------------

int time = 20;
string result = (time < 18) ? "Good day." : "Good evening.";
cout << result;

-------------- SWITCH ----------

int day = 4;
switch (day) {
  case 1:
    cout << "Monday";
    break;
  case 2:
    cout << "Tuesday";
    break;
  case 3:
    cout << "Wednesday";
    break;
  case 4:
    cout << "Thursday";
    break;
  case 5:
    cout << "Friday";
    break;
  case 6:
    cout << "Saturday";
    break;
  case 7:
    cout << "Sunday";
    break;
}

---------- default -------
int day = 4;
switch (day) {
  case 6:
    cout << "Today is Saturday";
    break;
  case 7:
    cout << "Today is Sunday";
    break;
  default:
    cout << "Looking forward to the Weekend";
}
// Outputs "Looking forward to the Weekend"

------------ while loop -----
int i = 0;
while (i < 5) {
  cout << i << "\n";
  i++;
}

-------------- DO --------------

int i = 0;
do {
  cout << i << "\n";
  i++;
}
while (i < 5);


----------- For Loop --------

for (int i = 0; i < 5; i++) {
  cout << i << "\n";
}

----------- nested for loop -------
// Outer loop
for (int i = 1; i <= 2; ++i) {
  cout << "Outer: " << i << "\n"; // Executes 2 times

  // Inner loop
  for (int j = 1; j <= 3; ++j) {
    cout << " Inner: " << j << "\n"; // Executes 6 times (2 * 3)
  }
}

--------- foreach Loop -----------

int myNumbers[5] = {10, 20, 30, 40, 50};
for (int i : myNumbers) {
  cout << i << "\n";
}

---------- break and condinue -------

for (int i = 0; i < 10; i++) {
  if (i == 4) {
    break;
  }
  cout << i << "\n";
}

for (int i = 0; i < 10; i++) {
  if (i == 4) {
    continue;
  }
  cout << i << "\n";
}


------------- Arrays -----------

string cars[4];
string cars[4] = {"Volvo", "BMW", "Ford", "Mazda"};

int myNumbers[5] = {10, 20, 30, 40, 50};
cout << sizeof(myNumbers);

string cars[5] = {"Volvo", "BMW", "Ford", "Mazda", "Tesla"};
for (int i = 0; i < 5; i++) {
  cout << cars[i] << "\n";
}

int myNumbers[5] = {10, 20, 30, 40, 50};
for (int i = 0; i < 5; i++) {
  cout << myNumbers[i] << "\n";
}


string letters[2][4] = {
  { "A", "B", "C", "D" },
  { "E", "F", "G", "H" }
};

string letters[2][2][2] = {
  {
    { "A", "B" },
    { "C", "D" }
  },
  {
    { "E", "F" },
    { "G", "H" }
  }
};

string letters[2][4] = {
  { "A", "B", "C", "D" },
  { "E", "F", "G", "H" }
};

for (int i = 0; i < 2; i++) {
  for (int j = 0; j < 4; j++) {
    cout << letters[i][j] << "\n";
  }
}



*/




/* ================= enum Level ===============

An enum is a special type that represents a group of constants (unchangeable values). returns  "0", index of LOW by default

enum Level {
  LOW,
  MEDIUM,
  HIGH
};

enum Level myVar;

enum Level myVar = MEDIUM;

this returns  "1", index of MEDIUM

------------

#include <iostream>
using namespace std;
 
enum Level {
  LOW = 25,
  MEDIUM = 50,
  HIGH = 75
}; 

int main() {
  enum Level myVar = MEDIUM;
  cout << myVar;
  return 0;
}
 returns: 50


---------------

enum Level {
  LOW = 1,
  MEDIUM,
  HIGH
};

int main() {
  enum Level myVar = MEDIUM;   


  switch (myVar) {
    case 1:
      printf("Low Level");
      break;
    case 2:
      printf("Medium level");
      break;
    case 3:
      printf("High level");
      break;
  }
  return 0;
}




*/



/*
          ============================ Creating References +++++++++++++

string food = "Pizza";
string &meal = food;

cout << food << "\n";  // Outputs Pizza
cout << meal << "\n";  // Outputs Pizza                                                             note 1:  not using &   when we call  ------  meal



================== C++ Memory Address =============


string food = "Pizza";

cout << &food; // Outputs 0x6dfed4                                                                 note 2:  using &   when we call    ----       &food  


cout << food;                // Outputs the value of food (Pizza)
cout << &food;               // Outputs the memory address of food (0x6dfed4)



=======================  POINTERS =====================

string* mystring; // Preferred
string *mystring;
string * mystring;


string food = "Pizza";  // A food variable of type string
string *ptr = &food;    // A pointer variable, with the name ptr, that stores the address of food


// Output the value of food (Pizza)
cout << food << "\n";

// Output the memory address of food (0x6dfed4)
cout << &food << "\n";

// Output the memory address of food with the pointer (0x6dfed4)
cout << ptr << "\n";



============== Dereference =============

string food = "Pizza";  // Variable declaration
string *ptr = &food;    // Pointer declaration

// Reference: Output the memory address of food with the pointer (0x6dfed4)
cout << ptr << "\n";

// Dereference: Output the value of food with the pointer (Pizza)
cout << *ptr << "\n"


// Change the value of the pointer
*ptr = "Hamburger";

// Output the new value of the pointer (Hamburger)
cout << *ptr << "\n";

// Output the new value of the food variable (Hamburger)
cout << food << "\n";



string txt = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
cout << "The length of the txt string is: " << txt.length() <<endl;
cout << "The length of the txt string is: " << txt.size();

int myNumbers[5] = {10, 20, 30, 40, 50};
cout << sizeof(myNumbers);

Update string character; 
myString="Hello"
myString.at(0) = 'J';
cout << myString;

#include <cmath>

cout << sqrt(64);
cout << round(2.6);
cout << log(2);

++++++++++++  enum ============

#include <iostream>
using namespace std;
 
enum Level {
  LOW = 1,
  MEDIUM,
  HIGH
};

int main() {
  enum Level myVar = MEDIUM;

  switch (myVar) {
    case 1:
      printf("Low Level");
      break;
    case 2:
      printf("Medium level");
      break;
    case 3:
      printf("High level");
      break;
  }
  return 0;
}




*/


/*

========================================= DATA Struture =========================================


Vector  ---   same as array used to store multiple elements, of the same data type
              The difference between an array and a vector, is that the size of an array cannot be modified (you cannot add or remove elements from an array). A vector however, can grow or shrink by itself.(list)
#include <vector>
vector<string> cars = {"Volvo", "BMW", "Ford", "Mazda"};

// Get the first element
cout << cars[0];  // Outputs Volvo

// Get the second element
cout << cars[1];  // Outputs BMW
vector<string> cars = {"Volvo", "BMW", "Ford", "Mazda"};

// Get the first element
cout << cars.front();

// Get the last element
cout << cars.back();

// Create a vector called cars that will store strings
vector<string> cars = {"Volvo", "BMW", "Ford", "Mazda"};

// Get the second element
cout << cars.at(1);

// Get the third element
cout << cars.at(2);


Change Vector:
-------------


vector<string> cars = {"Volvo", "BMW", "Ford", "Mazda"};

// Change the value of the first element
cars[0] = "Opel";

cout << cars[0];  // Now outputs Opel instead of Volvo


Add items into Vector:
""""""""""""""""""""""

vector<string> cars = {"Volvo", "BMW", "Ford", "Mazda"};
cars.push_back("Tesla");

Remove items from Vector:
""""""""""""""""""""""""

vector<string> cars = {"Volvo", "BMW", "Ford", "Mazda"};
cars.pop_back();


Check size (length)
""""""""""""""""""
vector<string> cars = {"Volvo", "BMW", "Ford", "Mazda"};
cout << cars.size();  // Outputs 4


Check if Vector is epmpty:
""""""""""""""""""""""""""
vector<string> cars;
cout << cars.empty();  // Outputs 1 (The vector is empty)

Loop:
""""""

vector<string> cars = {"Volvo", "BMW", "Ford", "Mazda"};

for (string car : cars) {
  cout << car << "\n";
}



-----------------------------------------

#include <list>

LIST - A list is similar to a vector in that it can store multiple elements of the same type and dynamically grow in size.

      Two of the major differences between lists and vectors are:
      You can easily add and remove elements from both the beginning and at the end of a list, while vectors are generally optimized for adding at the end.
      Unlike vectors, a list does not support random access, meaning you cannot directly jump to a specific index, or access elements by index numbers



You cannot access list elements by referring to index numbers, like with arrays and vectors
However, you can access the first or the last element with the .front() and .back() functions, respectively:



// Create a list called cars that will store strings
list<string> cars = {"Volvo", "BMW", "Ford", "Mazda"};

// Get the first element
cout << cars.front();  // Outputs Volvo

// Get the last element
cout << cars.back();  // Outputs Mazda


Change value on 1st and last item:
""""""""""""""""""""""""""""""""
list<string> cars = {"Volvo", "BMW", "Ford", "Mazda"};

// Change the value of the first element
cars.front() = "Opel";

// Change the value of the last element
cars.back() = "Toyota";

cout << cars.front(); // Now outputs Opel instead of Volvo
cout << cars.back();  // Now outputs Toyota instead of Mazda


Add:
""""
list<string> cars = {"Volvo", "BMW", "Ford", "Mazda"};

// Add an element at the beginning
cars.push_front("Tesla");

// Add an element at the end
cars.push_back("VW");

Remove:
""""""""
list<string> cars = {"Volvo", "BMW", "Ford", "Mazda"};

// Remove the first element
cars.pop_front();

// Remove the last element
cars.pop_back();


----------------------------------------

#include <deque>

Deque   -   A deque (stands for double-ended queue) is like a combination of a vector and a list, as elements can be:
            Added and removed from both ends fast, like a list.
            Accessed by index numbers (supports random access), like vectors.

// Create a deque called cars that will store strings
deque<string> cars = {"Volvo", "BMW", "Ford", "Mazda"};

// Get the first element
cout << cars[0];  // Outputs Volvo

// Get the second element
cout << cars[1];  // Outputs BMW


deque<string> cars = {"Volvo", "BMW", "Ford", "Mazda"};

// Get the first element
cout << cars.front();

// Get the last element
cout << cars.back();


// Create a deque called cars that will store strings
deque<string> cars = {"Volvo", "BMW", "Ford", "Mazda"};

// Get the second element
cout << cars.at(1);

// Get the third element
cout << cars.at(2);

// Create a deque called cars that will store strings
deque<string> cars = {"Volvo", "BMW", "Ford", "Mazda"};

// Try to access an element that does not exist (will throw an exception)
cout << cars.at(6);


deque<string> cars = {"Volvo", "BMW", "Ford", "Mazda"};

// Change the value of the first element
cars.at(0) = "Opel";

cout << cars.at(0);  // Now outputs Opel instead of Volvo


cars.pop_back();
cout << cars.size(); 
cout << cars.empty();

for (int i = 0; i < cars.size(); i++) {
  cout << cars[i] << "\n";
}


-------------------
#include <set>
SET  - list but no duplicate:

set<string> cars = {"Volvo", "BMW", "Ford", "BMW", "Mazda"};

// Print set elements
for (string car : cars) {
  cout << car << "\n";
}
output:
BMW              (only once)
Ford
Mazda
Volvo



// Sort elements in a set in descending order
set<int, greater<int>> numbers = {1, 7, 3, 2, 5, 9};
// Print the elements
for (int num : numbers) {
  cout << num << "\n";
}

add:
""""

set<string> cars = {"Volvo", "BMW", "Ford", "Mazda"};

// Add new elements
cars.insert("Tesla");
cars.insert("VW");
cars.insert("Toyota");
cars.insert("Audi");

remove:
""""""
set<string> cars = {"Volvo", "BMW", "Ford", "Mazda"};

// Remove elements
cars.erase("Volvo");
cars.erase("Mazda");

cout << cars.size(); 
cout << cars.empty();

set<string> cars = {"Volvo", "BMW", "Ford", "Mazda"};

for (string car : cars) {
  cout << car << "\n";
}


------------------  Maps ----------------------------------------------  

#include <map>

A map stores elements in "key/value" pairs.
Elements in a map are:
Accessible by keys (not index), and each key is unique.
Automatically sorted in ascending order by their keys.


Create:

map<string, int> people
or
map<string, int> people = { {"John", 32}, {"Adele", 45}, {"Bo", 29} };


// Create a map that will store the name and age of different people
map<string, int> people = { {"John", 32}, {"Adele", 45}, {"Bo", 29} };

// Get the value associated with the key "John"
cout << "John is: " << people["John"] << "\n";

// Get the value associated with the key "Adele"
cout << "Adele is: " << people["Adele"] << "\n";


// Create a map that will store the name and age of different people
map<string, int> people = { {"John", 32}, {"Adele", 45}, {"Bo", 29} };

 // Get the value associated with the key "Adele"
cout << "Adele is: " << people.at("Adele") << "\n";

// Get the value associated with the key "Bo"
cout << "Bo is: " << people.at("Bo") << "\n";



// Create a map that will store the name and age of different people
map<string, int> people = { {"John", 32}, {"Adele", 45}, {"Bo", 29} };

// Try to access an element that does not exist (will throw an exception)
cout << people.at("Jenny");


change:
""""""
map<string, int> people = { {"John", 32}, {"Adele", 45}, {"Bo", 29} };

// Change John's value to 50 instead of 32
people["John"] = 50;

cout << "John is: " << people["John"];  // Now outputs John is: 50


map<string, int> people = { {"John", 32}, {"Adele", 45}, {"Bo", 29} };

// Change John's value to 50 instead of 32
people.at("John") = 50;

cout << "John is: " << people.at("John");  // Now outputs John is: 50



Add:
""""
map<string, int> people = { {"John", 32}, {"Adele", 45}, {"Bo", 29} };

// Add new elements
people["Jenny"] = 22;
people["Liam"] = 24;
people["Kasper"] = 20;
people["Anja"] = 30;


map<string, int> people = { {"John", 32}, {"Adele", 45}, {"Bo", 29} };

// Add new elements
people.insert({"Jenny", 22});
people.insert({"Liam", 24});
people.insert({"Kasper", 20});
people.insert({"Anja", 30});


remove:
""""""
1.
map<string, int> people = { {"John", 32}, {"Adele", 45}, {"Bo", 29} };

// Remove an element by key
people.erase("John");

2.
map<string, int> people = { {"John", 32}, {"Adele", 45}, {"Bo", 29} };

// Remove all elements
people.clear();



cout << people.empty();
// Outputs 1 (The map is empty)
// Outputs 0 (not empty)



Loop Through a Map:
""""""""""""""""""
        An easy way to loop through a map is with the for-each loop. However, there are a couple of things to be aware of:

        You should use the auto keyword inside the for loop. This allows the compiler to automatically determine the correct data type for each key-value pair.
        Since map elements consist of both keys and values, you have to include .first to access the keys, and .second to access values in the loop.

map<string, int> people = { {"John", 32}, {"Adele", 45}, {"Bo", 29} };

for (auto person : people) {
  cout << person.first << " is: " << person.second << "\n";
}


























*/
