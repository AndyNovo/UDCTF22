#include <stdlib.h> 
#include <stdio.h> 

void win(){ 
    system("/bin/sh"); 

} 

void vuln(){
    char buf[55]; 
    gets(buf); 
} 

int main(){ 
    puts("Level 2: Control the IP\n"); 
    vuln(); 
    return 0; 
} 
