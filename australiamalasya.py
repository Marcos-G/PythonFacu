def get_tag_value(f):
    line = f.readline()
    num_line, num_query = line.split()

    dict_tag_value = {}
    prev_tag_name_list = []

    for count in range(int(num_line)):
        #print(dict_tag_value)
        curr_line = f.readline()
        if curr_line.startswith('</'):
            prev_tag_name_list.pop(-1)
        else:
            curr_line = curr_line.replace('<','').replace('>', '')
            taglist=True
            if '/' in curr_line:
                curr_line.replace('/','')
                taglist=False
            curr_tag_name = curr_line.split()[0]
            value_list = curr_line.replace(curr_tag_name, '').split()
            prev_tag = '.'.join(prev_tag_name_list)
            for index in range(len(value_list)):
                tags=value_list[index].split("=")
                tag_name = tags[0].strip()
                tag_val = tags[1].replace('"','').strip()

                if prev_tag_name_list:
                    temp_tag = '%s.%s' %(prev_tag, curr_tag_name)
                    dict_tag_value['%s~%s' %(temp_tag, tag_name)] = tag_val
                else:
                    dict_tag_value['%s~%s' %(curr_tag_name, tag_name)] = tag_val
            if taglist:
                prev_tag_name_list.append(curr_tag_name)
    for count in range(int(num_query)):
        entry = f.readline().strip()
        if entry in dict_tag_value:
            print (dict_tag_value[entry], end=chr(hex("0x0A")))
        else:
            print ('¡No encontrado!', end=chr(hex("0x0A")))


for i in range(1,16):
    print("archivo",i)
    n="input-"
    if(i<10):
        n+="0"
    n+=str(i)+".hrml"
    f = open(n)
    get_tag_value(f)
    f.close()
