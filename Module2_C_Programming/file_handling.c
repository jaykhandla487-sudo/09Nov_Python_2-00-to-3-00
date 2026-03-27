#include <stdio.h>

int main() {
    FILE *fp;
    char text[100];

    fp = fopen("sample.txt", "w");

    printf("Enter text: ");
    scanf("%s", text);

    fprintf(fp, "%s", text);

    fclose(fp);

    fp = fopen("sample.txt", "r");

    fscanf(fp, "%s", text);

    printf("File content: %s", text);

    fclose(fp);

    return 0;
}