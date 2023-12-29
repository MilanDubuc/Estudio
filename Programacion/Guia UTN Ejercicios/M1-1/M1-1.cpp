#include <iostream>
using namespace std;



void ingresar_valores(int *pA, int *pB)
{
    cout<< "ingrese el valor de A"<< endl;
    cin>> *pA;
    cout<< "ingrese el valor de B"<< endl;
    cin>> *pB;
    cout<< "A vale: "<< *pA<< " ; B vale: "<< *pB<< endl;
    return;
}

void seleccionar_opcion(char *po)
{
    cout<< endl<< "Que desea hacer?"<< endl
    << "a - Suma"<< endl
    << "b - Resta"<< endl
    << "c - Multiplicacion"<< endl
    << "Elija una opcion"<< endl;
    cin>> *po;
    return;
}

int main()
{
    
    int A;
    int B;
    int resultado;
    char opcion;

    do
    {
        seleccionar_opcion(&opcion);

         switch (opcion)
        {
        case 'a':
            ingresar_valores(&A, &B);
            resultado = A + B;
            cout<< A<< " + "<< B<< " = "<< resultado<< endl;
            break;
        case 'b':
            ingresar_valores(&A, &B);
            resultado = A - B;
            cout<< A<< " - "<< B<< " = "<< resultado<< endl;
            break;
        case 'c':
            ingresar_valores(&A, &B);
            resultado = A * B;
            cout<< A<< " x "<< B<< " = "<< resultado<< endl;
            break;
        default:
            cout<< "Ingrese una opcion valida"<< endl;
            break;
        }
    }

    while (opcion != 27);  
    return 0;
}   