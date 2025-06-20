#

# if (line.startswith('<Sentence')):
  
#   sentence_id = line.split("id='")[1].split("'")[0] # start of sentence
#   csv_data.append(sentence_id)
  
  
#   sub_id = lines[i].split(" ")[0].split('\t')[0]
#   csv_data.append(sub_id)
  

#   pos = lines[i].split('\t')[2]
#   csv_data.append(pos)
  
#   if (lines[i].__contains__("fs name=")):
#     fs_name = lines[i].split("fs name='")[1].split("'")[0]
#     csv_data.append(fs_name)
    
#   elif (lines[i].__contains__("name=")):
#     name = lines[i].split("name='")[1].split("'")[0]
#     csv_data.append(name)
    
#   else: 
#     csv_data.append()
  
#   if (lines[i].__contains__("drel")):
#     drel = lines[i].split("drel='")[1].split("'")[0]
#     csv_data.append(drel)
    

  
#   elif (line.endswith('))')):
#     print('end of line')
  
# print(csv_data)
 
  
# elif(line.startswith('</Sentence>')):
#   print(csv_data)