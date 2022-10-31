#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void init(){ 
    setvbuf(stdin,NULL,_IONBF,0);
    setvbuf(stdout,NULL,_IONBF,0);
    setvbuf(stderr,NULL,_IONBF,0);
} 

int main(){
        init();
        char input[64];
        printf("This might help you out: %p\n",input);
        gets(input);
        fflush(stdout);
        printf(input);
        fflush(stdout);
        gets(input);
        return 0;
}
