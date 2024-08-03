#include<stdio.h>
#include<stdlib.h>
#include<time.h>

void main(){
    int c,u,count=0,oe=0;
    char ch,d;
    srand(time(0));
    repeat:
    for(;count<=20;){
        input:
        printf("Choose 1,2,3 or 4: ");
        scanf("%d",&u);
        if(u>4 || u<1){
            printf("Wrong input! Try again\n");
            goto input;}
            oe++;
            count+=u;
        if(count<=20){
            c=(rand()%100)/25 +1;
            count+=c;
            printf("Computer chose: %d\nCount= %d\n",c,count);
            oe++;}}
    if(oe%2)
        printf("You loose!");
    else
        printf("You win!");
    printf("\nDo you want to play again? ");
    scanf("%c",&d);
    scanf("%c",&ch);
    if(ch=='y'){
        count=0;
        oe=0;
        goto repeat;}
}