#python 2.7
me='me=%r\nprint me %% me'
print me % me

#python 3.0+
me='me=%r\nprint (me %% me)'
print (me % me)

#C version written by others
#include <stdio.h>
char* recurse = "#include <stdio.h>%cchar* recurse=%c%s%c;%cvoid main(){printf(recurse,10,34,recurse,34,10,10);}%c";
void main(){printf(recurse,10,34,recurse,34,10,10);}





#reference:
#[1] 《Introduction to the Theory of Computation》Michael Sipser  chapter 6
#[2] 《哥德尔、艾舍尔、巴赫》侯世达
#[3] 《复杂》梅拉妮·米歇尔
#[4] 《Theory of Self-Reproducing Automata》 John von Neumann
