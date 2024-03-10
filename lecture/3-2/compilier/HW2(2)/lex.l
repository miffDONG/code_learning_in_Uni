%{
#include <stdio.h>

int acceptedTokens = 0;
int rejectedTokens = 0;
%}

%option noyywrap

%%
if      { printf("IF(if)\n"); acceptedTokens++; }
[a-z][a-z0-9]*   { printf("ID(%s)\n", yytext); acceptedTokens++; }
[0-9]+   { printf("NUM(%s)\n", yytext); acceptedTokens++; }
[a-z0-9]+   { printf("ERROR\n"); rejectedTokens++; }
[ \t\n]   { /* 공백 및 탭 문자는 무시 */ }
.   { printf("ERROR\n"); rejectedTokens++; }
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

    printf("# Accepted tokens: %d\n", acceptedTokens);
    printf("# of Rejected tokens: %d\n", rejectedTokens);

    return 0;
}
