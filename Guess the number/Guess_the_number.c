#include<stdio.h>
#include<stdlib.h>
#include<time.h>

void main(){
    int n,g,t=1,i,p,ip,min,minp;
    char ch;
    srand(time(0));
    players:
    printf("Enter number of players: ");
    scanf("%d",&p);
    if(p<=0)
        goto players;
    int pt[p],d[p],dc=0,tn=0;
    for(ip=0;ip<p;ip++){
        if(p>1)
            printf("Player %d's turn\n",ip+1);
        n=(rand()%100 +1)/2;  //Do not divide by 2 for no b/w 1-100 & divide by 4 for no b/w 1-25
        t=1;
        //printf("%d\n",n);
        repeat1:
        printf("Guess number between 1 to 50: ");
        scanf("%d",&g);
        if(g<0 || g>50){
            printf("Wrong Input!\n");
            goto repeat1;}
        for(i=0;g!=n;i++){
            if(g<n)
                printf("Higher number please!\n");
            else if(g>n)
                printf("Lower number please!\n");
            repeat2:
            printf("Guess again: ");
            scanf("%d",&g);
            if(g<0 || g>50){
                printf("Wrong Input!\n");
                goto repeat2;}
            t++;}
        printf("Number of guesses taken: %d\n",t);
        pt[ip]=t;}
    if(p>1){
        printf("Number turns taken by\n");
        for(i=0;i<p;i++)
            printf("Player %d: %d\n",i+1,pt[i]);
        for(i=0;i<p;i++){
            d[i]=pt[i];
            for(ip=0;ip<p;ip++){
                if(i!=ip){
                    if(d[i]==pt[ip]){
                        tn=d[i];
                        dc++;}}}}
        min=pt[0];
        minp=0;
        for(i=1;i<p;i++){
            if(pt[i]<min){
                min=pt[i];
                minp=i;}}
        if(!dc)
            printf("Player %d wins!\n",minp+1);
        if(dc){
            if(tn>min)
                printf("Player %d wins!\n",minp+1);
            else
                printf("Tie!\n");}}
    printf("Do you want to play again? ");
    scanf("%c",&ch);
    scanf("%c",&ch);
    if(ch=='y')
        goto players;
}