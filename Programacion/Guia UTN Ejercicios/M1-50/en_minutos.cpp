//toma horas en formato HHMM y devuelve los minutos totales

#include <iostream>
using namespace std;

int main(int hora)
{
    return (((hora/100)*60) + hora);
}