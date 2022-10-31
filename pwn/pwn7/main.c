#include <stdlib.h> 
#include <stdio.h> 

void init(){
    setvbuf(stdin,NULL,_IONBF,0);
    setvbuf(stdout,NULL,_IONBF,0);
    setvbuf(stderr,NULL,_IONBF,0);
}

void win(unsigned int x){ 
    if (x != 0xdeadbeef){
        puts("Almost...");
	return;
    }
    system("/bin/sh");
} 

void vuln(){
    printf("How about creating a leak AND smashing a canary?"); 
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
