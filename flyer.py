#! usr/bin/env python
RES_OPT = 1
CLOSE_OPT = 2
import wx
import math
class WindowUI(wx.Frame):
	def __init__(self, titlestr,sizetuple, postuple):
		super(WindowUI, self).__init__(None, -1, title = titlestr, size = sizetuple, style = wx.DEFAULT_FRAME_STYLE, pos = postuple)
		self.counter = 0
		self.n = 1
		self.GeneralUI()
		self.Show(True)
	def GeneralUI(self):
#		pass
#diseno de el menu
		menubar = wx.MenuBar()
		filemenu = wx.Menu()
		resopt = wx.MenuItem(filemenu,RES_OPT,'&Reset Count\tReset')
		resopt.SetBitmap(wx.Bitmap('res/reseter.png'))
		closeopt = wx.MenuItem(filemenu,CLOSE_OPT,'&Quit\tQuit ')
		closeopt.SetBitmap(wx.Bitmap('res/close.png'))
		filemenu.AppendItem(resopt)
		filemenu.AppendItem(closeopt)

		viewmenu = wx.Menu()

		self.dis_status_check = viewmenu.Append(wx.ID_ANY,'Disable Status', 'Disable Status', kind = wx.ITEM_CHECK)

		viewmenu.Check(self.dis_status_check.GetId(),False)
		menubar.Append(filemenu,'&File')
		menubar.Append(viewmenu,'&View')
		self.SetMenuBar(menubar)
#diseno toolbar
		self.toolbox = wx.BoxSizer(wx.VERTICAL)
		self.toolbar1 = wx.ToolBar(self)
		#muy util para no hacer resize a imagenes
		self.toolbar1.SetToolBitmapSize((50,50))
		plus1 = self.toolbar1.AddLabelTool(wx.ID_ANY,'+1',wx.Bitmap('res/plus1.png'))
		min1 = self.toolbar1.AddLabelTool(wx.ID_ANY,'-1',wx.Bitmap('res/min1.png'))
		self.toolbar1.AddSeparator()
		plusN = self.toolbar1.AddLabelTool(wx.ID_ANY, '+n',wx.Bitmap('res/plusN.png'))
		minN = self.toolbar1.AddLabelTool(wx.ID_ANY,'-n',wx.Bitmap('res/minN.png'))
		resetool = self.toolbar1.AddLabelTool(wx.ID_ANY,'Reset counter', wx.Bitmap('res/reset.png'))
		self.toolbar1.Realize()

		self.toolbar2 =	wx.ToolBar(self)
		self.toolbar2.SetToolBitmapSize((50,50))
		showtool = self.toolbar2.AddLabelTool(wx.ID_ANY,'show counter',wx.Bitmap('res/show.png'))
		tantool = self.toolbar2.AddLabelTool(wx.ID_ANY,'tan()',wx.Bitmap('res/tan.png', wx.BITMAP_TYPE_PNG))
		self.toolbar2.Realize()

		self.toolbox.Add(self.toolbar1,0,wx.EXPAND)
		self.toolbox.Add(self.toolbar2,0,wx.EXPAND)		
		self.SetSizer(self.toolbox)
#status bar
		self.statbar = self.CreateStatusBar()
		self.statbar.Show()
		self.statbar.SetStatusText(str(self.counter))
#Conexion de eventos
		self.Bind(wx.EVT_MENU,self.reset,resopt)
		self.Bind(wx.EVT_MENU,self.quit,closeopt)
		self.Bind(wx.EVT_MENU,self.disable_status , self.dis_status_check)

		self.Bind(wx.EVT_TOOL,self.add_one , plus1)
		self.Bind(wx.EVT_TOOL,self.substract_one, min1)
		self.Bind(wx.EVT_TOOL,self.add_N, plusN)
		self.Bind(wx.EVT_TOOL,self.substract_n,minN)
		self.Bind(wx.EVT_TOOL,self.reset, resetool)
		self.Bind(wx.EVT_TOOL,self.show_c, showtool)
		self.Bind(wx.EVT_TOOL,self.tan_f, tantool)
		self.Bind(wx.EVT_RIGHT_DOWN,self.clicderecho)
#eventos		
	def reset(self,e):
		self.counter = 0
		self.statbar.SetStatusText(str(self.counter))
	def quit(self,e):
		self.Close()
	def disable_status(self,e):
		self.statbar.Hide()
	def add_one(self,e):
		self.counter += 1
		self.s()
	def substract_one(self,e):
		self.counter -=1
		self.s()
	def add_N(self,e):
		self.counter += self.n
		self.s()
	def substract_n(self,e):
		self.counter -= self.n	
		self.s()
	def show_c(self,e):
		self.toolbar1.EnableTool(wx.ID_ANY, True)
		self.statbar.Show()
	def tan_f(self,e):		
		self.statbar.SetStatusText(str(math.tan(self.counter)))
	def s(self):
		self.statbar.SetStatusText(str(self.counter))
	def clicderecho(self,e):
		self.PopupMenu(PopUpMenuUI(self), e.GetPosition())		
#pop up aislado
class PopUpMenuUI(wx.Menu):
	def __init__(self, parent):
		super(PopUpMenuUI, self).__init__()
		self.parent = parent
		popupmen = wx.Menu()
		quick_quit = wx.MenuItem(self,wx.NewId(),'Close')
		self.AppendItem(quick_quit)
		info = wx.MenuItem(self,wx.NewId(),'About')
		self.AppendItem(info)
		self.Bind(wx.EVT_MENU,self.close,quick_quit)
		self.Bind(wx.EVT_MENU,self.info,info)
	def info(self,e):
		pass	
	def close(self,e):
		self.parent.Close()		
						
if __name__ == '__main__':
	application = wx.App()
	WindowUI('flyer', (400,500),(30,30))
	application.MainLoop()		
		