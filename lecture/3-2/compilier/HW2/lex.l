%{
#include <stdio.h>
%}

%option noyywrap

%%
if      { printf("IF(if)\n"); }
[a-z][a-z0-9]*   { printf("ID(%s)\n", yytext); }
[0-9]+   { printf("NUM(%s)\n", yytext); }
[a-z0-9]+   { printf("ERROR\n"); }
[ \t\n]   { /* 공백 및 탭 문자는 무시 */ }
.   { printf("ERROR\n"); }
%%

int main(int argc, char *argv[]){
    if (argc != 2) {
        printf("Usage: %s <input_file>\n", argv[0]);
        return 1;
    }

    FILE *inputFile = fopen(argv[1], "r");
    if (inputFile == NULL) {
        perror("Failed to open the input file");
        return 1;
    }

    yyin = inputFile;
    yylex();

    fclose(inputFile);
    return 0;
}
