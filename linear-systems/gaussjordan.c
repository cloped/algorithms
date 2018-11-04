// Based on http://www-di.inf.puc-rio.br/~tcosta/cap2.htm
#include <stdio.h>

void printMatrix(double matrix[3][4]) {
    printf("------------------------------------\n");
    for(int i = 0; i < 3; ++ i) {
        for(int j = 0; j < 3; ++ j) {
            printf("%.2lf\t", matrix[i][j]);
        }
        printf(": %.2lf\n", matrix[i][3]);
    }
    printf("------------------------------------\n");
}

void gaussJordanElimination(double matrix[3][4]) {
    double pivot, mLine;

    // Below diagonal
    for(int i = 0; i < 3; ++i) {
        pivot = matrix[i][i];
        // Calculating m for each line below
        for(int m = i+1; m < 3; ++m) {
            mLine = matrix[m][i] / pivot;
            // Calculating new lines
            for(int n = i; n < 4; ++n) {
                matrix[m][n] = matrix[m][n] - (mLine * matrix[i][n]);
            }
        }
    }

    // Upper Diagonal
    for(int i = 2; i >= 0; --i) {
        pivot = matrix[i][i];
        // Calculating m for each line above
        for(int m = i-1; m >= 0; --m) {
            mLine = matrix[m][i] / pivot;
            // Calculating new lines
            for(int n = i; n < 4; ++n) {
                matrix[m][n] = matrix[m][n] - (mLine * matrix[i][n]);
            }
        }
    }

    printMatrix(matrix);
}

int main() {
    /**
     *  Slide example:
     *   x1 + x2 + 2x3 =  4
     *  2x1 - x2 -  x3 =  0
     *   x1 - x2 -  x3 = -1
     */
    double example[3][4] = {
        { 1,  1,  2,  4},
        { 2, -1, -1,  0},
        { 1, -1, -1, -1}
    };

    printf("Gauss-Jordan elimination of slide example:\n");
    gaussJordanElimination(example);
    
    /**
     *  Exercise:
     *  3x1 + 2x2 + 4x3 =  1
     *   x1 +  x2 + 2x3 =  2
     *  4x1 + 3x2 - 2x3 =  3
     */
    double exercise1[3][4] = {
        { 3,  2,  4,  1},
        { 1,  1,  2,  2},
        { 4,  3, -2,  3}
    };

    printf("\nGauss-Jordan elimination of slide exercise1:\n");
    gaussJordanElimination(exercise1);

    return 0;
}
