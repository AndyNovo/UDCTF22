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
    char buf[24]; 
    gets(buf); 
} 

int main(){ 
    init();
    printf("How about reading a leak? %p\n", win); 
    vuln(); 
    return 0; 
} 
