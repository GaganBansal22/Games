#include<stdio.h>

char op(char you){
    if(you=='S')
        return 'p';
    if(you=='p')
        return 's';
    if(you=='s')
        return 'S';}

void result(char c,char y){
    if(y=='S'){
        printf("You chose stone || ");
        if(c=='s'){
            printf("Computer chose scissor\n");}
        else if(c=='p'){
            printf("Computer chose paper\n");}
        else
            printf("Computer chose stone\n");}

    if(y=='p'){
    printf("You chose paper || ");
    if(c=='s'){
        printf("Computer chose scissor\n");}
    else if(c=='S'){
        printf("Computer chose stone\n");}
    else
        printf("Computer chose paper\n");}
    
    if(y=='s'){
        printf("You chose scissor || ");
        if(c=='S'){
            printf("Computer chose stone\n");}
        else if(c=='p'){
            printf("Computer chose paper\n");}
        else
            printf("Computer chose scissor\n");}}
        
void main(){
    char you,comp,ch,d;
    int cs=0,r;
    game:
    for(cs=1;cs<=5;cs++){
        input:
        printf("Enter 'S' for stone, 'p' for paper & 's' for scissor: ");
        scanf("%c",&you);
        scanf("%c",&d);
        if((you !='S' && you !='p' && you !='s')){
            printf("Wrong input!\n");
            goto input;}
        comp=op(you);
        result(comp,you);
        printf("Score: You 0\tComputer %d\n",cs);}
    printf("You loose the game!\n");
    printf("Do you want to play again?(y/n) ");
    scanf("%c",&ch);
    scanf("%c",&d);
    if(ch=='y')
        goto game;
}