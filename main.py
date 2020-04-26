#! /usr/bin/env python3
"""
基于同义词词林扩展版实现上下文关系自动抽取
将上下位关系词对写入文件中中，用Tab键隔开，以（下位词，上位词）顺序写入
"""

"""
code_word  以编码为key，单词list为value的dict，一个编码有多个单词
"""
code_word={}
cilin_file='/home/hxy/task2-cilin/new_cilin.txt'
res_file='/home/hxy/task2-cilin/result.txt'
word_second_no={"Aa","Ac","Ad","Ae","Af","Ag","Ai","Aj","Ak","Al","Am","Ba","Bb","Bc"}

pairs=[]

with open(cilin_file,'r',encoding='gbk') as f:
	for line in f.readlines():
		res=line.split()
		
		#先抽取第一大类至第四大类的名词词语
		if res[0][0] >='E':
			continue

		code=res[0]	
		words=res[1:]
		code_word[code]=words
		
		if len(code)>6 and res[0][0]>'E':
			break

		#通过原子词群的编码，得到大，中，小类的编码
		if len(code)<6:	
			continue		
	
		#大类词
		word_first=code_word[code[:1]][0]
		#中类词
		word_second=code_word[code[:2]][0]
		#小类词
		word_third_set=set()
		word_third_set.update(code_word[code[:4]])
		#原子词群，对于原子词群中的第一个词段，若整个词段为同义词，由于这些词意思相同，且多存在不常用词，只保留其第一个词语;
		word_last_set=set()
		if(code[-2]=="1" and code[-1]=="="):
			word_last_set.add(code_word[code][0])
		else:
			word_last_set.update(code_word[code])
		#词群中的第一个词为整个词群的标题词，可以作为词段的上位词
		word_last_fu=code_word[code[:5]][0]
	
		
		#若中类词是非描述性的词语，一般可以作为大类词的下位词;此时可抽取到<中类词，大类词>,<小类词，中类词>上下位关系词对
		if code[:2] not in word_second_no:
			s_f=[word_second,word_first]
			if s_f not in pairs:
				pairs.append(s_f)
			for word_third in word_third_set: 		
				if word_second == word_third:
					continue
				t_s=[word_third,word_second]
				if t_s not in pairs:
					pairs.append(t_s)
		else:#否则，跳过中类词，抽取出<小类词，大类词>上下位关系词对
			for word_third in word_third_set:
				t_f=[word_third,word_first]
				if t_f not in pairs:
					pairs.append(t_f)
		#<词群词，标题词>
		for word_zi in word_last_set:
			if word_zi == word_last_fu:
				continue
			z_f=[word_zi,word_last_fu]
			if z_f not in pairs:
				pairs.append(z_f)
				

with open(res_file,'a') as o:
	for pair in pairs:
		o.write(pair[0])
		o.write('\t')
		o.write(pair[1])
		o.write('\n')

	














