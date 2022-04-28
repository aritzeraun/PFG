from __future__ import absolute_import
from __future__ import print_function

import csv

from Rake_Analysis import rake
import io
from os import listdir


def writeKeyFile(downloadedFilesFolder, keyFilePath, rake_object):
    f = open(keyFilePath, "w+", encoding="iso-8859-1")
    for file in listdir(downloadedFilesFolder):
        if file.endswith('.txt'):
            sample_file = io.open(downloadedFilesFolder + file, 'r', encoding="iso-8859-1")
            text = sample_file.read()
            keywords = rake_object.run(text)
            i = 0
            enc = False
            try:
                f.write(file + ";")
                for key in keywords:
                    if i == 0:
                        f.write(key[0])
                        enc = True
                    if 0 < i < 15:
                        print(key[0])
                        f.write("," + key[0])
                    i = i + 1
            except Exception:
                print("error")
            if enc:
                f.write("\n")
    f.flush()
    f.close()


def writeKeyListFile(downloadedFilesFolder, keyListFilePath, rake_object):
    f = open(keyListFilePath, "w+", encoding="iso-8859-1")

    for file in listdir(downloadedFilesFolder):
        if file.endswith('.txt'):
            sample_file = io.open(downloadedFilesFolder + file, 'r', encoding="iso-8859-1")
            text = sample_file.read()
            keywords = rake_object.run(text)
            i = 0
            enc = False
            try:
                for key in keywords:
                    if i < 15:
                        print(key[0])
                        f.write(key[0] + "\n")
                    i = i + 1
            except Exception:
                print("error")
            if enc:
                f.write("\n")
    f.flush()
    f.close()


def writeUniqueKeysFile(downloadedFilesFolder, uniqueKeyListFilePath, rake_object, wordsDict):
    f = open(uniqueKeyListFilePath, "w+", encoding="iso-8859-1")
    for file in listdir(downloadedFilesFolder):
        if file.endswith('.txt'):
            sample_file = io.open(downloadedFilesFolder + file, 'r', encoding="iso-8859-1")
            text = sample_file.read()
            keywords = rake_object.run(text)
            i = 0
            enc = False
            for key in keywords:
                try:
                    clave = key[0]
                    if i == 0:
                        if clave in wordsDict:
                            f.write(wordsDict[clave])
                            i = i + 1
                            enc = True
                    if i > 0:
                        if clave in wordsDict:
                            f.write("," + wordsDict[clave])
                        i = i + 1
                except Exception:
                    print("error")
            if enc:
                f.write("\n")
    f.flush()
    f.close()


def writeMatrix(downloadedFilesFolder, matrixAnalysisFile, rake_object):
    item_list = []
    seen = set(item_list)
    for file in listdir(downloadedFilesFolder):
        sample_file = io.open(downloadedFilesFolder + file, 'r+', encoding="iso-8859-1")
        text = sample_file.read()
        keywords = rake_object.run(text)
        i = 0
        for key in keywords:
            if key[0] not in seen and i < 15:
                seen.add(key[0])
            i = i + 1
    print(seen)
    f = open(matrixAnalysisFile, "w+", encoding="iso-8859-1")
    for keys in seen:
        f.write(str(keys) + ",")
    f.write("doc\n")
    for file in listdir(downloadedFilesFolder):
        sample_file = io.open(downloadedFilesFolder + file, 'r+', encoding="iso-8859-1")
        text = sample_file.read()
        keywords = rake_object.run(text)
        for word in seen:
            valor = 0
            for key in keywords:
                if word == key[0]:
                    valor = key[1]
            f.write(str(valor) + ",")
        f.write(file + "\n")
    f.flush()
    f.close()


def documentStandardization(finalDocumentPath, matrixAnalysisFile):
    finalAnalysisDocument = open(finalDocumentPath, "w+", encoding="iso-8859-1")
    i = 0
    for linea in open(matrixAnalysisFile, "r", encoding="iso-8859-1"):
        if i == 0:
            finalAnalysisDocument.write(linea)
        else:
            values = linea.split(",")
            sumValue = 0
            for valor in range(0, len(values) - 1):
                sumValue = sumValue + float(values[valor])
            for valor in range(0, len(values) - 1):
                writingValue = 0
                if sumValue != 0:
                    writingValue = float(values[valor]) / sumValue
                finalAnalysisDocument.write(str(writingValue) + ",")
            finalAnalysisDocument.write(values[len(values) - 1])
        i = i + 1
    finalAnalysisDocument.flush()
    finalAnalysisDocument.close()


def writeRelationCSV(relationKeyListPath, relationData):

    with open(relationKeyListPath, 'w+', encoding='iso-8859-1') as f:
        writer = csv.writer(f)

        for item in relationData:
            writer.writerow(item)

        f.close()


def readCSVFile(keyListFilePath):
    wordsDictionary = {}

    for linea in open(keyListFilePath, "r", encoding="iso-8859-1"):
        readLine = linea.split(",")
        clave = readLine[0]
        if len(readLine) > 1:
            valor = str(readLine[1]).replace('\n', '')
            valor = valor.rstrip()
            if valor != "":
                wordsDictionary[clave] = valor
    return wordsDictionary


def readKeysListFile(path):
    WordDictionary = []

    for linea in open(path, "r", encoding="iso-8859-1"):
        WordDictionary.append(str(linea).replace('\n', ''))

    return WordDictionary


def writeListKey(downloadedFilesFolder, pathKeysFile, stopPath, min_char_length, min_phrase_freq_adj,
                 min_keyword_frequency):

    rake_object = rake.Rake(stopPath, min_char_length=min_char_length, min_keyword_frequency=min_phrase_freq_adj,
                            min_phrase_freq_adj=min_keyword_frequency)
    writeKeyListFile(downloadedFilesFolder, pathKeysFile, rake_object)
    # writeKeyFile(downloadedFilesFolder, pathKeysFile, rake_object)
    keysArray = readKeysListFile(pathKeysFile)
    return keysArray


def allAnalysis(keyWordsFile, downloadedFilesFolder, uniqueKeysFilePath, stopPath, min_char_length, min_phrase_freq_adj,
                min_keyword_frequency):
    rake_object = rake.Rake(stopPath, min_char_length=min_char_length, min_keyword_frequency=min_phrase_freq_adj,
                            min_phrase_freq_adj=min_keyword_frequency)
    wordsDict = readCSVFile(keyWordsFile)
    writeUniqueKeysFile(downloadedFilesFolder, uniqueKeysFilePath, rake_object, wordsDict)
    # writeMatrix(downloadedFilesFolder, matrixAnalysisFile, rake_object)
    # documentStandardization(finalDocumentPath, matrixAnalysisFile)
