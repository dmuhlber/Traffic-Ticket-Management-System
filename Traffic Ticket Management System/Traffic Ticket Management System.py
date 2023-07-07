import wx
import sqlite3 as db

#---------------------------------------------ticket entry box-------------------------------------------
class MyDialog(wx.Dialog):    
    def __init__(self):
        
        wx.Dialog.__init__(self, None, title="Dialog", size=(470, 300))

        lbl = wx.StaticText(self, label='Ticket Record Entry', pos=(190, 10))

        self.tid = wx.TextCtrl(self, -1, '', pos=(98, 40))
        wx.StaticText(self, -1, 'Ticket ID:', pos=(45, 45))

        self.time = wx.TextCtrl(self, -1, '', (98, 80))
        wx.StaticText(self, -1, 'Time:', (65, 85))

        self.ps = wx.TextCtrl(self, -1, '', (98, 120))
        wx.StaticText(self, -1, 'Posted Speed:', (20, 125))

        self.age = wx.TextCtrl(self, -1, '', (98, 160))
        wx.StaticText(self, -1, 'Age:', (70, 165))

        self.date = wx.TextCtrl(self, -1, '', pos=(305, 40))
        wx.StaticText(self, -1, 'Date:', pos=(275, 45))

        self.asp = wx.TextCtrl(self, -1, '', pos=(305, 80))
        wx.StaticText(self, -1, 'Actual Speed:', pos=(230, 85))

        self.mph = wx.TextCtrl(self, -1, '', pos=(305, 120))
        wx.StaticText(self, -1, 'MPH Over:', pos=(245, 125))

        self.sex = wx.TextCtrl(self, -1, '', pos=(305, 160))
        wx.StaticText(self, -1, 'Sex:', pos=(280, 165))

        okBtn = wx.Button(self, id=wx.ID_OK, pos=(200, 200)) #add ok button to ticket entry

#------------------------------------------data table---------------------------------------------------
class DataList(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(635, 590))
        panel = wx.Panel(self, size=(440, 575))

        self.table_name = wx.StaticText(panel, -1, 'Citation Data', pos=(285,5))
        self.list = wx.ListCtrl(panel, -1, style=wx.LC_REPORT, pos=(20, 30), size=(574, 450))
        
        # set up column width
        self.list.InsertColumn(0, 'tid', width=40)
        self.list.InsertColumn(1, 'stop_date', width=70)
        self.list.InsertColumn(2, 'stop_time', width=70)
        self.list.InsertColumn(3, 'actual_speed', width=80)
        self.list.InsertColumn(4, 'posted_speed', width=84)
        self.list.InsertColumn(5, 'mph_over', width=90)
        self.list.InsertColumn(6, 'age', width=40)
        self.list.InsertColumn(7, 'violator_sex', wx.LIST_FORMAT_LEFT, 80)

        # set up buttons
        display = wx.Button(panel, -1, 'Display', size=(-1, 30), pos=(100, 500))
        insert = wx.Button(panel, -1, 'Insert Citation', size=(-1, 30), pos=(260, 500))
        cancel = wx.Button(panel, -1, 'Cancel', size=(-1, 30), pos=(420, 500))

        display.Bind(wx.EVT_BUTTON, self.OnDisplay)
        insert.Bind(wx.EVT_BUTTON, self.OnAdd)
        cancel.Bind(wx.EVT_BUTTON, self.OnCancel)

        self.Centre()

    def getAllData(self):

        self.list.DeleteAllItems()
        con = db.connect('speeding_tickets.db')
        cur = con.cursor()

        cur.execute('SELECT * FROM tickets')
        results = cur.fetchall()
        for row in results:
            self.list.Append(row)

        cur.close()
        con.close()
#-------------------------------Display Button----------------------------------------------
    def OnDisplay(self, event):

        try:
            self.getAllData()

        except db.Error as error:
            dlg = wx.MessageDialog(self, str(error), 'Error occured')
            dlg.ShowModal()
#-------------------------------Opens Dialog Box------------------------------------------
    def OnAdd(self, event):
        dlg = MyDialog()
        btnID = dlg.ShowModal()
        if btnID == wx.ID_OK:
            tid = dlg.tid.GetValue()
            time = dlg.time.GetValue()
            ps = dlg.ps.GetValue()
            age = dlg.age.GetValue()
            date = dlg.date.GetValue()
            asp = dlg.asp.GetValue()
            mph = dlg.mph.GetValue()
            sex = dlg.sex.GetValue()

        if tid != "" and time != "" and ps != "" and age != "" and date != "" and asp != "" and mph != "" and sex != "":

            try:
                con = db.connect('speeding_tickets.db')  # connect to db
                cur = con.cursor()

                sql = "INSERT INTO tickets VALUES (?, ?, ?, ?, ?, ?, ?, ?)"

                cur.execute(sql, (tid, time, ps, age, date, asp, mph, sex))
                con.commit()

                self.getAllData()

            except db.Error as error:
                dlg = wx.MessageDialog(self, str(error), 'Error occured')
                dlg.ShowModal()

        dlg.Destroy()
        
#----------------------------------Cancel Button------------------------------------------------
    def OnCancel(self, event):
        self.Close()  # closes window


app = wx.App()
dl = DataList(None, -1, 'Traffic Tickets')
dl.Show()
app.MainLoop()
