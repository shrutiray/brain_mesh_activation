#!/bin/bash

#extracting the mesh components one at a time

for f in *_1001.msh *_1002.msh *_1003.msh *_1004.msh *_1005.msh;
do
    filename=$f
    stored_name=$f #storing the original file
    printf "starting....." $filename "\n"
    printf "remnaming file to temp.... \n"
    cp ${filename} copy.msh
    mv copy.msh temp.msh #renaming as temp.msh so that 
    #it can easily be accessed by the gmsh script for 
    #formatting
    printf "running gmsh .geo script on file..... \n"
    gmsh visual_check2.geo temp.msh #running the gmsh script for formatting mesh display and storing as .png image file
    printf "renaming files....\n" #changing the .png filename based on the display axis side
    mv temp_image_01.png ${f}_top.png
    mv temp_image_02.png ${f}_below.png
    mv temp_image_03.png ${f}_left_side.png 
    mv temp_image_04.png ${f}_right_side.png
    mv temp_image_05.png ${f}_front.png
    mv temp_image_06.png ${f}_behind.png
    printf "done with...... " $f "\n"
done

