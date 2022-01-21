from tkinter import *
from tkinter import ttk
import tkinter.messagebox as tkm


app=Tk()
app.title('Distance Converter')
app.geometry('600x315-400-380')
app.resizable(False,False)


convert_value=StringVar()
#convert_value.set('')
frmcmb=StringVar()
tocmb=StringVar()
res_var=StringVar()


def reset():
    convert_value.set('')
    frmcmb.set('')
    tocmb.set('')
    res_var.set('')
    


def convert():
    if convert_value.get()=="":
        tkm.showinfo('Value Error','Please enter a value to convert.')

    #if float(convert_value.get()) * 1 != float(convert_value.get()):
    #    tkm.showinfo('Value Error','Please enter a number, not a string.')

    value=float(convert_value.get())
    valfrom=frmcmb.get()
    valto=tocmb.get()

    
    if valfrom=='':
        tkm.showinfo('Unit Error','Please select a uint to convert from.')

    elif valto=='':
        tkm.showinfo('Unit Error','Please select a uint to convert to.')
    
    elif valfrom==valto:
        convert_constant=1
    
    #'Inches'
    elif valfrom=='Inches' and valto=='Feet':
        convert_constant=0.083333
    elif valfrom=='Feet' and valto=='Inches':
        convert_constant=12
    elif valfrom=='Inches' and valto=='Yards':
        convert_constant=0.083333
    elif valfrom=='Yards' and valto=='Inches':
        convert_constant=12
    elif valfrom=='Inches' and valto=='Miles':
        convert_constant=0.000016
    elif valfrom=='Miles' and valto=='Inches':
        convert_constant=63360
    elif valfrom=='Inches' and valto=='Nautical Miles':
        convert_constant=0.000014
    elif valfrom=='Nautical Miles' and valto=='Inches':
        convert_constant=72913.39
    elif valfrom=='Inches' and valto=='Nanometers':
        convert_constant=25400000
    elif valfrom=='Nanometers' and valto=='Inches':
        convert_constant=0.000000039370079
    elif valfrom=='Inches' and valto=='Microns':
        convert_constant=25400
    elif valfrom=='Microns' and valto=='Inches':
        convert_constant=0.000039
    elif valfrom=='Inches' and valto=='Millimeters':
        convert_constant=25.4
    elif valfrom=='Millimeters' and valto=='Inches':
        convert_constant=0.03937
    elif valfrom=='Inches' and valto=='Centimeters':
        convert_constant=2.54
    elif valfrom=='Centimeters' and valto=='Inches':
        convert_constant=0.393701
    elif valfrom=='Inches' and valto=='Meters':
        convert_constant=0.0254
    elif valfrom=='Meters' and valto=='Inches':
        convert_constant=39.37008
    elif valfrom=='Inches' and valto=='Kilometers':
        convert_constant=0.000025
    elif valfrom=='Kilometers' and valto=='Inches':
        convert_constant=39370.08

    #Feet','Yards','Miles','Nautical Miles','Nanometers','Microns','Millimeters','Centimeters','Meters','Kilometers'
    elif valfrom=='Feet' and valto=='Yards':
        convert_constant=0.333333
    elif valfrom=='Yards' and valto=='Feet':
        convert_constant=3
    elif valfrom=='Feet' and valto=='Miles':
        convert_constant=5280
    elif valfrom=='Miles' and valto=='Feet':
        convert_constant=63360
    elif valfrom=='Feet' and valto=='Nautical Miles':
        convert_constant=0.000165
    elif valfrom=='Nautical Miles' and valto=='Feet':
        convert_constant=6076.115
    elif valfrom=='Feet' and valto=='Nanometers':
        convert_constant=304800000
    elif valfrom=='Nanometers' and valto=='Feet':
        convert_constant=0.00000000328084
    elif valfrom=='Feet' and valto=='Microns':
        convert_constant=304800
    elif valfrom=='Microns' and valto=='Feet':
        convert_constant=0.000003
    elif valfrom=='Feet' and valto=='Millimeters':
        convert_constant=304.8
    elif valfrom=='Millimeters' and valto=='Feet':
        convert_constant=0.003281
    elif valfrom=='Feet' and valto=='Centimeters':
        convert_constant=30.48
    elif valfrom=='Centimeters' and valto=='Feet':
        convert_constant=0.032808
    elif valfrom=='Feet' and valto=='Meters':
        convert_constant=0.3048
    elif valfrom=='Meters' and valto=='Feet':
        convert_constant=3.28084
    elif valfrom=='Feet' and valto=='Kilometers':
        convert_constant=0.000305
    elif valfrom=='Kilometers' and valto=='Feet':
        convert_constant=3280.84
   
   #'Yards','Miles','Nautical Miles','Nanometers','Microns','Millimeters','Centimeters','Meters','Kilometers'
    elif valfrom=='Yards' and valto=='Miles':
        convert_constant=0.000568
    elif valfrom=='Miles' and valto=='Yards':
        convert_constant=1760
    elif valfrom=='Yards' and valto=='Nautical Miles':
        convert_constant=0.000494
    elif valfrom=='Nautical Miles' and valto=='Yards':
        convert_constant=2025.372
    elif valfrom=='Yards' and valto=='Nanometers':
        convert_constant=914400000
    elif valfrom=='Nanometers' and valto=='Yards':
        convert_constant=0.000000001093613
    elif valfrom=='Yards' and valto=='Microns':
        convert_constant=914400
    elif valfrom=='Microns' and valto=='Yards':
        convert_constant=0.000001
    elif valfrom=='Yards' and valto=='Millimeters':
        convert_constant=914.4
    elif valfrom=='Millimeters' and valto=='Yards':
        convert_constant=0.001094
    elif valfrom=='Yards' and valto=='Centimeters':
        convert_constant=91.44
    elif valfrom=='Centimeters' and valto=='Yards':
        convert_constant=0.010936
    elif valfrom=='Yards' and valto=='Meters':
        convert_constant=0.9144
    elif valfrom=='Meters' and valto=='Yards':
        convert_constant=1.093613
    elif valfrom=='Yards' and valto=='Kilometers':
        convert_constant=0.000914
    elif valfrom=='Kilometers' and valto=='Yards':
        convert_constant=1093.613

    #'Miles','Nautical Miles','Nanometers','Microns','Millimeters','Centimeters','Meters','Kilometers'
    elif valfrom=='Miles' and valto=='Nautical Miles':
        convert_constant=0.868976
    elif valfrom=='Nautical Miles' and valto=='Miles':
        convert_constant=1.150779
    elif valfrom=='Miles' and valto=='Nanometers':
        convert_constant=1609344000000
    elif valfrom=='Nanometers' and valto=='Miles':
        convert_constant=0.000000000000621
    elif valfrom=='Miles' and valto=='Microns':
        convert_constant=1609344000
    elif valfrom=='Microns' and valto=='Miles':
        convert_constant=0.000000000621371
    elif valfrom=='Miles' and valto=='Millimeters':
        convert_constant=1609344
    elif valfrom=='Millimeters' and valto=='Miles':
        convert_constant=0.000000621371192
    elif valfrom=='Miles' and valto=='Centimeters':
        convert_constant=160934.4
    elif valfrom=='Centimeters' and valto=='Miles':
        convert_constant=0.000006
    elif valfrom=='Miles' and valto=='Meters':
        convert_constant=1609.344
    elif valfrom=='Meters' and valto=='Miles':
        convert_constant=0.000621
    elif valfrom=='Miles' and valto=='Kilometers':
        convert_constant=1.609344
    elif valfrom=='Kilometers' and valto=='Miles':
        convert_constant=0.621371
    
    
    #'Nautical Miles','Nanometers','Microns','Millimeters','Centimeters','Meters','Kilometers'
    elif valfrom=='Nautical Miles' and valto=='Nanometers':
        convert_constant=1852000000000
    elif valfrom=='Nanometers' and valto=='Nautical Miles':
        convert_constant=0.00000000000054
    elif valfrom=='Nautical Miles' and valto=='Microns':
        convert_constant=1852000000
    elif valfrom=='Microns' and valto=='Nautical Miles':
        convert_constant=0.000000000539957
    elif valfrom=='Nautical Miles' and valto=='Millimeters':
        convert_constant=1852000
    elif valfrom=='Millimeters' and valto=='Nautical Miles':
        convert_constant=0.000000539956803
    elif valfrom=='Nautical Miles' and valto=='Centimeters':
        convert_constant=185200
    elif valfrom=='Centimeters' and valto=='Nautical Miles':
        convert_constant=0.000005
    elif valfrom=='Nautical Miles' and valto=='Meters':
        convert_constant=1852
    elif valfrom=='Meters' and valto=='Nautical Miles':
        convert_constant=0.00054
    elif valfrom=='Nautical Miles' and valto=='Kilometers':
        convert_constant=1.852
    elif valfrom=='Kilometers' and valto=='Nautical Miles':
        convert_constant=0.539957
    
    
    #'Nanometers','Microns','Millimeters','Centimeters','Meters','Kilometers'
    elif valfrom=='Nanometers' and valto=='Microns':
        convert_constant=0.001
    elif valfrom=='Microns' and valto=='Nanometers':
        convert_constant=1000
    elif valfrom=='Nanometers' and valto=='Millimeters':
        convert_constant=0.000001
    elif valfrom=='Millimeters' and valto=='Nanometers':
        convert_constant=1000000
    elif valfrom=='Nanometers' and valto=='Centimeters':
        convert_constant=0.0000001
    elif valfrom=='Centimeters' and valto=='Nanometers':
        convert_constant=10000000
    elif valfrom=='Nanometers' and valto=='Meters':
        convert_constant=0.000000001
    elif valfrom=='Meters' and valto=='Nanometers':
        convert_constant=1000000000
    elif valfrom=='Nanometers' and valto=='Kilometers':
        convert_constant=0.000000000001
    elif valfrom=='Kilometers' and valto=='Nanometers':
        convert_constant=1000000000000


    #'Microns','Millimeters','Centimeters','Meters','Kilometers'
    elif valfrom=='Microns' and valto=='Millimeters':
        convert_constant=0.001
    elif valfrom=='Millimeters' and valto=='Microns':
        convert_constant=1000
    elif valfrom=='Microns' and valto=='Centimeters':
        convert_constant=0.0001
    elif valfrom=='Centimeters' and valto=='Microns':
        convert_constant=10000
    elif valfrom=='Microns' and valto=='Meters':
        convert_constant=0.000001
    elif valfrom=='Meters' and valto=='Microns':
        convert_constant=1000000
    elif valfrom=='Microns' and valto=='Kilometers':
        convert_constant=0.000000001
    elif valfrom=='Kilometers' and valto=='Microns':
        convert_constant=1000000000


    #'Millimeters','Centimeters','Meters','Kilometers'
    elif valfrom=='Millimeters' and valto=='Centimeters':
        convert_constant=0.1
    elif valfrom=='Centimeters' and valto=='Millimeters':
        convert_constant=10
    elif valfrom=='Millimeters' and valto=='Meters':
        convert_constant=0.001
    elif valfrom=='Meters' and valto=='Millimeters':
        convert_constant=1000
    elif valfrom=='Millimeters' and valto=='Kilometers':
        convert_constant=0.000001
    elif valfrom=='Kilometers' and valto=='Millimeters':
        convert_constant=1000000

    #'Centimeters','Meters','Kilometers'
    elif valfrom=='Centimeters' and valto=='Meters':
        convert_constant=0.01
    elif valfrom=='Meters' and valto=='Centimeters':
        convert_constant=100
    elif valfrom=='Centimeters' and valto=='Kilometers':
        convert_constant=0.00001
    elif valfrom=='Kilometers' and valto=='Centimeters':
        convert_constant=100000

    #'Meters','Kilometers'
    elif valfrom=='Meters' and valto=='Kilometers':
        convert_constant=0.001
    elif valfrom=='Kilometers' and valto=='Meters':
        convert_constant=1000

    result=value*convert_constant

    res_var.set(str(value)+ '  '+valfrom+'  is  '+str(result)+'  '+valto)

#===============================================================================================================================================
mframe=Frame(app, bg='#7fb174',bd=3,relief=RIDGE)
mframe.pack()

s=Label(mframe,text='Developed by Thomas Burns Botchwey',
        font=('candara',10,'bold'),justify='right',bd=3,relief=SUNKEN,anchor=E)
s.pack(side='bottom',fill=X)

framea=Frame(mframe)
framea.pack(side='top',pady=0)
#===============================================================================================================================================
lframe=Frame(framea, bg='#d4587a',bd=3,relief=RIDGE,width=450,height=250)
lframe.pack(side='left')

lframe1=LabelFrame(lframe, bg='#d4587a',bd=3,relief=RIDGE,width=450,height=80,text='Enter Value',font=('montserat',13,'italic'))
lframe1.pack(side='top')

val=Label(lframe1,text='Value',font=('montserat',12,'bold'),bg='#d4587a')
val.pack(side='left',pady=15)

valen=Entry(lframe1,textvariable=convert_value,font=('montserat',15,'bold'),bg='#7fb174',width=30,justify='right')
valen.pack(side='left',pady=15,padx=15)

lframe2=LabelFrame(lframe, bg='#d4587a',bd=3,relief=RIDGE,width=450,height=200,text='Select Conversion',font=('montserat',13,'italic'))
lframe2.pack(side='top',pady=20,padx=10)

ffrom=Label(lframe2,text='From:',font=('montserat',12,'bold'),bg='#d4587a')
ffrom.grid(row=0,column=0,sticky=E)

ffrom_value=ttk.Combobox(lframe2,width=30,textvariable=frmcmb,font=('montserat',15,'bold'),state='readonly')
ffrom_value['value']=['','Inches','Feet','Yards','Miles','Nautical Miles','Nanometers','Microns','Millimeters','Centimeters','Meters','Kilometers']
ffrom_value.grid(row=0,column=1,padx=15,pady=10)

to=Label(lframe2,text='To:',font=('montserat',12,'bold'),bg='#d4587a')
to.grid(row=1,column=0,sticky=E)

to_value=ttk.Combobox(lframe2,width=30,textvariable=tocmb,font=('montserat',15,'bold'),state='readonly')
to_value['value']=['','Inches','Feet','Yards','Miles','Nautical Miles','Nanometers','Microns','Millimeters','Centimeters','Meters','Kilometers']
to_value.grid(row=1,column=1,padx=15,pady=10)

#===============================================================================================================================================
rframe=Frame(framea, bg='#d4587a',bd=3,relief=RIDGE,width=150,height=250)
rframe.pack(side='right')

btnCon=Button(rframe,text='Convert',font=('montserat',15,'bold'),bg='#32435f',width=10,height=2,bd=6,command=convert)
btnCon.pack(side='top',pady=25,padx=5)

btnRes=Button(rframe,text='Reset',font=('montserat',15,'bold'),bg='#bc5f6a',width=10,height=2,bd=6,command=reset)
btnRes.pack(side='top',pady=25,padx=5)
#===============================================================================================================================================
dframe=Frame(mframe, bg='#d4587a',bd=3,relief=RIDGE,width=600,height=50)
dframe.pack(side='bottom')

res=Entry(dframe,font=('montserat',12,'bold'),textvariable = res_var, width = 100, state='readonly')
res.pack(fill=X)

#===============================================================================================================================================
#app.bind('<Return>',convert)
app.mainloop()
