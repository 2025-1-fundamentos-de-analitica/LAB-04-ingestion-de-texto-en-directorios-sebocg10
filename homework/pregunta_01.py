# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

"""
La información requerida para este laboratio esta almacenada en el
archivo "files/input.zip" ubicado en la carpeta raíz.
Descomprima este archivo.

Como resultado se creara la carpeta "input" en la raiz del
repositorio, la cual contiene la siguiente estructura de archivos:


```
train/
    negative/
        0000.txt
        0001.txt
        ...
    positive/
        0000.txt
        0001.txt
        ...
    neutral/
        0000.txt
        0001.txt
        ...
test/
    negative/
        0000.txt
        0001.txt
        ...
    positive/
        0000.txt
        0001.txt
        ...
    neutral/
        0000.txt
        0001.txt
        ...
```

A partir de esta informacion escriba el código que permita generar
dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
del repositorio.

Estos archivos deben tener la siguiente estructura:

* phrase: Texto de la frase. hay una frase por cada archivo de texto.
* sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
    o "neutral". Este corresponde al nombre del directorio donde se
    encuentra ubicado el archivo.

Cada archivo tendria una estructura similar a la siguiente:

```
|    | phrase                                                                                                                                                                 | target   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
|  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
|  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
|  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
|  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
```


"""

import os
import zipfile
import pandas as pd

def extract_zip(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

def read_files_in_directory(directory):
    data = []
    for sentiment in ['negative', 'neutral', 'positive']:
        sentiment_path = os.path.join(directory, sentiment)
        for filename in os.listdir(sentiment_path):
            if filename.endswith('.txt'):
                file_path = os.path.join(sentiment_path, filename)
                with open(file_path, 'r', encoding='utf-8') as file:
                    phrase = file.read().strip()
                    data.append({'phrase': phrase, 'sentiment': sentiment})
    return data

def clean_data(data):
    # Remove special characters and extra spaces
    data['phrase'] = data['phrase'].str.replace('[^\w\s]', '', regex=True)
    data['phrase'] = data['phrase'].str.strip()
    return data

def save_to_csv(data, output_path):
    df = pd.DataFrame(data)
    df.to_csv(output_path, index=False)

def pregunta_01():

    # Extract zip file
    extract_zip('files/input.zip', 'files')

    # Read train and test data
    train_data = read_files_in_directory('files/input/train')
    test_data = read_files_in_directory('files/input/test')

    train_data = pd.DataFrame(train_data)
    test_data = pd.DataFrame(test_data)

    train_data = clean_data(train_data)
    test_data = clean_data(test_data)

    train_data.rename(columns={'sentiment': 'target'}, inplace=True)
    test_data.rename(columns={'sentiment': 'target'}, inplace=True)


    os.makedirs('files/output', exist_ok=True)
    save_to_csv(train_data, 'files/output/train_dataset.csv')
    save_to_csv(test_data, 'files/output/test_dataset.csv')

pregunta_01()