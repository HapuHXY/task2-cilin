#! /usr/bin/env python3
"""
基于同义词词林扩展版实现上下文关系自动抽取
将上下位关系词对写入文件中中，用Tab键隔开，以（下位词，上位词）顺序写入
"""

"""
code_word  以编码为key，单词list为value的dict，一个编码有多个单词
word_code  以单词为key，编码为value的dict，一个单词可能有多个编码
"""
code_word={}
word_code={}
cilin_file='/home/hxy/task2-cilin/new_cilin.txt'
res_file='/home/hxy/task2-cilin/result.txt'


with open(cilin_file,'r',encoding='gbk') as f:
	for line in f.readlines():
		res=line.split()
		code=res[0]
		words=res[1:]
		code_word[code]=words

		for word in words:
			if word in word_code.keys():
				word_code[word].append(code)
			else:
				word_code[word]=[code]
		
				
		#通过原子词群的编码，得到大，中，小类的编码,大类，中类的词具有很强的概括性，一般作为上位词
		if len(code)<6:	
			continue
		else:		
			#上位词集合
			word_fu_set=set()
			word_fu_set.update(code_word[code[:1]],code_word[code[:2]],[code_word[code[:5]][0]])
			#词段/原子词群中的词作为下位词，一般词段中第一个词是小类中的词，可以作为整个词群的上位词
			
			word_zi_set=set()
			word_zi_set.update(words)
			
			with open(res_file,'a') as o:
				#从原子词群向上找上层词，依次作为下层词的上位词
				for word_zi in word_zi_set:
					for word_fu in word_fu_set:
						if word_zi == word_fu:
							continue
						o.write(word_zi)
						o.write('\t')
						o.write(word_fu)
						o.write('\n')	
	



				
	






















