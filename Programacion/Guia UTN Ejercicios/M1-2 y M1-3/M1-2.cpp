#include <iostream>
using namespace std;

void obtener_fecha(int pf[])
{  
    system("cls");
    cout<< "ingrese el dia (DD)"<< endl;
    cin>> pf[0];    
    cout<< "ingrese el mes (MM)"<< endl;
    cin>> pf[1];
    cout<< "ingrese el ano (AAAA)"<< endl;
    cin>> pf[2];
    return;
}

int codificar_fecha(int F[])
{
    int dia = F[0];
    int mes = F[1] * 100;
    int año = F[2] * 10000;
    return (dia + mes + año);
}

int main()
{
    int fecha[3];

    obtener_fecha(fecha);

    system("cls");
    cout<< "Fecha ingresada:"<< endl
    << "dia: "<< fecha[0]<< endl
    << "mes: "<< fecha[1]<< endl
    << "ano: "<< fecha[2]<< endl
    << endl<< "codigo (AAAAMMDD): "<< codificar_fecha(fecha)<< endl<< endl;

    return 0;
}