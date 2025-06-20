file = open('test.ssf', 'r', encoding='utf-8') # try with 1.misc.depn.ssf
lines = file.readlines()


# * expected result : ['1', '1.1', 'N__NN', 'കഥകളിയുടെ', നിറം,n,ne,sg,3,d,0,0]
csv_data = []
sentence_data = []
global_sentence_id = None



for line in lines:
  
  if (line.startswith('<Sentence')):
    global_sentence_id = line.split("id='")[1].split("'")[0] # get id from start of sentence
    
  if not sentence_data and global_sentence_id: # if sentence list is empty append sentence id
    sentence_data.append(global_sentence_id) 

  token_id = line.split('\t')[0] # get token id eg: 1.1, 2.2, 3.2
  if ('.' in token_id):
    sentence_data.append(token_id)
    
  if ('fs name' in line ) :
    fs_name = line.split('\t')[2] # eg: NP, BLK
    sentence_data.append(fs_name)
    
  if ('.' in line ) and (fs_name not in sentence_data): # add fs name to other token ids like 1.2 etc
    sentence_data.append(fs_name)
    
  if('name' in line and '((' not in line):
    name = line.strip().split("\t")[1]
    sentence_data.append(name)
    
  if ('drel' in line): #eg: k2:VGNF
    drel = line.strip().split("drel='")[1].split("'")[0]
    sentence_data.append(drel)
    
  if ('fs af' in line):
    fs_af = line.strip().split("fs af='")[1].split("'")[0] # eg: നിറം,n,ne,sg,3,d,0,0
    sentence_data.append(fs_af)
    
  
  if( line.endswith('>\n') and len(sentence_data) >=4 ): # check if sentence end
    
    csv_data.append(sentence_data)
    sentence_data = []
    
  else: 
    pass
    
  
print(csv_data)
