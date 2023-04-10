#include <stdlib.h>
#include <stdio.h>

#define BOUND 128
int array1[BOUND] = {0};

void __attribute__((noinline))
victim_function(size_t arr_len, int *arr) {
    for (size_t i = 0; i < arr_len; ++i) {
        int index = arr[i];
        if (index < BOUND) {
            array1[index] ++;
        }
    }
}

int main(int argc, char **argv) {
    if (argc < 2) {
        printf("warning: no input file\n");
        exit(-1);
    } else if (argc > 2) {
        printf("warning: too much inputs\n");
    }

    char* filename = argv[1];
    FILE *f = fopen(filename, "r");
    if (!f) {
        printf("error: unable to open input file %s\n", filename);
        exit(-1);
    }

    int *arr;
    char word[128];
    if (fgets(word, 128, f) == NULL) {
        printf("warning: no contents in file %s\n", filename);
        exit(-1);
    }
    size_t arr_len = strtoul(word, NULL, 10);
    printf("arr_len: %zu\n", arr_len);

    /* read at most arr_len indexes into arr */
    arr = malloc(arr_len * sizeof(int));
    size_t i = 0;
    for (; i < arr_len && fgets(word, 128, f) != NULL; ++i) {
        arr[i] = strtol(word, NULL, 10);
    }
    arr_len = i;
    for (i = 0; i < arr_len; ++i)
        printf("%d ", arr[i]);
    printf("\n");


    fclose(f);

    victim_function(arr_len, arr);
    for (i = 0; i < BOUND; ++i)
        printf("%d ", array1[i]);
    printf("\n");

    free(arr);
    return 0;
}
