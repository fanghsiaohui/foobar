#include <stdio.h>

int main(){
    int n, m;
    scanf("%d %d", &n, &m);

    int prime =1;
    int sum = 0;
    int x = 2;
    int i = 1;
    while (i <= m){
        sum += (i >= n) * prime * x;
        prime = 1;
        x ++;
        for (int j = 2; j < x; j++){
            if (x % j ==0){
                prime = 0;
                break;
            }
        }
        i += prime;
    }
    printf("%d\n", sum);
    return 0;
}

