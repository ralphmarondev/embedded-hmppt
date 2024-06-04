#include <stdio.h>
#include <unistd.h> // For sleep function

int main() {
    FILE *file;
    int variable2;

    file = fopen("hello.txt", "r");

    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    fscanf(file, "%d\n", &variable2);
    fclose(file);

    printf("Variable 2: %s\n", variable2);

    sleep(2);

    return 0;
}
