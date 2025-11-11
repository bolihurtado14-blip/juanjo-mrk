# guia de implementos del chatbot, supervisado
pip install scikit-learn
pip install numpy
pip install gym==0.26.2
pip install gym-notices
pip install scikit-learn numpy gym==0.26.2 gym-notices
pip install nltk

crear el archivo setup_nltk.py
```
import nltk


try:
    nltk.download('punkt')
    print("NLTK punkt descargado correcatamente")
    except Exception as e:
        print("Erros durante la descarga:",e)

```
python setup_nltk.py