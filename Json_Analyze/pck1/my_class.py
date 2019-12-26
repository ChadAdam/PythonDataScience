import json
import requests

class my_class(object):
    """
    get_json_object() , add_json_object(ob) , del_id(id) , update_id(ob , id) , print_parem(json , p) , print_parem_multi(json , parem_list)
    """
    def __init__(self , url , index):
        self.url = url
        self.index = index
        self.json_ob = None
        self.json =  None
        self.arg_dict = dict()
        #for arg in args:
           # arg_dict[arg] = None

    def _true_url(self,index):
        return self.url + '/'+ self.index

    def _edit_ob(self, ob, key , value):
        for k in ob.keys():
            if k == key:
                ob[k] = value
        return ob

    def _find_kv(self,json, arg_dict, p=False):
        for i,dic in enumerate(json, start=1):
            if p == True:
                print(i,') \n')
            temp_dic = dict()
            for k,v in dic.items():
                #arg_dict[key]=dic.values
                if p == True:
                    print(k,'--',v,'\n')
                temp_dic[k]=None
                if k not in arg_dict.keys():
                    arg_dict[k] = None
            print('Above Keys List=', list(temp_dic.keys()), '<---\n')
           
        #print(arg_dict)
        return arg_dict
           
    

    def get_json_object(self):
        # Add Error checker for 200 code 
        self.json_ob=requests.get(self._true_url(self.index))
        if self.json_ob.status_code != 200:
            print("NOT SUCCESS -{}".format(json_ob.status_code))
        else:
            print(self.json_ob.status_code)
    def add_json_object(self,ob):
        print(ob.keys())
        t='n'
        while(t.lower() =="n"):
            k, v= input("Input Key/Value to Assign: ").split()
            ob = self._edit_ob(ob , k , v )
            t = str(input('Done?'))
        print(ob)
        resp = requests.post(self._true_url(self.index), json=ob)
        if resp.status_code != 201:
            print("NOT SUCCESS -{}".format(resp.status_code))
        else:
            print(resp.status_code)
    def del_id(self, id):
        url = self._true_url(self.index)
        url = url+'/{}'.format(id)
        print(url)
        resp = requests.delete(url)
        print(resp.status_code)
      
    def update_id(self, ob, id):
         print(ob.keys())
         url = self._true_url(self.index)
         url = url+'/{}'.format(id)
         print(requests.get(url).json())
         t='n'
         while(t.lower() =="n"):
            k, v= input("Input Key/Value to Assign: ").split()
            ob = self._edit_ob(ob , k , v )
            ob = [(k, v) for (k , v) in ob.items() if v != ' ']
            t = str(input('Done?'))
         print(ob)
        
         resp = requests.put(url, json=ob)
         if resp.status_code != 200:
            print("NOT SUCCESS -{}".format(resp.status_code))
         else:
            print(resp.status_code)
    def print_parem(self,json, p=False):
        dic = self._find_kv( json , self.arg_dict, p)
        for k in dic.keys():
            print(k)
        print('Length= ',len(json))
        print('------------------------------')
        return list(dic.keys())


    # Fix output so that its clean and easy to understand
    def print_parem_multi(self , json, parem_list):
        if type(json) is not dict:
            json= json[0]
        layer=0
        for key in parem_list:
            if key in json:
                #print(len(json), json[key])
                json_key = json[key]
                print('KEY= ',key)
                t = True
                done = 0
                #layer += 1
            while(t):
                #print('T ', layer)
                #print(str(json_key)+'--While Start\n')
                if type(json_key) is not dict and type(json_key) is not list:
                    #print(str(key)+" KEY\n")
                    layer=1
                    print('L= ',layer, ' ({}:{})'.format(key,json_key))
                    print("Not dict 1 " + str(json_key))
                    break
                
                else:
                    if type(json_key) is list:
                        if bool(json_key) != False:
                            json_key = json_key[0]
                            print('Json key is a list')
                            print(str(json_key) + ' Convert from list')
                        else:
                            print('Error: List is Empty'+str(type(json_key)))
                            break
                       
                    for k in json_key.keys():
                        #print(k,'cc')
                        if k not in json_key.keys():
                            print('Error: Key Not in Dict.Keys()')
                            continue
                        if type(json_key[k]) is not dict and type(json_key[k]) is not list:
                           # print("\tNot Dict 2 \n")
                            print("\tNot Dict 2 ",k,':',json_key[k])
                            #t=False
                            done +=1 
                            print(done)
                            if done == len(json_key):
                                print("\t\t I finished all keys")
                                print(len(json_key))
                               # if layer==2:
                                #    layer +=1
                                #else:
                                #layer=2
                                print('\tLayer= ',layer, ' ({}:{})'.format(key,json_key))
                                t = False
                        else:
                            json_key = json_key[k]
                            print('\t', json_key,'----->>')
                            layer +=1
                            print('\tLayer= ',layer, ' ({}:{})'.format(k,json_key))
                        #print("No k = dict")
                    print("NEXT ")
                    done=0
                #print('T2 ',layer)
                #layer+=1

                                

                                

 
            



                            




