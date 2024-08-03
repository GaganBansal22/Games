#include<stdio.h>
void main(){
    int c,u,count=0,i;
    char ch,d;
    repeat:
    for(i=0;i<4;i++){
        input:
        printf("Choose 1,2,3 or 4: ");
        scanf("%d",&u);
        if(u>4 || u<1){
            printf("Wrong input! Try again\n");
            goto input;}
        c=5-u;
        count+=5;
        printf("Computer chose: %d\nCount= %d\n",c,count);}
    printf("Choose 1,2,3 or 4: ");
        scanf("%d",&u);
    printf("Count= %d\n",count+u);
    printf("You loose!");
    printf("\nDo you want to play again? ");
    scanf("%c",&d);
    scanf("%c",&ch);
    if(ch=='y'){
        count=0;
        goto repeat;}
}