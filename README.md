# Building-Feature-Classification
Abstract 

Three-dimensional, discontinuous, non-uniform spatial data is being collected at a rapid pace and may be stored in the form of point clouds. There has been little investigation about how machine learning techniques may be used to provide better outcomes for feature classification. The goal of my research is to gain insight into applying machine learning algorithms to classify building features. This project is part of a research initiative from the Center of Urban Science and Progress (CUSP) at NYU. 

Tools/Technologies Used: 
- Python (Numpy, pandas, matplotlib) 
- Jupyter Notebook/Deepnote
- CloudCompare 

An aerial LiDAR scan of Dublin City was conducted by the Urban Modeling Group at University College Dublin in 2015, covering an area of 5.6km^2 (including partially covered areas), with a total of 1.4 billion points. The densest point cloud tiles were selected to be split into 13 tiles, which consisted about 25 million building-labeled points (door/window/roof/structure). 

Three models were trained to classify doors, roofs, and windows. Due to the nature of general building layouts, the data had to be pre-processed prior to model creation. For instance, roofs tend to take up more surface area than doors, leading to an unequalized amount of represented classes in the models. Resampling, normalization and data cleaning was performed to ensure the quality of data found within the models. 
