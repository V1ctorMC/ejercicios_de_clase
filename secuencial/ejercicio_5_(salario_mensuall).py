#Este programa calcula tu salario mensual
print("¿Cuanto ganas por hora?")
Salarioporhora = int(input())
print("¿Cuantas horas trabajas a la semana?")
horasporsemana = int(input())
salariomensual = horasporsemana * Salarioporhora * 4
print("Tu salario mensual es de", salariomensual,"euros")
