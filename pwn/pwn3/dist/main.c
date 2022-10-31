#include <stdlib.h> 
#include <stdio.h> 

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
    puts("Level 3: Args too?\n"); 
    vuln(); 
    return 0; 
} 
