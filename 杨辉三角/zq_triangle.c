#include <stdio.h>
#include <stdlib.h>

//#define MAX_DIGIT  1000000000
#define INT_ARRAY_LEN  36

typedef unsigned long long uint_64;
void free_p(uint_64 **p)
{
    if (p == NULL)
        return;
    free(*p);
    *p = NULL;
}

void free_p_plus(int ***p, int m)
{
    if (p == NULL)
        return;
    for (int i = 0; i <= m; i++)
    {
        free((*p)[i]);
        (*p)[i] = NULL;
    }
    free(*p);
    *p = NULL;
}

void add(int **p, int  **new_p, int j)
{
    if (p == NULL || new_p == NULL)
        return;
    int i, sum;
    for (i = 0; i < INT_ARRAY_LEN; i++ )
    {
        sum = p[j][i] + p[j-1][i];

        if ( sum >= 10)
        {
            new_p[j+1][i] += 1;
            sum = sum - 9;
        }
        new_p[j][i] = sum;
    }

}

void exchange(int  *p, int  *new_p)
{
    if (p == NULL || new_p == NULL)
        return;
    for (int i = 0; i < INT_ARRAY_LEN; i++ )
    {
        p[i] = new_p[i];
    }

}

void get_n_plus(const int m)
{
    int i, j, k, l, index, mid;
    int **p = (int **)malloc(sizeof(int *) * (m + 1));
    int  **new_p = (int **)malloc(sizeof(int *) * (m/2 + 1));

    for (i = 0; i <= m; i++)
    {
        p[i] = (int *)malloc(sizeof(int) * INT_ARRAY_LEN);
        for (int j = 0; j < INT_ARRAY_LEN; j++)
        {
            p[i][j] = 0;
        }
    }
    for (i = 0; i <= m/2; i++)
    {
        new_p[i] = (int  *)malloc(sizeof(int) * INT_ARRAY_LEN);
        for (int j = 0; j < INT_ARRAY_LEN; j++)
        {
            new_p[i][j] = 0;
        }
    }  
    

    p[0][0]= 1;
    p[1][0] = 1;
    new_p[0][0] = 1;

    for (i = 2; i <= m; i++)
    {

        mid = i / 2 ;
        for (j = 1; j <= mid; j++)
        {
            add(p, new_p, j);
        }
 
        index = 0;
        for (k = i; k > mid; k--)
        {
            exchange(p[k], new_p[index]);
            exchange(p[index], new_p[index]);
            index++;
        }

        if (i % 2 == 0)
            exchange(p[mid], new_p[mid]);

        
    }

    free_p_plus(&new_p, m/2);

    for (i = 0; i <= m; i++)
    {
        for (j = INT_ARRAY_LEN; j >= 0; j--)
        {
            if (p[i][j])
                break;   
        }
        for (; j>=0; j--)
            printf("%d", p[i][j]);
        printf("   ");
    }
    printf("\n");

    free_p_plus(&p, m);

}

void get_n(const int m)
{
    uint_64 *p = (uint_64 *)malloc(sizeof(uint_64) * (m + 1));
    int i, j, k, index, mid;
    uint_64 *new_p = (uint_64 *)malloc(sizeof(uint_64) * (m/2 + 1));
    p[0] = 1;
    p[1] = 1;
    new_p[0] = 1;
    for (i = 2; i <= m; i++)
    {
        mid = i / 2 ;
        for (j = 1; j <= mid; j++)
        {
            new_p[j] = p[j] + p[j-1];
        }
 
        index = 0;
        for (k = i; k > mid; k--)
        {
            p[index] = new_p[index];
            p[k] = new_p[index];
            index++;
        }
        if (i % 2 == 0)
            p[mid] = new_p[mid];

        
    }
    free_p(&new_p);
    for (i = 0; i <= m; i++)
    {
        printf("%lld  ", p[i]);
    }
    printf("\n");
    free_p(&p);

}


int main()
{
    // get_n(1000);
    get_n_plus(1);
    // get_n_plus(2);
    // get_n_plus(3);
    // get_n_plus(4);
    return 0;
}