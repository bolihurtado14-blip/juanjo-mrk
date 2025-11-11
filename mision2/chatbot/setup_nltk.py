import nltk


try:
    nltk.download('punkt')
    print("NLTK punkt descargado correcatamente")
except Exception as e:
        print("Erros durante la descarga:",e)
