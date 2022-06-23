#include <stdio.h>
#include <string.h>
 
struct emp 
{
           int id;
           char name[50];
           float salary;
};
 
void func(struct emp *rec);
 
int main() 
{
          struct emp rec;
 
          rec.id=115;
          strcpy(rec.name, "Siddhi");
          rec.salary = 25000;
 
          func(&rec);
          return 1;
}
 
void func(struct emp *rec)
{
          printf(" Employee Id : %d \n", rec->id);
          printf(" Employee Name : %s \n", rec->name);
          printf(" Employee Basic Salary : %.2f \n", rec->salary);
}