#include <stdio.h>
#include <math.h>
#include <time.h>

int main(){
    clock_t tm1, tm2;
    double tm;
    long m, i;
    tm1 = clock();
    for (i =1; i < pow(10,7); i++){
        m = i * i;
    }
    tm2 = clock();
    tm = ((double)(tm2 - tm1)) / CLOCKS_PER_SEC;
    printf("time = %f ms\n", tm * 1000);
    printf("i = %ld\n", i);
    printf("m = %ld\n", m);
    printf("max of long int: %ld\n",LONG_MAX);
    return 0;
}
