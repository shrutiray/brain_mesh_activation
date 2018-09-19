Merge "temp.msh" ; //using the temp.msh file for formatting 
//from image_generation.sh
//Merge "almi5_001_dir_170316-142935_tensor_visualization.pos";

//name=Str("Top","Bottom","Left","Right","Front","Back") ;
//Printf(name[1]);

// define 
scale = 1.0; //scaling the image for storing as .png image
//storing the image orientation axis values
x[1] = 0;
x[2] = 180;
x[3] = 270;
x[4] = 270;
x[5] = 270;
x[6] = 270;

y[1] = 0;
y[2] = 0;
y[3] = 360;
y[4] = 0;
y[5] = 360;
y[6] = 0;

z[1] = 0;
z[2] = 180;
z[3] = 90;
z[4] = 270;
z[5] = 180;
z[6] = 0;

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
For i In {1:6}
  General.RotationX = x[i];
  General.RotationY = y[i];
  General.RotationZ = z[i];
  Printf(" %i", i);

  Print Sprintf("temp_image_%02g.png",i); //printing the 
  //image and filename

EndFor

Exit;

//Delete Physicals;


