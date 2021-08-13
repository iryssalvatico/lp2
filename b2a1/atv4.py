dicio = {'UUU':'Fenil-alanina', 'UUC':'Fenil-alanina',
    'UUA':'Leucina', 'UUG':'Leucina','CUU':'Leucina', 'CUC':'Leucina','CUA':'Leucina', 'CUG':'Leucina',
    'AUU':'Isoleucina', 'AUC':'Isoleucina','AUA':'Isoleucina','AUG':'start codon',
    'GUU':'Valina', 'GUG':'Valina','GUA':'Valina', 'GUC':'Valina',
    'UCU':'Serina', 'UCC':'Serina','UCA':'Serina','UCG':'Serina',
    'CCU':'Prolina','CCC':'Prolina', 'CCA':'Prolina','CCG':'Prolina',
    'ACU':'Treonina','ACC':'Treonina', 'ACA':'Treonina','ACG':'Treonina',
    'GCU':'Alanina','GCC':'Alanina', 'GCA':'Alanina','GCG':'Alanina',
    'UAU':'Tirosina','UAC':'Tirosina', 'UAA':'Stop codon','UAG':'Stop codon',
    'CAU':'Histidina', 'CAC':'Histidina','CAA':'Glutamina','CAG':'Glutamina',
    'AAU':'Asparagina','AAC':'Asparagina','AAA':'Lisina', 'AAG':'Lisina',
    'GAU':'Acido aspartico', 'GAC':'Acido aspartico','GAA':'Acido Glutamico', 'GAG':'Acido Glutamico',
    'UGU':'Cysteine','UGC':'Cysteine', 'UGA':'Stop codon','UGG':'Tryptophan',
    'CGU':'Arginina','CGC':'Arginina', 'CGA':'Arginina','CGG':'Arginina',
    'AGU':'Serina', 'AGC':'Serina','AGA':'Arginina', 'AGG':'Arginina',
    'GGU':'Glicina', 'GGC':'Glicina','GGA':'Glicina','GGG':'Glicina'}
from os import replace
with open('bases-lp2', 'r') as arq: 
    arquivo = arq.readlines()
print (arquivo)
i=0
while i < len(arquivo):
    z = arquivo[i]
    k1 = z.replace("A","u")
    k2 = k1.replace("T","a")
    k3 = k2.replace("G","c")
    k4 = k3.replace("C","g")
    print('\n')
    print(('Linha'),(i+1),('inicial: '),(z))
    print(('Transcrição da linha final '),(i+1),(':'),(k4.upper()))
    k4 = k4.upper()
    j=0
    print('Aminoacidos que serão sintetizados após o start codon:')
    for j in range(3, len(k4), 1):
        v1= ''
        v1 = k4[j-3]
        v1 += k4[j-2]
        v1 += k4[j-1]
        if dicio[v1]=='start codon':
            k=j+1
            print (dicio[v1])
            for j in range(k, len(k4), 1):
                v1= ''
                v1 = k4[j-3]
                v1 += k4[j-2]
                v1 += k4[j-1]
                if (dicio[v1])=='Stop codon':
                    break
                else:
                    print (dicio[v1])
            break
    i=i+1