from bs4 import BeautifulSoup
import tkinter as tk
import requests
import tkinter.font as font
from rich import print as ps

win = tk.Tk()
winFont = font.Font(family='Segoe UI', size=11, weight='bold')


def airTravel():
    global driver
    L14=tk.Label(win, text="-"*69+"Air Travel"+"-"*69,font=winFont)
    L14.grid(row=15,column=1,pady=15,padx=(30,0))
    win.update()
    
    airport1 = BeautifulSoup(requests.request("GET", f'https://www.travelmath.com/nearest-airport/kuwait').content, "html.parser")
    airport2 = BeautifulSoup(requests.request("GET", f'https://www.travelmath.com/nearest-airport/goa').content, "html.parser")
    
    code1=airport1.find_all("li")
    code2=airport2.find_all("li")
    airports=[]
    airports2=[]
    c=0
    for i in code1:
    
        st=i.text
    
        if(st.find("(") !=-1):
            airports.append(st[st.find("(")+1:st.find("(")+4])
        c+=1
    
    
    ps(code1,code2,airports)

airTravel()