#include <stdio.h>

int main(){
    int n;
    // printf("enter a number:");
    scanf("%d", &n);

    if (n < 0){
        n = -n;
        printf("fu ");
    }
    int i;
    i = n;
    int mask = 1;
    while (i >= 10){
        mask *= 10;
        i /= 10;
    }
    int j;
    i = n;
    while (mask > 0){
        j = i / mask;
        i %= mask;
        mask /= 10;
        // printf("%d", j);
        switch (j){
            case 1: printf("yi");
                    break;
            case 2: printf("er");
                    break;
            case 3: printf("san");
                    break;
            case 4: printf("si");
                    break;
            case 5: printf("wu");
                    break;
            case 6: printf("liu");
                    break;
            case 7: printf("qi");
                    break;
            case 8: printf("ba");
                    break;
            case 9: printf("jiu");
                    break;
            case 0: printf("ling");
                    break;
        }
        if (mask > 0)
            printf(" ");
    }
    printf("\n");
    return 0;
}
