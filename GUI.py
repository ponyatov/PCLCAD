import os,sys,time,pickle,random

import wx,wx.py.shell

import COLOR

app = wx.App()

# main frame

frmMain = wx.Frame(None,-1,'pyCAD')
frmMain.SetIcon(wx.Icon('cad.ico', wx.BITMAP_TYPE_ICO))
frmMain.Maximize()
frmMain.Show()

status = frmMain.CreateStatusBar()

# menu 

menu = wx.MenuBar()
frmMain.SetMenuBar(menu)

menuFile = wx.Menu()
menu.Append(menuFile,'&File')

miOpen = wx.MenuItem(menuFile,-1,'&Open\tAlt+O','Open')
def onOpen(e):  
    dlg=wx.FileDialog(frmMain,"Open",os.getcwd(),'','*.pcd',wx.OPEN)
    if dlg.ShowModal() == wx.ID_OK:
        D,F=dlg.GetDirectory(),dlg.GetFilename()
        T=open('%s/%s'%(D,F),'rb') ; global DAT ; DAT=pickle.load(T) ; T.close()
        global FileName ; FileName = F ; onRefresh(None)
frmMain.Bind(wx.EVT_MENU, onOpen, menuFile.AppendItem(miOpen))

def NOW(): return '%.4i%.2i%.2i_%.2i%.2i%.2i'%time.localtime()[:6]

miSave = wx.MenuItem(menuFile,-1,'&Save\tAlt+S','Save')
def onSave(e): 
    dlg=wx.FileDialog(frmMain,"Save",os.getcwd(),'%s.pcd'%NOW(),'*.pcd',wx.SAVE)
    if dlg.ShowModal() == wx.ID_OK:
        D,F=dlg.GetDirectory(),dlg.GetFilename()
        T=open('%s/%s'%(D,F),'wb') ; pickle.dump(DAT,T) ; T.close()
        global FileName ; FileName=F ; onRefresh(None)
frmMain.Bind(wx.EVT_MENU, onSave, menuFile.AppendItem(miSave))

menuFile.AppendSeparator()

miImport = wx.MenuItem(menuFile,-1,'&Import\tAlt+I','Import')
def onImport(e): pass
frmMain.Bind(wx.EVT_MENU, onImport, menuFile.AppendItem(miImport))

miExport = wx.MenuItem(menuFile,-1,'&Export\tAlt+E','Export')
def onExport(e): pass
frmMain.Bind(wx.EVT_MENU, onExport, menuFile.AppendItem(miExport))

menuFile.AppendSeparator()

miQuit = wx.MenuItem(menuFile,-1,'&Quit\tAlt+Q','Quit')
def onQuit(e): frmMain.Close()
frmMain.Bind(wx.EVT_MENU, onQuit, menuFile.AppendItem(miQuit))

menuDraw = wx.Menu()
menu.Append(menuDraw,'&Draw')

miPoint = wx.MenuItem(menuDraw,-1,'&Point\tAlt+P','Point')
def onPoint(e): pass
frmMain.Bind(wx.EVT_MENU, onPoint, menuDraw.AppendItem(miPoint))

miLine = wx.MenuItem(menuDraw,-1,'&Line\tAlt+L','Line')
def onLine(e): pass
frmMain.Bind(wx.EVT_MENU, onLine, menuDraw.AppendItem(miLine))

miArc = wx.MenuItem(menuDraw,-1,'A&rc\tAlt+C','Arc')
def onArc(e): pass
frmMain.Bind(wx.EVT_MENU, onArc, menuDraw.AppendItem(miArc))

miSpline = wx.MenuItem(menuDraw,-1,'Spline','Spline')
def onSpline(e): pass
frmMain.Bind(wx.EVT_MENU, onSpline, menuDraw.AppendItem(miSpline))

menuDraw.AppendSeparator()

miBlock = wx.MenuItem(menuDraw,-1,'Block','Block')
def onBlock(e): pass
frmMain.Bind(wx.EVT_MENU, onBlock, menuDraw.AppendItem(miBlock))

miExplode = wx.MenuItem(menuDraw,-1,'Explode','Explode')
def onExplode(e): pass
frmMain.Bind(wx.EVT_MENU, onExplode, menuDraw.AppendItem(miExplode))

miOffset = wx.MenuItem(menuDraw,-1,'Offset','Offset')
def onOffset(e): pass
frmMain.Bind(wx.EVT_MENU, onOffset, menuDraw.AppendItem(miOffset))

miCopy = wx.MenuItem(menuDraw,-1,'Copy','Copy')
def onCopy(e): pass
frmMain.Bind(wx.EVT_MENU, onCopy, menuDraw.AppendItem(miCopy))

miMirror = wx.MenuItem(menuDraw,-1,'Mirror','Mirror')
def onMirror(e): pass
frmMain.Bind(wx.EVT_MENU, onMirror, menuDraw.AppendItem(miMirror))

miArray = wx.MenuItem(menuDraw,-1,'Array','Array')
def onArray(e): pass
frmMain.Bind(wx.EVT_MENU, onArray, menuDraw.AppendItem(miArray))

menuDraw.AppendSeparator()

miDim = wx.MenuItem(menuDraw,-1,'Di&mension\tAlt+M','Dimension')
def onDim(e): pass
frmMain.Bind(wx.EVT_MENU, onDim, menuDraw.AppendItem(miDim))

miVar = wx.MenuItem(menuDraw,-1,'Variable','Variable')
def onVar(e): pass
frmMain.Bind(wx.EVT_MENU, onVar, menuDraw.AppendItem(miVar))

miEq = wx.MenuItem(menuDraw,-1,'Equation','Equation')
def onEq(e): pass
frmMain.Bind(wx.EVT_MENU, onEq, menuDraw.AppendItem(miEq))

menuDraw.AppendSeparator()

miCoincide = wx.MenuItem(menuDraw,-1,'Coincide','Constraint: Coincide')
def onCoincide(e): pass
frmMain.Bind(wx.EVT_MENU,onCoincide,menuDraw.AppendItem(miCoincide))

miHorizontal = wx.MenuItem(menuDraw,-1,'Horizontal','Constraint: Horizontal')
def onHorizontal(e): pass
frmMain.Bind(wx.EVT_MENU, onHorizontal, menuDraw.AppendItem(miHorizontal))

miVertical = wx.MenuItem(menuDraw,-1,'Vertical','Constraint: Vertical')
def onVertical(e): pass
frmMain.Bind(wx.EVT_MENU, onVertical, menuDraw.AppendItem(miVertical))

miTangent = wx.MenuItem(menuDraw,-1,'Tangent','Constraint: Tangent')
def onTangent(e): pass
frmMain.Bind(wx.EVT_MENU, onTangent, menuDraw.AppendItem(miTangent))

miMidpoint = wx.MenuItem(menuDraw,-1,'Midpoint','Constraint: Midpoint')
def onMidpoint(e): pass
frmMain.Bind(wx.EVT_MENU, onMidpoint, menuDraw.AppendItem(miMidpoint))

miParallel = wx.MenuItem(menuDraw,-1,'Parallel','Constraint: Parallel')
def onParallel(e): pass
frmMain.Bind(wx.EVT_MENU, onParallel, menuDraw.AppendItem(miParallel))

miPerpendicular = wx.MenuItem(menuDraw,-1,'Perpendicular','Constraint: Perpendicular')
def onPerpendicular(e): pass
frmMain.Bind(wx.EVT_MENU, onPerpendicular, menuDraw.AppendItem(miPerpendicular))

miAngle = wx.MenuItem(menuDraw,-1,'Angle','Constraint: Angle')
def onAngle(e): pass
frmMain.Bind(wx.EVT_MENU, onAngle, menuDraw.AppendItem(miAngle))

menuView = wx.Menu()
menu.Append(menuView,'&View')

miRefresh = wx.MenuItem(menuView,-1,'&Refresh\tAlt+R','Refresh screen')
def onRefresh(e):
    onTreeRefresh(None)
    canvas.Refresh()
frmMain.Bind(wx.EVT_MENU, onRefresh, menuView.AppendItem(miRefresh))

menuDraw = wx.Menu()
menu.Append(menuDraw,'Calc')

menuDraw = wx.Menu()
menu.Append(menuDraw,'Render')

menuDraw = wx.Menu()
menu.Append(menuDraw,'Machine')

menuHelp = wx.Menu()
menu.Append(menuHelp,'&Help')

miManual = wx.MenuItem(menuHelp,-1,'&Manual','Manual')
def onManual(e): pass
frmMain.Bind(wx.EVT_MENU, onManual, menuHelp.AppendItem(miManual))

miAbout = wx.MenuItem(menuHelp,-1,'&About','About')
def onAbout(e): wx.MessageBox(open('README.txt','r').read())
frmMain.Bind(wx.EVT_MENU, onAbout, menuHelp.AppendItem(miAbout))

# splitters

splV = wx.SplitterWindow(frmMain)
splH = wx.SplitterWindow(splV)

# objtree

tree = wx.TreeCtrl(splH)
tree.BackgroundColour=COLOR.LIGHTCYAN

# canvas

canvas = wx.Panel(splH,-1)
canvas.BackgroundColour=COLOR.BLUEPRINT
canvas.Bind(wx.EVT_ENTER_WINDOW, lambda e:canvas.SetFocus())

class PEN:
    def __init__(self,color,width):
        self.C,self.W=color,width
PEN_POINT=PEN(COLOR.YELLOW,7)
PEN_LINE =PEN(COLOR.WHITE,1)

ZOOM = 1.0
def onPaint(e):
    W,H=canvas.GetClientSize() ; X0,Y0=W/2,H/2
    dc = wx.AutoBufferedPaintDC(canvas)
    # clear
    dc.SetBackground(wx.Brush(canvas.BackgroundColour)) ; dc.Clear()
    # draw origin
    dc.SetPen(wx.Pen('RED'  ,2)) ; dc.DrawLine(X0,Y0,X0+10,Y0)
    dc.SetPen(wx.Pen('GREEN',2)) ; dc.DrawLine(X0,Y0,X0,Y0-10)
    # draw geom
    for i in DAT['Geom']:
        X,Y=i.X,i.Y
        dc.SetPen(wx.Pen(PEN_POINT.C,PEN_POINT.W))
        dc.DrawCircle(X0+X*ZOOM,Y0-Y*ZOOM,1)
canvas.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
canvas.Bind(wx.EVT_PAINT, onPaint)

# python shell

shell = wx.py.shell.Shell(splV)
shell.Bind(wx.EVT_ENTER_WINDOW, lambda e:shell.setFocus())

# project data

class POINT:
    def __init__(self,X,Y,Name=''):
        self.X,self.Y,self.Name=X,Y,Name
    def __str__(self): return 'P:%s(%s,%s)'%(self.Name,self.X,self.Y)

FileName=None
RP=[]
for i in range(10):
    RP+=[POINT(random.randint(-100,+100),random.randint(-100,+100))]
    
DAT={
     'Title':'Empty Project',
     'Author':'User Name',
     'Date':time.localtime()[:6],
     'Geom':RP
     }

# events

def onResize(e):
    W,H=frmMain.GetClientSize()
    splV.SetSashPosition(H*4/5)
    splH.SetSashPosition(W*1/6)
    
def onTreeRefresh(e):
    tree.DeleteAllItems()
    root=tree.AddRoot(str(FileName))
    tree.SetItemHasChildren(root)
    for i in DAT:
        T=DAT[i]
        if type(T)==type([]) or type(T)==type({}):
            D=tree.AppendItem(root,i)
            tree.SetItemHasChildren(D)
            for j in DAT[i]:
                tree.AppendItem(D,str(j))
                
        else:
            tree.AppendItem(root,'%s : %s'%(i,T))
    tree.ExpandAll()
onTreeRefresh(None)

def onMove(e):
    W,H=canvas.GetClientSize() ; X0,Y0=W/2,H/2
    Xpt,Ypt=e.GetPositionTuple()
    status.SetStatusText('X:%.2f Y:%.2f'%((Xpt-X0)/ZOOM,(Y0-Ypt)/ZOOM))
canvas.Bind(wx.EVT_MOTION, onMove)

def onScroll(e): 
    global ZOOM
    if e.GetWheelRotation()>0:
        ZOOM*=1.2
    else:
        ZOOM*=0.7
    canvas.Refresh()

canvas.Bind(wx.EVT_MOUSEWHEEL,onScroll)

# canvas.Bind(wx.EVT_PAINT,onPaint)
# canvas.Bind(wx.EVT_SIZE,onResize)
# canvas.Bind(wx.EVT_MOTION,onMove)
# canvas.Bind(wx.EVT_LEFT_DOWN,onLeftDown)    

# mainloop

splH.SplitVertically(tree,canvas)
splV.SplitHorizontally(splH,shell)
# frmMain.Bind(wx.EVT_SIZE, onResize)
onResize(None)
shell.setFocus()
app.MainLoop()
