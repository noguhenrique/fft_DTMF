import numpy as np
#import matplotlib.pyplot

#Carrega os dados do arquivo .mat
mat_data = np.loadtxt("ydata_grupo3_2023.mat")
#print (mat_data)

# Extrair os dados do sinal e a frequência de amostragem
signal = mat_data
sampling_rate = 22050  # Frequência de amostragem de 22,05 kHz

# Parâmetros para a divisão dos dígitos
digit_duration = 0.04  # 40 ms
digit_interval = 0.1   # 100 ms

# Número de pontos da FFT
samples_per_digit = int(sampling_rate * digit_duration)
fft_size = int(2 ** np.ceil(np.log2(samples_per_digit)))

# Função para decodificar os dígitos DTMF
def decode_dtmf(signal_chunk):
    # Aplicar FFT no sinal
    fft_result = np.fft.fft(signal_chunk, fft_size)
    
    # Frequências correspondentes aos dígitos DTMF
    dtmf_freqs = {
    '1': (697, 1209),
    '2': (697, 1336),
    '3': (697, 1477),
    '4': (770, 1209),
    '5': (770, 1336),
    '6': (770, 1477),
    '7': (852, 1209),
    '8': (852, 1336),
    '9': (852, 1477),
    '0': (941, 1336),
}
    
    max_digit = None
    max_corr = 0
    
    # Encontrar o dígito com a maior correlação
    for digit, freqs in dtmf_freqs.items():
        freq1, freq2 = freqs
        index1 = int(freq1 * fft_size / sampling_rate)
        index2 = int(freq2 * fft_size / sampling_rate)
    
        corr = np.abs(fft_result[index1]) + np.abs(fft_result[index2])
    
        if corr > max_corr:
            max_corr = corr
            max_digit = digit
    
    return max_digit

# Dividir o sinal em trechos de dígitos + intervalos
signal_length = len(signal)
digits = []
start = 0
counter = 1 

while start + digit_duration * sampling_rate <= signal_length:
    signal_chunk = signal[int(start):int(start + digit_duration * sampling_rate)]
    decoded_digit = decode_dtmf(signal_chunk)
    digits.append(decoded_digit)

    print(f"• Valor do dígito {counter}: {decoded_digit}.")
    counter += 1
    start += (digit_duration + digit_interval) * sampling_rate


# Juntar os dígitos decodificados em um número de telefone
phone_number = ''.join(digits)
# Formatar o número de telefone
formatted_phone_number = f"({phone_number[:2]}) {phone_number[2:6]}-{phone_number[6:]}"
# Imprimir o número de telefone no formato desejado
print("Número de telefone decodificado:", formatted_phone_number)
