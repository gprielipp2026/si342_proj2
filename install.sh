rm -f toGUI fromGUI
mkfifo toGUI
mkfifo fromGUI
curl -O https://faculty.cs.usna.edu/~wcbrown/courses/F24SI342/proj/04/triangle-app-v1.0
curl -O https://faculty.cs.usna.edu/~wcbrown/courses/F24SI342/proj/04/resources.neu
chmod +x ./triangle-app-v1.0
