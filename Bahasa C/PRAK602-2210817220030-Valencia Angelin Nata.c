#include <stdio.h>
int main(){
  int ruangan, zetsu, j;
  scanf("%d", &ruangan);
  int matrix[ruangan];
    for (j = 0; j < ruangan; j++) {
      scanf("%d", &zetsu);
      matrix[j] = zetsu;
  }
      for (j = 0; j < ruangan; j++) {
        printf("%d ", matrix[j] * (j + 1));
    }printf("\n");
}
