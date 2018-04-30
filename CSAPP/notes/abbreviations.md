# Abbreviations

1.  GNU
    GNU is a recursive acronym for "GNU's Not Unix".
2.  GCC
    1.  GNU Compiler Collection
        The GNU Compiler Collection (GCC) is a compiler system produced by the GNU Project supporting various programming languages.
    2.  GNU C Compiler
        Originally named the GNU C Compiler, when it only handled the C programming language, GCC 1.0 was released in 1987.
3.  cpp
    A program that processes the C programming language before it is compiled. The **C preprocessor** or **cpp** is the macro preprocessor for the C and C++ computer programming languages. The preprocessor provides the ability for the inclusion of header files, macro expansions, conditional compilation, and line control. In many C implementations, it is a separate program invoked by the compiler as the first part of translation.
4.  cc1
    A C compiler in the GNU Compiler Collection. **cc1** is the internal command which takes preprocessed C-language files and converts them to assembly. It's the actual part that compiles C. For C++, there's **cc1plus**, and other internal commands for different languages.
5.  as
    **as** is a generic name for an assembler on Unix. On many systems the standard or pre-installed assembler is the GNU Assembler, commonly called GAS, whose executable is simply named **as**.
6.  ld
    The linker command on Unix and Unix-like systems. In computing, a **linker** or **link editor** is a computer utility program that takes one or more object files generated by a compiler and combines them into a single executable file, library file, or another 'object' file. A simpler version that writes its output directly to memory is called the *loader*, though loading is typically considered a separate process. Possible origins of the name "**ld**" are "**LoaD**" and "**Link eDitor**".

An answer from Unix & Linux Stack Exchange:
> GCC has a number of phases to its compilation, and it uses different internal commands to do each phase. C in particular is first preprocessed with cpp, then is compiled into assembly, assembled into machine language, and then linked together.

> cc1 is the internal command which takes preprocessed C-language files and converts them to assembly. It's the actual part that compiles C. For C++, there's cc1plus, and other internal commands for different languages.

Links:
[GNU](https://en.wikipedia.org/wiki/GNU)
[GNU_Compiler_Collection](https://en.wikipedia.org/wiki/GNU_Compiler_Collection)
[C_preprocessor](https://en.wikipedia.org/wiki/C_preprocessor)
[As_(Unix)](https://en.wikipedia.org/wiki/As_(Unix))
[GNU_Assembler](https://en.wikipedia.org/wiki/GNU_Assembler)
[Linker_(computing)](https://en.wikipedia.org/wiki/Linker_(computing))
[GNU_linker](https://en.wikipedia.org/wiki/GNU_linker)
[The answer](https://unix.stackexchange.com/questions/77779/relationship-between-cc1-and-gcc/77781#77781)