The data is locally downloaded via our drive, and is found in a folder called Data, 
Link to the drive - https://drive.google.com/drive/folders/1iNQdBk9WtV7Qm7Qs5fe6stzXTRwT5TS8
Library requirements located in the 'reqirements.txt' file.


============================================================= How to run our code: ====================================================

Firstly create a folder called "Data", then:
Download *311_2025_Jan_Dec.csv* from the Google Drive and add it to "Data" folder
Download the 3 geojson files located in Google Drive ( *new-york-city-boroughs.geojson.txt*, *Centerline.geojson*, *Zip-Code-Tabulation-Areas-(MODZCTA).geojson* )...
...and put them in 'Data' folder 
Run 'Final_Pre_EDA_Table.ipynb'
Run 'EDA_Final.ipynb'
Now you can run each clustering zip/street files, thanks for your attention and enjoy!

#NOTE: DBSCAN is deprecated but you can still run it.


============================================================== Kepler map guide: ===========================================================

Run the code
Open the arrow on the top left
In the 'Layers' section click on the arrow near "NYC Boroughs" 
Click on the cyan box next to 'Fill Color'
Next under 'Stroke Color' click on the color underneath and choose black ( or whatever you want )

In the same 'Layers' section click on the arrow near "NYC Street by Cluster" 
Click on the cyan box next to 'Stroke Color'
Next to 'Fill Color' click on the 3 vertical dots.

In the newly appeared "Color based on" field, click on it and choose "cluster"
Click on the color palette and select the amount of steps as the amount of clusters
Choose the Type to be qualitative and choose a palette you would like. 

========================================================================================================================================