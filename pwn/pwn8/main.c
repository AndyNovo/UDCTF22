#include <stdlib.h> 
#include <stdio.h> 

void init(){
    setvbuf(stdin,NULL,_IONBF,0);
    setvbuf(stdout,NULL,_IONBF,0);
    setvbuf(stderr,NULL,_IONBF,0);
}

int gateway1=0;
int gateway2=0;
int gateway3=0;

void func1(unsigned int a){
    if (a == 0x1337){
        gateway1=1;
    }
}

void func2(unsigned int a){
    if (a == 0xcafef00d){
        gateway2=1;
    }
}

void func3(unsigned int a){
    if (a == 0xd00df00d){
        gateway3=1;
    }
}

void win(unsigned int x){ 
    if (!gateway1 || !gateway2 || !gateway3){
        puts("Almost...");
	return;
    }
    system("/bin/sh");
} 

void vuln(){
    printf("How about creating a leak AND smashing a canary AND chaining several functions?"); 
    char buf1[24];
    gets(buf1); 
    printf(buf1);
    char buf2[24]; 
    gets(buf2); 
} 

int main(){ 
    init();
    vuln(); 
    return 0; 
} 
