%{
void print(){
	printf("%s\n",yytext);
}
%}
%%
if	{print();}
[a-z][a-z0-9]*	{print();}
[0-9]+	{print();}
[a-z0-9]+	{print("ERROR\n");}
[ \t\n]	{}
.	{printf("ERROR\n");}
%%
int yywrap(){
	return 1;
}
int main(int argc, char *argv[]){
	yyin = fopen(argv[1],"r");
	yylex();
	return 0;
}