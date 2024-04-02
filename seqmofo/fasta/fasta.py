#!/bin/python
# -*- coding=utf-8 -*-
'''
@Author : YHJ
@Created Time : 2023/11/15 15:17:39
@Description :
'''



class fastaclass(object):
    """ 类属性 """
    dnanut = {'A', 'T', 'G', 'C'}
    rnanut = {'A', 'U', 'G', 'C'}
    __dnaref = {"A":"T", "G":"C", "T":"A", "C":"G"}

    # 实例属性
    def __init__(self, seq) -> None:
        """ 特殊的实例方法 """
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

    # 类方法, 类方法可以访问类的属性和方法，但不能直接访问实例对象的属性
    @classmethod
    def getdnanut(cls):
        """
        获取类属性
        """
        return cls.dnanut

    @classmethod
    def getdnaref(cls):
        """
        获取私有的类属性
        """
        return cls.__dnaref

    # 普通方法, 普通方法的第一个参数通常是 self，表示实例对象自身。
    def names(self, num=10):
        """获取所有序列的名字"""
        seqkey = list(self.seq.keys())
        return seqkey[0:num]

    # 普通方法
    def sigseqid(self, id):
        """获取指定名字的序列"""
        if id in self.seq.keys():
            outseq = ">" + str(id) + "\n" + self.seq.get(id, None)
            return outseq.strip("\n ")
        else:
            return f"No this id: {id}"

    # 普通方法
    def sigseqnum(self, num=0):
        """获取指定序号的序列"""
        num = num if num == 0 else num - 1
        if num <= len(self.seq):
            seqkey = list(self.seq.keys())[num]
            outseq = ">" + str(seqkey) + "\n" + self.seq.get(seqkey, None)
            return outseq.strip("\n ")
        else:
            return "out of range"

    # 普通方法
    def head(self, num=5):
        """获取部分头部的序列"""
        num = 1 if num <= 0 else num
        seqkey = list(self.seq.keys())[:num]
        outseq = ""
        for i in seqkey:
            outseq = outseq + ">" + str(i) + "\n" + self.seq.get(i, None) + "\n"
        return outseq.strip("\n ")

    # 普通方法
    def tail(self, num=5):
        """获取部分尾部的序列"""
        num = 1 if num <= 0 else num
        seqkey = list(self.seq.keys())[-num:]
        outseq = ""
        for i in seqkey:
            outseq = outseq + ">" + str(i) + "\n" + self.seq.get(i, None) + "\n"
        return outseq.strip("\n ")

    # 类静态方法，可以操作对象以外的数据
    @staticmethod
    def gcpct(sequenses: str):
        """
        计算序列的GC含量
        """
        print(fastaclass.dnanut) # 引用类属性
        sequenses = sequenses.upper()
        alen = len(sequenses)
        gcsum = sum([sequenses.count("G"), sequenses.count("C")])
        return round(gcsum * 100 / alen, 2)


if __name__ == '__main__':
    # 类操作
    dir(fastaclass)
    print(fastaclass.getdnanut())
    print(fastaclass.dnanut)
    fastaclass.gcpct("TCGA")
    fastaclass.getdnaref()

    # 实例操作
    fadir = '/home/yuanhj/project/16s/16s_2024_02_28_4sample/Ana_out/3.Annotaion/uparse/otus.uparse.fa'
    faclass = fastaclass(fadir)
    dir(faclass)
    faclass.names()
    print(faclass.sigseqid("OTU_121"))
    print(faclass.sigseqnum(600))
    print(faclass.head(1))
    print(faclass.tail(1))
    faclass.gcpct(faclass.head(10000))
    print(faclass.__dnaref)
    print(faclass._faclass__dnaref)