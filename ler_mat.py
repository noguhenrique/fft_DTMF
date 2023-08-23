#------------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

#------------------------------------------------------------------------------
# Gráfico do sinal.
def plotdata(data):
    
    frequencia_amostragem = 22050
    t = np.array(range(len(data)))/frequencia_amostragem
    plt.plot(t, data, label='Sinal')
    plt.title('Sinal de DTMF com ruido')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.grid(True)
    plt.show()

#------------------------------------------------------------------------------
if __name__ == '__main__':

    # O arquivo deve estar na mesma pasta.
    # O vetor com os dados é o ydata
    # A frequencia de amostragem do sinal é 22050 Hz.
    mat_file = "ydata_grupo2_2023.mat" # Substituir pelo arquivo a ser lido.

    try:
        #Carrega os dados do arquivo .mat
        mat_data = np.loadtxt(mat_file)
        plotdata(mat_data)

    except Exception as e:
        print("ERRO:", e)
