/*
- C is general purpose, inveted by Dennis Ritchie at AT&T Bell Labs
- Was used to develop the UNIX system
- is a MUST for students becoming a Software Enginer

- Successor to the B language introduced in the early 1970s
*/

//Hello world in C:

#include <stdio.h>

int  main() {
    printf("Hello, World! \n");

    return 0;
}

/*
C is used for:

- Operating Systems
- language compilers
- Assemblers
- Text Editors
- Print Spoolers
- Network Drivers
- Modern Programs
- Databases
- Language Interpreters
- Utilities

c programs are written with the .c extension

To run C programs, need text editor (Using Mint's built in text editor) and the C compiler (version 9 installed with mint by default)

Program needs to be compiled into machine friendly code, hence the use of a compiler (remeber execution cycle from OS notes)


A C program consists of:
- Preprocessor Commands
- Functions
- Variables
- Statements & Expressions
- Comments

In the Hello World example:

- First line is a preprocessor command telling the compiler to include the <stdio.h> file before actually compiling
- The next line is the declaration of the main() function where program execution begins
- printf() is another function which prints the output to the screen
- The next line terminates the main fnction by returning 0 (returns 0 because int main specifies that an int must be returned after function execution)

Tokens in C

- Tokens are either a keyword, an identifier, a constant, a string literal or a symbol. For example,

printf("Hello, World! \n");

can be broken into 5 tokens

printf
(
    "Hello, World! \n"    
)
;

Semicolons in the C programming language are statement terminators, meaning each individual statement must be ended with a semicolon

ex.

printf("Hello, World! \n");

 

Identifiers are names used to identify a variable, function or user defined item. they can only have:
- a letter (A - Z or a - z, must start with letter)
- underscore (can start with an underscore)
- more letters or digits

keywords: reserved words in C which include:

auto        else    long        switch
break       enum    register    typedef
case        extern  return      union
char        float   short       unsigned
const       for     signed      void
continue    goto    sizeof      volatile
default     if      static      while
do          int     struct      _Packed
double

- C ignores whitespace (blank lines)

- C has data types that are used whn declaring variables or functions of different types. The type of a variable determines the space it occupies in storage and how the bit pattern stored is interpreted

Types include:

1) Basic Types
- Arithmetic types that are further classified into: (a) integer types and (b) floating-point types

2) Enumerated Types
- Arithmetic types used to define variabls that can only be assigned a discrete integer value through the program

3) The type void
- Type specifier void indicating no value is available

4) Derived types
- They include (a) Pointer types, (b) Array types, (c) Structure types, (d) Union types and (e) Function types

The following table provides information regarding integer types

Type                Storage Size                            Value Range

char                1 byte
unsigned char       1 byte
signed char         1 byte
int                 2 bytes or 4 bytes
unsigned int        2 bytes or 4 bytes
short               2 bytes
unsigned short      2 bytes
long                8 bytes or 4 bytes(32bitOS)
unsigned long       8 bytes

*/

// single line comment

/*
multiline comment
*/
