#include<stdio.h>
#include<stdlib.h>
#include<time.h>

char op(){
    srand(time(0));
    int n;
    n=rand()%10;
    if(n>=1 && n<=3)
        return('S');
    else if(n>=4 && n<=6)
        return('p');
    if(n>=1 && n<=9)
        return('s');}

int result(char c,char y){
    /*if((c=='S' && y=='s') || (c=='p' && y=='S') || (c=='s' && y=='p'))
        return (-1);
    else if((c=='S' && y=='p') || (c=='p' && y=='s') || (c=='s' && y=='S'))
        return (1);
    else
        return 0;}*/
    if(y=='S'){
        printf("You chose stone || ");
        if(c=='s'){
            printf("Computer chose scissor\n");
            return (1);}
        else if(c=='p'){
            printf("Computer chose paper\n");
            return (-1);}
        else{
            printf("Computer chose stone\n");
            return 0;}}

    if(y=='p'){
    printf("You chose paper || ");
    if(c=='s'){
        printf("Computer chose scissor\n");
        return (-1);}
    else if(c=='S'){
        printf("Computer chose stone\n");
        return (1);}
    else{
        printf("Computer chose paper\n");
        return 0;}}
    
    if(y=='s'){
        printf("You chose scissor || ");
        if(c=='S'){
            printf("Computer chose stone\n");
            return (-1);}
        else if(c=='p'){
            printf("Computer chose paper\n");
            return (1);}
        else{
            printf("Computer chose scissor\n");
            return 0;}}
    }
        
void main(){
    char you,comp,ch,d;
    int ys=0,cs=0,r;
    game:
    for(;ys<5 && cs<5;){
        input:
        printf("Enter 'S' for stone, 'p' for paper & 's' for scissor: ");
        scanf("%c",&you);
        scanf("%c",&d);
        if((you !='S' && you !='p' && you !='s')){
            printf("Wrong input!\n");
            goto input;}
        comp=op();
        r=result(comp,you);
        if(r==1){
            ys++;
            printf("You win!\n");}
        else if(r==(-1)){
            cs++;
            printf("You Lose!\n");}
        else 
            printf("Draw!\n");
        printf("Score: You %d\tComputer %d\n",ys,cs);}
    if(ys==5)
        printf("You win the game!\n");
    else
        printf("You loose the game!\n");
    printf("Do you want to play again?(y/n) ");
    scanf("%c",&ch);
    scanf("%c",&d);
    if(ch=='y'){
        ys=0;
        cs=0;
        goto game;} 
}