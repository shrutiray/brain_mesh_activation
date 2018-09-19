Merge "temp2.msh" ; //using the temp.msh file for formatting
Merge "c0_m1.geo" ;
Merge "c0_m2.geo" ; 
//from image_generation.sh
//To print 50% activation area;

//name=Str("Top","Bottom","Left","Right","Front","Back") ;
//Printf(name[1]);

// define 
scale = 1.0; //scaling the image for storing as .png image
//storing the image orientation axis values
x[1] = 270;

y[1] = 360;

z[1] = 90;

//setting gmsh parameters
Mesh.SurfaceFaces = 0;
Mesh.SurfaceEdges = 0;
Mesh.SmoothNormals = 1;
Mesh.LightTwoSide = 1;

//scaling the xyz axis 
General.ScaleX = scale;
General.ScaleY = scale;
General.ScaleZ = scale;
General.TranslationX = 0;
General.TranslationY = 0;
General.TranslationZ = 0;

General.SmallAxes = 0;
General.Trackball = 0;

View[0].Visible = 0;
View[1].Visible = 1 ;
View[1].Light =1;
View[1].LightLines=1;
View[1].LightTwoSide=1;
View[1].RangeType=2;
a1=View[1].Min;
a2=View[1].Max;
View[1].CustomMin=a2*0.8;
View[1].CustomMax=a2;
View[2].Visible = 0;
View[3].Visible = 0;

//  View.CustomMax = 3;
//  View.CustomMin = 0;
//  View.SaturateValues = 1;
//  View.RangeType = 2;
//  View.VectorType = 1;
//  View.Visible = 1;
//  View.AngleSmoothNormals = 60;
//  View.SmoothNormals = 1;
//  View.NbIso = 0;
//  View.Name = '';
//  View.Light = 0;


//Rotating through the axis values
For i In {1:1}
  General.RotationX = x[i];
  General.RotationY = y[i];
  General.RotationZ = z[i];
  Printf(" %i", i);

  Print Sprintf("temp_image_act_01.png"); //printing the 
  //image and filename

EndFor

Exit;

//Delete Physicals;


