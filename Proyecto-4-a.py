print("--- Bienvenido a pizzas Juandi ---")
dinero=float(input("¿Cuánto dinero tiene?: "))
comida=[]
total=0
queso=12
carne=14
piña=15.5
if dinero < 12:
    print("Su dinero no es suficiente para comprar ninguna pizza.")
    
else:
    print("¿Qué pizza quiere ordenar?\n(1)Queso = 12$\n(2)Carne = 14$\n(3)Piña 15.5$")
    op=int(input("Ingrese una opción de su agrado: "))
while True:    
    if op == 1:
        total+=queso
        dinero-=total
        comida.append("Pizza de queso")
        print(f"!Buena elección, su pizza de Queso estará lista pronto\nel total por el momento es de: {total}$\nLe quedan {dinero}$")
        break
    elif op==2 and dinero >= carne:
        total+=carne
        dinero-=total
        comida.append("Piza de carne")
        print(f"!Excelente elección, su pizza de carne estará lista pronto\nel total a pagar por el momento es de: {total}$\nLe quedan {dinero}$")
        break
    elif op==3 and dinero >= piña:
        total+=piña
        dinero-=total
        comida.append("Pizza de piña")
        print(f"!Incríble elección, su pizza de piña estará lista pronto\nel total a pagar por el momento es de: {total}$\nLe quedan {dinero}$")
        break
    else:
        op=int(input("Ingrese una opción válida por favor: "))
while True:
    if dinero >= 3.4:
        print("Desearía agregar algun ingrediente extra?\n(1)Si\n(2)No")
        op2=int(input("Ingrese su desición: "))
        if op2==2:
            print(f"--- RECIBO ---\n*Compra*{comida}\ntotal pagado: {total}$\ncambio: {dinero}$\n--- Vuelva Pronto ---")
            break
        else:
            champiñones=4
            maiz=3.4
            eq=5.5
            print("Estos son los ingredientes extra que puede agregar a su pizza:\n(1)Champiñones: 4$\n(2)Maíz: 3.4$\n(3)Extra queso: 5.5$\n(4)No más")
            op3=int(input("Ingrese su extra: "))
            if op3==1:
                total+=champiñones
                dinero-=champiñones
                comida.append("Champiñones")
            elif op3==2:
                total+=maiz
                dinero-=maiz
                comida.append("Maíz")
            elif op3==3:
                total+=eq
                dinero-=eq
                comida.append("Extraqueso")
            elif op==4:
                print("Imprimiendo recibo...")
                print(f"--- RECIBO ---\n*Compra*{comida}\ntotal pagado: {total}$\ncambio: {dinero}$\n--- Vuelva Pronto ---") 
                break
            else:
                op3=int(input("Ingrese una opción válida por favor: ")) 
    else:
        print("Su dinero no es suficiente para más ingredientes extra")
        print(f"--- RECIBO ---\n*Compra*{comida}\ntotal pagado: {round(total,2)}$\ny su dinero inicial era: {round(dinero+total,2)}$\nahora le quedan {round(dinero,2)}$, lo cual no es suficiente para añadir ingredientes extra.\n--- Vuelva Pronto ---") 
        break      
                
            
         

         
         
   
    
    