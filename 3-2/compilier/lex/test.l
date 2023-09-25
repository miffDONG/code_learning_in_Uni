%{
void print(){
	printf("%s\n",yytext);
}
%}
%%
.	{print();}
\n	{print();}
%%
int yywrap(){
	return 1;
}
int main(){
	yylex();
	return 0;
}