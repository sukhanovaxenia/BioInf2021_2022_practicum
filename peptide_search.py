#!usr/bin/env/python
# coding: utf-8
# In[ ]:

from argparse import ArgumentParser
from Bio import SeqIO
import os
import sys

parser = ArgumentParser()

parser.add_argument("-p",
        metavar = "STRING",
        type = str,
        help = "peptides sequences")

parser.add_argument("-f",
        metavar = "STRING",
        type = str,
        help = "hypothesized proteins")

args = parser.parse_args()


fPEP = args.p
fFA = args.f


peptides_in = SeqIO.parse(fPEP, 'fasta')
proteins_in = SeqIO.parse(fFA, 'fasta')
peptides, pep_des = [], []
proteins, prot_des = [], []
for i in peptides_in:
    peptides.append(str(i.seq))
    pep_des.append(str(i.id))
for j in proteins_in:
    proteins.append(str(j.seq))
    prot_des.append(str(j.id))
cut = []
with open('local_annot.txt', 'w') as annot, open('prot_local.fa', 'w') as localized:
    for i,prot in enumerate(proteins):
        for j,pep in enumerate(peptides):
            if pep in prot and prot_des[i] not in cur:
                cur.append(prote_des[i])
                localized.write(">"+prot_des[i] + '|' + pep_des[j] + '\n' + prot+'\n')
                annot.write(prot_des[i] + '\t' + pep_des[j]+ '\n')

