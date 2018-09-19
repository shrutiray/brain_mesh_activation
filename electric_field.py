#!/usr/bin/env python
# 1) add current path 
import sys
sys.path.append("simnibs_2.0.1")
sys.path.append(r"/Users/shrutiray/simnibs_2.0.1/fem_efield/src_python")
sys.path.append(r"/Users/shrutiray/Documents/dataset/simnibs2.0_example")

# 2) Import libraries
import os
import numpy
import gmsh_numpy
import glob
from scipy.stats import rankdata

# 3) current path
os.chdir('/Users/shrutiray/Documents/dataset/simnibs2.0_example')
#os.chdir('/Users/shrutiray/Documents/dataset')
path=os.getcwd()
#script='/Users/shrutiray/Code/image_generation.sh'

file_path_name='/Users/shrutiray/Documents/dataset/simnibs2.0_example'

# 8) define function for use in loop to seperate the mesh components   
def seperating_meshes_func(new_tail,r):    
    m = gmsh_numpy.read_msh(new_tail) #reads the .msh file       
    index_gm = (m.elm.tag1==r) #seperates the mesh components w.r.t the tag number 
    #re-assigning of mesh variable after seperation                  
    gm=m     
    node_number_list_orig = m.elm.node_number_list
    node_number_list_new0 = node_number_list_orig[index_gm]
    idx_surface=(node_number_list_new0[:,3]==0)
    node_number_list_new = node_number_list_new0[idx_surface] 
   
    node_index=numpy.unique(node_number_list_new)
    node_index=node_index[1:len(node_index)]  
                          
    node_number_list_new_new = rankdata(node_number_list_new,method='dense').reshape(node_number_list_new.shape)-1 

    gm.elm.node_number_list=node_number_list_new_new
    
    #setting elmtype
    elmtype=m.elm.elm_type
    elmtype=elmtype[index_gm]
    elmtype=elmtype[idx_surface]
    gm.elm.elm_type=elmtype
    #setting the tag
    tagtype=m.elm.tag1
    tagtype=tagtype[index_gm]
    tagtype=tagtype[idx_surface]
    gm.elm.tag1=tagtype
    
    gm.elm.nr_elm_of_type=len(gm.elm.elm_type)
    gm.elm.nr_tags=2
    gm.elm.number_of_tags=2
    
    tagtype2=m.elm.tag2
    tagtype2=tagtype2[index_gm]
    tagtype2=tagtype2[idx_surface]
    gm.elm.tag2=tagtype2
        
    gm.nodes.node_coord = m.nodes.node_coord[node_index-1]                         
    gm.elm.elm_number= m.elm.elm_number[0:len(gm.elm.node_number_list)]                   
    gm.elm.nr=len(gm.elm.node_number_list)   
    gm.elm.number_of_elements = len(gm.elm.elm_number)
    gm.nodes.number_of_nodes=len(gm.nodes.node_coord)
    gm.nodes.nr=gm.nodes.number_of_nodes
    gm.nodes.node_number = numpy.array(range(1,gm.nodes.nr+1))
    
    #setting the post processing options - $ElementData
    #strings_tags and real_tags remain the same.
    #set the integer_tag values - number_of_ineger_tags 
    #remain the same, so no need to re-state
    integertag0=m.elmdata[0].integer_tags
    integertag0[2]=gm.elm.nr
    gm.elmdata[0].integer_tags=integertag0

    integertag1=m.elmdata[1].integer_tags
    integertag1[2]=gm.elm.nr
    gm.elmdata[1].integer_tags=integertag1

    integertag2=m.elmdata[2].integer_tags
    integertag2[2]=gm.elm.nr
    gm.elmdata[2].integer_tags=integertag2

    integertag3=m.elmdata[3].integer_tags
    integertag3[2]=gm.elm.nr
    gm.elmdata[3].integer_tags=integertag3

    #setting the element_number values
    elmnumber0=numpy.array(range(1,gm.elm.nr+1))
    gm.elmdata[0].elm_number=elmnumber0

    elmnumber1=numpy.array(range(1,gm.elm.nr+1))
    gm.elmdata[1].elm_number=elmnumber1

    elmnumber2=numpy.array(range(1,gm.elm.nr+1))
    gm.elmdata[2].elm_number=elmnumber2

    elmnumber3=numpy.array(range(1,gm.elm.nr+1))
    gm.elmdata[3].elm_number=elmnumber3

    #setting the $ElementData values
    value0=m.elmdata[0].value
    value0=value0[index_gm]
    value0=value0[idx_surface]
    gm.elmdata[0].value=value0

    value1=m.elmdata[1].value
    value1=value1[index_gm]
    value1=value1[idx_surface]
    gm.elmdata[1].value=value1

    value2=m.elmdata[2].value
    value2=value2[index_gm]
    value2=value2[idx_surface]
    gm.elmdata[2].value=value2

    value3=m.elmdata[3].value
    value3=value3[index_gm]
    value3=value3[idx_surface]
    gm.elmdata[3].value=value3
   
    gm.fn = base_name + '_' + str(r) + '.msh'    
    gm.name = base_name + '_' + str(r)   
    return gm

# 4) extract subject files witih .msh format 
#and store in text file for looping
concat_file = file_path_name + '/*.msh'
filenames = glob.glob(concat_file)  
f=open("filenames.txt","w")
for i in range(len(filenames)):
    
    f.write("%s \n" %(filenames[i]))
    print str(filenames[i])
    
f.close()   
file_name=open("filenames.txt","r")


# 5) run mesh extraction across each line in text file (each subject)
for line in open('filenames.txt'):
    head, tail = os.path.split(line)    
    new_tail=tail.rstrip(' \n')    
    base_name = os.path.splitext(new_tail)[0]   
    print base_name     
#    m = gmsh_numpy.read_msh(new_tail)    
# 6) extracting each mesh structure
    for r in range(1001,1006):        
        gm = seperating_meshes_func(new_tail,r)
        gmsh_numpy.write_msh(gm)
        
# 7) Calling bash script from python for one terminal input :D
from subprocess import Popen, PIPE
cmd = "/Users/shrutiray/Code/image_elec_field.sh"
p = Popen(cmd , shell=True, stdout=PIPE, stderr=PIPE)
out, err = p.communicate()
print "Return code: ", p.returncode
print out.rstrip(), err.rstrip()

#def f():
#    cmd1 = "/Users/shrutiray/Code/image_generation.sh"          
#    os.system(cmd1)
#f()


        
      