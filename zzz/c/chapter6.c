#include <stdio.h>

int main(){
    int a, b;
    scanf("%d/%d", &a, &b);
    int bits = 200;
    int x[bits];
    int i = 0;
    for (i = 0; i < bits; i ++){
        x[i] = 0;
    }
    int validBits = 0;
    int t;
    t = a * 10;
    for (i = 0; i < bits; i ++){
        x[i] = t / b;
        t = t % b * 10;
        validBits ++;
        if (t == 0) break;
    }
    printf("0.");
    for (i = 0; i < validBits; i++){
        printf("%d", x[i]);
    }
    printf("\n");
    return 0;
}
