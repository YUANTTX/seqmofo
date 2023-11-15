#!/bin/python
# -*- coding=utf-8 -*-
'''
@Author : YHJ
@Created Time : 2023/11/15 15:17:39
@Description :
'''


class fastaclass(object):
    # 类属性
    dnanut = {'A', 'T', 'G', 'C'}
    rnanut = {'A', 'U', 'G', 'C'}

    # 实例属性（特殊的实例方法）
    def __init__(self, seq) -> None:
        fadict = {}
        faseq = open(seq, 'r', encoding="UTF-8")
        for line in faseq:
            if line.startswith(">"):
                name = line.strip("\n >")
                fadict[name] = ""
            else:
                fadict[name] = fadict[name] + line.strip("\n ")
        faseq.close()
        self.seq = fadict

    # 实例方法
    def names(self, num=10):
        seqkey = list(self.seq.keys())
        return seqkey[0:num]

    def sigseqid(self, id):
        if id in self.seq.keys():
            outseq = ">" + str(id) + "\n" + self.seq.get(id,None)
            return outseq.strip("\n ")
        else:
            return f"No this id: {id}"

    def sigseqnum(self, num=0):
        num = num if num == 0 else num - 1
        if num <= len(self.seq):
            seqkey = list(self.seq.keys())[num]
            outseq = ">" + str(seqkey) + "\n" + self.seq.get(seqkey,None)
            return outseq.strip("\n ")
        else:
            return "out of range"

    def head(self, num=5):
        num = 1 if num <= 0 else num
        seqkey = list(self.seq.keys())[:num]
        outseq = ""
        for i in seqkey:
            outseq = outseq + ">" + str(i) + "\n" + self.seq.get(i,None) + "\n"
        return outseq.strip("\n ")

    def tail(self, num=5):
        num = 1 if num <= 0 else num
        seqkey = list(self.seq.keys())[-num:]
        outseq = ""
        for i in seqkey:
            outseq = outseq + ">" + str(i) + "\n" + self.seq.get(i,None) + "\n"
        return outseq.strip("\n ")

    # 类的方法
    @classmethod
    def fet(cls):
        pass

    # 类静态方法，可以操作对象以外的数据
    @staticmethod
    def gcpct(seq: str):
        seq = seq.upper()
        alen = len(seq)
        gcsum = sum([seq.count("G"), seq.count("C")])
        return round(gcsum * 100 / alen, 2)

if __name__ == '__main__':
    fadir = '/home/yuanhj/RD/format/fasta/otus.multi.fa'
    faclass = fastaclass(fadir)
    faclass.names()
    print(faclass.sigseqid("OTU_1"))
    faclass.sigseqnum(60000)
    print(faclass.head(1))
    print(faclass.tail(1))
    faclass.gcpct(faclass.head(10000))
