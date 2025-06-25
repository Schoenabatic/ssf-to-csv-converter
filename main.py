import csv 
import os

def ssf_to_csv(filepath):

  file = open(filepath, 'r', encoding='utf-8')
  lines = file.readlines()

  # * expected result : [1,1.1,NP,തൂവെള്ള,"തൂവെള്ള,adj,,,,,,",k2:VGNF, parent: 3.1]
  csv_data = []
  sentence_data = []
  global_sentence_id = None
  drel = 'Na'

  # try:
  for line in lines:
   
      # print(f'line: {line.split(' ')}')
      
      if (line.startswith('<Sentence')):
        global_sentence_id = line.split("id='")[1].split("'")[0] # get id from start of sentence
        
      if (not sentence_data and global_sentence_id): # if sentence list is empty append sentence id
        sentence_data.append(global_sentence_id) 

      token_id = line.split('\t')[0] # get token id eg: 1.1, 2.2, 3.2
      if ('.' in token_id):
        sentence_data.append(token_id)
        
      if ('fs name' in line ) or ('((' in line) :
        fs_name = line.split('\t')[2] # eg: NP, BLK
        sentence_data.append(fs_name)
        
      if ('.' in line ) and (fs_name not in sentence_data): # add fs name to other token ids like 1.2 etc
        sentence_data.append(fs_name)
        
        
      if('name' in line and '((' not in line): #eg: പഴങ്ങളും
        name = line.strip().split("\t")[1]
        pos = line.strip().split("\t")[2]
        sentence_data.append(name)
        
        
      elif 'fs' in line: 
        name = line.strip().split("\t")[1]
        pos = line.strip().split("\t")[2]
        
      if ('head=' in line):
        name = line.split("head='")[1].split("'")[0]
        pos = line.strip().split("\t")[2]
        sentence_data.append(name)
        
        
      if ('drel' in line): #eg: k2:VGNF
        drel = line.strip().split("drel='")[1].split("'")[0]
        sentence_data.append(drel)
        
        
      if ('fs af' in line):
        print(line.strip().split("<"))
        fs_af = line.strip().split("<")[1].split('>')[0] # eg: fs af='കഥകളി,n,ne,sg,3,d,ഉടെ,yuTe' name='കഥകളിയുടെ'
        sentence_data.append(fs_af)
        
      if( line.endswith('>\n') and '.' in line): # check if sentence end
        sentence_data = [global_sentence_id, token_id, fs_name, name, pos, fs_af, drel]
        csv_data.append(sentence_data)
        sentence_data = []
        
      else: 
        pass
      
  # except:
  #   print(f"An exception occurred on {line.title()}")  
   
    


  
  # print(csv_data) # ! for testing purposes
  
  # print(filepath)
  
  output_path = 'Output'
  if not os.path.exists(output_path): # check if output folder exists
    os.makedirs(output_path)
  
  output_file = os.path.join(output_path, f"{os.path.basename(filepath).split('.ssf')[0]}.csv")
      
  with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([
    "sentence_id",
    "token_id",
    "chunk_type",
    "word",
    "pos",
    "fs",
    "drel"
])
    writer.writerows(csv_data)

if __name__ == "__main__":
  directory = 'General'
  
  # ssf_to_csv("Code/corpora.depn.ssf") #! for testing purposes
  
  for file in os.listdir(directory):
    if file.endswith(".ssf"):
      ssf_to_csv(os.path.join(directory, file))


  


