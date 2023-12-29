#include <iostream>
using namespace std;

int main()
{
    int fecha;
    int dia;
    int mes;
    int ano;

    system("cls");
    cout<< "Ingresar fecha (AAAAMMDD)";
    cin>> fecha;
    ano = fecha/10000;
    mes = fecha/100 - ano*10000;
    dia = fecha - ano*10000 - mes*100;

    system("cls");
    cout<< "Dia: "<< dia<< endl
    << "Mes: "<< mes<< endl
    << "ano: "<< ano<< endl;
    
    return 0;
}