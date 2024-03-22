import threading
import time

#Simulador de um sistema de controle de estacionamento
#Feito por Luiz Felipe e Anthony Araújo

vagas_total = 10
vagas_ocupadas = 0
carros_entraram = 0
carros_sairam = 0
vagas_lock = threading.Lock()
continuar_executando = True

def entrada_carros():
    global vagas_ocupadas, carros_entraram
    while continuar_executando:
        time.sleep(1)
        vagas_lock.acquire()
        if vagas_ocupadas < vagas_total:
            vagas_ocupadas += 1
            carros_entraram += 1
            print(f'Carro entrou, vagas ocupadas: {vagas_ocupadas}')
        vagas_lock.release()

def saida_carros():
    global vagas_ocupadas, carros_sairam
    while continuar_executando:
        time.sleep(1.5)
        vagas_lock.acquire()
        if vagas_ocupadas > 0:
            vagas_ocupadas -= 1
            carros_sairam += 1
            print(f'Carro saiu, vagas ocupadas: {vagas_ocupadas}')
        vagas_lock.release()

def parar_contagem():
    global continuar_executando
    time.sleep(10)
    continuar_executando = False

thread_entrada = threading.Thread(target=entrada_carros)
thread_saida = threading.Thread(target=saida_carros)
thread_temporizador = threading.Thread(target=parar_contagem)

thread_entrada.start()
thread_saida.start()
thread_temporizador.start()

thread_temporizador.join()
print(f'Total de carros que entraram: {carros_entraram}')
print(f'Total de carros que saíram: {carros_sairam}')
print(f'Vagas disponíveis: {vagas_total - vagas_ocupadas}')

#Sistemas Operacionais ADS - IFMA
