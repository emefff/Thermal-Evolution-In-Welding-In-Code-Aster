Salome-Meca and Code_Aster are very powerful tools in general thermo-mechanical engineering and simulation. However, some problems need a deeper dive into the guts of Code_Aster. This is one of those problems.
The basic idea is to simulate the thermal evolution of welding two plates with thickness 100, weld length is 100mm. The V-shaped weld is pre-designed as single body with 50 3D-zones. We need them for 'moving' the
heat source in every step. So basically, the moving heat source is equal to one such zone. Together with the heated zone, we also change its material properties from essentially heat conductivity = 0 to a certain value.
This is very important as you also see in the result: as we do not have any material in a real weld before the welding zone, it cannot have any heat conductivity (in real life it's air, but we are not interested in the 
air getting heated). Together with the changing material we also 'attach' this 'new' material to both of the plates in the for loop. You'll may also notice, we have a lot of material data in the Code_Aster command file. 
These data are generated with the two Python scripts. Because we are lazy and make mistakes, we do not want to type hundreds of values. We just generate two .csv-files we import in Salome-Meca during the first setup of the 
command file. 
