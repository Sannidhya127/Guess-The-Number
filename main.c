#include <stdio.h>

int main () {
   int ret;
   char oldname[] = "init.py";
   char newname[] = "main.py";
   
   ret = rename(oldname, newname);
	
   if(ret == 0) {
      printf("File renamed successfully");
   } else {
      printf("Error: unable to rename the file");
   }
   
   return(0);
}