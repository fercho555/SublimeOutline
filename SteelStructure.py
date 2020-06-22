import tkinter as tk
from tkinter import ttk
import csv
import sys
import io
import os
import pdb
from decimal import Decimal, ROUND_HALF_EVEN
import math
#Add a class
class hanger():
    numb_bolts=1
    def __init__(self,fy,load,angle_thick):
        self.fy=fy
        self.load=load
        self.angle_thick=angle_thick

        hanger.numMaxBolt(fy,load,angle_thick)
##        hanger.BearingStress(load,fy,angle_thick,self.boltD)
##        hanger.loadInstan=load
    def thickplate(self,r):
        fy, load,angle_thick= self.fy, self.load,self.angle_thick
        v= float(load)/(float(fy)*float(r))
        return v
    def bearingstress(self,w,h):#w=number of bolts, h=bolt's diameter
        fy, load,angle_thick=self.fy, self.load,self.angle_thick
        q= float(load)/(float(angle_thick)*float(w)*float(h))
        return q

##    def __init__(self, size, fy, thickness, area, load):
##        global vertLo
##
##        self.size=size
##        self.fy=fy
##        self.thickness=thickness
##        self.area=area
##        self.load=load
    @classmethod
    def boltAllowStress(cls,fy,bolt,angle_thick):
        temp =cls(fy,round(2.0*bolt*bolt*fy/4*math.pi,2),angle_thick)
        return temp
    @staticmethod
    def numbOfBolts(a,bolt,c):
        nu=math.ceil(float(c)/(2*float(bolt)**2*float(a)/4*math.pi))
        return nu
    @classmethod
    def numMaxBolt(cls, n1,n2,n3):
        g=cls.numbOfBolts(n1,n2,n3)
        return g
##    @classmethod
##    def BearingStress(cls, load, numbOfBolts,thicknOfPlate,boltdiam):
##        t=cls.bearingCalc(load,numbOfBolts,thicknOfPlate,boltdiam)
##        return t
##    @staticmethod
##    def bearingCalc(kip,numb,plate,boltdiam):
##        mi=float(kip)/(float(numb)*float(plate)*float(boltdiam))
##        return mi


    def calculAreReqByLoad(self):
        allowabTensile=float(self.load)/2.7
        areaReq = round(float(self.load)/allowabTensile,2)
        return areaReq
    def areaRemovedBybolts(self):
        anglesSection = float(self.angle_thick)*2*1#1 represents a 1 inch diametre
        return anglesSection
    def safetyFactorForSteel(self):
        #depending on industry standards: If aerospace then factor 1.5;
        #whereas the cables in elevators must have a factor of 11.
        #I will assume a SF of 2.7
        SafetyFac=2.7
        return SafetyFac
    def displaycapacityOfBolt(self):
        print("Bolts capacity of {}diam is {}kips".format(self.angle_thick , self.load))
    def numberOfBolts(self):
        parti=self.boltAllowStress(self.fy,self.load,self.angle_thick)
        return self.load/parti
class ClassBearing():

    def __init__(self,  numbOfBolts, thicknOfPlate, diamBolts):
##        self.fy=class_a.fy
##        self.angle_thick=class_a.angle_thick
        self.numbOfBolts=numbOfBolts
        self.thicknOfPlate=thicknOfPlate
        self.diamBolts = diamBolts
    def bearing(numbOfBolts, thicknOfPlate, diamBolts,km):
         bear= 60/(float(numbOfBolts)*float(thicknOfPlate)*foat(diamBolts))
         return bear

def print_fy(_):
    global fy_val
    fy_val=ICustomer.get()
    print(ICustomer.get())

root = tk.Tk()#create an instance
ICus = tk.StringVar(root)
ICus.set("Select fy kips")
ICustomer = ttk.Combobox( textvariable = ICus, state = 'readonly')
ICustomer['values'] = ("36", "40", "50", "60")
ICustomer.grid(row = 2, column = 2)
label_ICustVar = tk.Label( textvariable= ICus)
label_ICustVar.grid(row = 1, column = 2)

ICustomer.bind("<<ComboboxSelected>>", print_fy)
#========combobox for load input=================

def print_value(self):
    global Load
    Load=comboVertLoad.get()
    print(combotext.get())
    print("Load selected: ",Load)

label_comboVertLoad= tk.Label(text="Enter load (kip)")
label_comboVertLoad.grid(row=1,column=3)
combotext= tk.StringVar()
comboVertLoad=ttk.Combobox(root, textvariable=combotext,state='readonly')
comboVertLoad['values']=("1","5","6","7","8","10","20","30","50","60","70","80")
comboVertLoad.current(0) #set the select item
comboVertLoad.grid(row=2, column=3)
comboVertLoad.bind("<<ComboboxSelected>>", print_value)
#Disable resizing the GUI
#root.resizable(False,False)
#=============Combobox for angles sizes================

def set_angle(_):
    global float_angle
    angle_val=comboAngleThickn.get()
    print(angle_val)
    float_angle=convert_to_float(angle_val)

def convert_to_float(frac_str):
    try:
        return float(frac_str)
    except ValueError:
        num, denom = frac_str.split('/')
        try:
            leading, num = num.split(' ')
            whole = float(leading)
        except ValueError:
            whole = 0
        frac = float(num) / float(denom)
        return whole - frac if whole < 0 else whole + frac

label_angleThickn = tk.Label(text="Angle thickness (in)")
label_angleThickn.grid(row=1, column=1)
anglesLabel = tk.StringVar()
anglesLabel.set("angle thickness (in)")
comboAngleThickn = ttk.Combobox(textvariable= anglesLabel)
comboAngleThickn['values']= ("1/8","5/16","1/4","3/8","1/2","5/8","3/4","7/8","1")
comboAngleThickn.grid(row=2, column=1)
comboAngleThickn.current(5)
comboAngleThickn.bind("<<ComboboxSelected>>", set_angle)
def set_AllowableS(self):
    global A307
    A307=float(comboA307.get())
    print("Bolt Allw stress: ", A307)

lab_comboA307 = tk.Label(text="Select type of Steel A307")
lab_comboA307.grid(row=4, column=1)
textVari=tk.StringVar()
textVari.set("Select allowable stress")
comboA307=ttk.Combobox(root,textvariable=textVari, state='readonly')
comboA307['values']=("10", "15","20")
comboA307.current(2)
comboA307.grid(row= 5 ,column= 1 )
comboA307.bind("<<ComboboxSelected>>", set_AllowableS)

def set_bolt(self):
    global float_bolt
    bolt_val= comboBolt.get()
    float_bolt=convert_to_float(bolt_val)
    print("Selected Bolt diameter", bolt_val)

lab_comboBolt = tk.Label(text="Bolt diameter in")
lab_comboBolt.grid(row=4, column=2)
tittext=tk.StringVar()
tittext.set("Select bolt's diameter (in)")
comboBolt=ttk.Combobox(root, textvariable=tittext, state='readonly')
comboBolt['values']=("5/16","3/8","7/16","1/2","9/16","5/8","3/4","7/8","1")
comboBolt.grid(row=5,column=2)
comboBolt.bind("<<ComboboxSelected>>", set_bolt)

#Assign value of boltsLabel to a variable
def set_gussetWidth (self):
    global gussetWidth
    gussetWidth= comboGusset.get()

    print("Selected gusset plate width (inch): ", gussetWidth)

lab_comboGusset = tk.Label(text="Gusset width (in) ")
lab_comboGusset.grid(row=4, column=3)
tittext=tk.StringVar()
tittext.set("Select gusset plate's width (in)")
comboGusset=ttk.Combobox(root, textvariable=tittext, state='readonly')
comboGusset['values']=("2","3","4","5","6","7","8","9","10")
comboGusset.grid(row=5,column=3)
comboGusset.current(4)
comboGusset.bind("<<ComboboxSelected>>", set_gussetWidth)
root.mainloop()

Dict = {}
Dict={'Dict1':{'Depth': '12'},
       'DictThickness':{'Thickness':1.375},
       'DictArea':{'Area':30.9}}
##print(Dict['DictThickness']['Thickness'])
##print(Dict.get('DictThickness'))
##print("\nDictionary with angles properties")
##print(Dict)

def main():
     global soughtArea
     strhang=hanger(fy_val,Load,float_angle)

     hanger1=hanger.boltAllowStress(A307,float_bolt,Load)
     print("Angle Req. section inch²: ", strhang.calculAreReqByLoad())
     crossSectByLoad = round(strhang.calculAreReqByLoad(),2)
     print("Area removed by bolts instal. inch²: ", \
           strhang.areaRemovedBybolts())
     crossSectRemovedByBolts = strhang.areaRemovedBybolts()
     totalAreaReqd= round(crossSectByLoad + crossSectRemovedByBolts,1)
     print('Total area required for structural angle in²: ', totalAreaReqd)
     totalReqArea_1=round(totalAreaReqd +0.1,1)
       #Chercher dans l'arrays taille de structure adequate
     with open("C:\\Users\\MOSES\\Documents\\POSTSAPPLIED.csv","r") as f:
         reader = csv.DictReader(f)
         #reader=csv.reader(f)
         Size,Depth,Thickness,Sectional_Area,Weight, Moment_of_Inertia \
                                                     =reader.fieldnames
##         reader=[[row[0],eval(row[1]),eval(row[2]),eval(row[3]),eval(row[4]),
##                  eval(row[5])]  for row in reader]
         #pdb.set_trace()

         for row in reader:

             if float(row[Sectional_Area]) == totalAreaReqd:
                 soughtArea = row[Size]
                 soughtThick= row[Thickness]
                 print ("Size: ",soughtArea)
                 print ("Thickness: ", soughtThick)
                 print ("Section sought FOUND",row[Sectional_Area])
             elif float(row[Sectional_Area]) == totalReqArea_1:
                 soughtArea = row[Size]
                 soughtThick= row[Thickness]
                 print ("Area value found with 0.01 increm: ", row[Sectional_Area])
                 print ("Size: ",row[Size])
                 print ("Thickness: ",row[Thickness])
             elif  float(row[Sectional_Area]) == round((totalAreaReqd + 0.2),1):
                 print ("Area value found with 0.02 increm: ", row[Sectional_Area])
                 print ("Size: ",row[Size])
                 print ("Thickness: ",row[Thickness])
             elif  float(row[Sectional_Area]) == round((totalAreaReqd + 0.3),1):
                 print ("Area value found with 0.03 increm: ", row[Sectional_Area])
                 print ("Size: ",row[Size])
                 print ("Thickness: ",row[Thickness])
##             else:
##                   print ("Area value notfound")


##   Number of bolts calculation
     hanger2=hanger(A307,Load,float_angle)
     print ("Number of bolts: ",hanger1.numMaxBolt(A307,float_bolt,Load) )
     #Store variable numbOfB to use subsequently in bearingstress function
     numbOfB= hanger1.numMaxBolt(A307,float_bolt,Load)
     # Thickness of plate calculation. First, new width should be entered
     hanger2.thickplate(gussetWidth)

     val_thickplate=hanger2.thickplate(gussetWidth)
     print("Gusset plate's thickness (in): " ,val_thickplate)

     mixHangBear=hanger(fy_val,Load,float_angle)
     mixHangBear.bearingstress(numbOfB,val_thickplate)#0.3 plate's thickness?
    
     print("Bearing stress: " ,mixHangBear.bearingstress(numbOfB,val_thickplate))




##     strhang=gussetThickReq(hanger)


try:

    my_file=open("C:\\Users\\MOSES\\Documents\\POSTSAPPLIED.csv","r")
    #run file through a reading method
    readFile = csv.reader(my_file)
    #print out each row
    for row in readFile:
        print(row)
    print(my_file.read())#Analytics4all.org/2016/05/06/python-working-csv-files/
    #You can dump the file into variables though.
    #You can work on those variables repeatedly
    Name = []
    Depth =[]
    Thickness =[]
    Area =[]
    for jt in readFile:
        Name.append(jt[0])
        Depth.append(jt[1])
        Thickness.append(jt[2])
        Area.append(jt[3])

##        print (Name)
##        print (Depth)
##        print (Thickness)
##        print (Area)
except IOError:
    print("File not found or path is incorrect")
finally:
    print("exit")

main()
