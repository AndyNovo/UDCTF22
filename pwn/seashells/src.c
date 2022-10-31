#include <stdio.h>
#include <stdlib.h>

void init(){ 
    setvbuf(stdin,NULL,_IONBF,0);
    setvbuf(stdout,NULL,_IONBF,0);
    setvbuf(stderr,NULL,_IONBF,0);
}

int main(){
        init();
        long local_8=0x54e11;
        long local_16=0,local_24=0,local_32=0,local_40=0x54e11;
        long local_48=0x54e11;
        char local_60[12];

        printf("So this is where Sally sold her sea SHELLS: %p\n",local_60);
        fgets(local_60,0x60,stdin);
        if((local_48=0x5ea54e115ea54e11) && (local_8=0xdeadbeef)){
                       return 0;
        }
        exit(1);
}
