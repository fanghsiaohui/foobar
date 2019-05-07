#include <stdio.h>
#include <math.h>
#include <time.h>

int main(){
    clock_t tm1, tm2;
    double tm;
    tm1 = clock();
    for (int i =1; i < pow(10,7); i ++){
        i * i;
    }
    tm2 = clock();
    tm = ((double)(tm2 - tm1)) / CLOCKS_PER_SEC;
    printf("time = %f ms\n", tm * 1000);
    return 0;
}
