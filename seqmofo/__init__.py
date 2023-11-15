#!/usr/bin/python
# -*- coding=utf8 -*-
"""
# @Author : YHJ
# @Created Time : 2023-06-13 21:29:15
# @Description : 
"""

# 模块版本
__version__ = "1.0.2"

# 预加载模块
from .fasta import fasta
from .fastq import fastq

# 初始化配置参数
CONFIG_PARAM = "example"

# 初始化代码
print("Initializing my package!")