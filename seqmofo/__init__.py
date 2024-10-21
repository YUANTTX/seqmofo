#!/usr/bin/python
# -*- coding=utf8 -*-
"""
# @Author : YHJ
# @Created Time : 2023-06-13 21:29:15
# @Description : 
"""


# 导入模块的函数（公共接口）
# from .module1 import function1, Class1
# from .module2 import function2


# 导入子模块
from .fasta import fasta
from .fastq import fastq
__all__ = ['fasta', 'fastq']

# seqmofo/__init__.py

# # 导入子模块
# from .fasta.fasta import fastaclass
# from .bam.bam import BamClass  # 假设bam.py中有一个BamClass类
# from .bed.bed import BedClass  # 假设bed.py中有一个BedClass类
# from .fastq.fastq import FastqClass  # 假设fastq.py中有一个FastqClass类
# from .gff.gff import GffClass  # 假设gff.py中有一个GffClass类
# from .gtf.gtf import GtfClass  # 假设gtf.py中有一个GtfClass类
# from .sam.sam import SamClass  # 假设sam.py中有一个SamClass类

# # 定义公开接口
# __all__ = [
#     'fastaclass',
#     'BamClass',
#     'BedClass',
#     'FastqClass',
#     'GffClass',
#     'GtfClass',
#     'SamClass',
# ]

# 定义包的版本
__version__ = "1.0.0"


# 可选：定义包的公开接口
# __all__ = ['function1', 'Class1', 'function2', 'submodule1']


# 初始化配置参数
CONFIG_PARAM = "example"


# 可选：包级别的初始化代码
print("my_package initialized")
