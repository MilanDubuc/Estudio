#include <iostream>
using namespace std;

struct infraccion
{
    int tipo;
    char motivo[30];
    int multa;
    char gravedad;
};

char menu()
{
    char opcion;
    system("cls");
    cout<< "a - Agregar infraccion"<< endl
    << "b - Terminar"<< endl;
    cin>> opcion;
    return opcion;
}

int main()
{
    infraccion lista[100];
    char op;
    op = menu();

    switch (op)
    {
        case 'a':
            system ("cls");
            for (int i=0; i<100; i++)
            {
                cout<< "Tipo de infraccion (1, 2, 3 ó 4):";
                cin>> lista[i].tipo;
                cout<< "Motivo:";
                cin>> lista[i].motivo;
                cout<< "Gravedad ('L','M','G'):";
                cin>> lista[i].gravedad;
                //agregar switch
                cout<< "Multa:"<< endl;
                cin>> lista[i].multa;
            }
            break;
        case 'b':

            break;
        default:

            break;
    }

    return 0;
}