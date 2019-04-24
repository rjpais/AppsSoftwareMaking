%%%%

This code was written for the Explanation of Class communication between
Panels and Frames using Wx.Python package for designing User Interface Software.

%%%%
'''

import wx                                                                       ### A package to use wx.Python functions in the package

#=====================================================================================================================================Start of Class Mypanel

class MyPanel(wx.Panel):                                                        ### Creates the Class named MyPanel that holds function from wx.Python .. wx.Panel

   def __init__(self, parent, title):                                           ### Function that is repeated when class is called. wx.Panel generates a panel that is referenced by self and a variable is generated to give to the class
      super(MyPanel, self).__init__(parent, title = title)                      ### Uses the variables passed to it when class was called. This case a title was passed called 'Title' when the class was called
      button = wx.Button(self, label = 'Label', pos = (x-value, y-value))       ### Generates a button with a name label
      button.Bind(wx.EVT_BUTTON, self.function2)                                ### binds this button to the function2 within the panel
      self.Bind(wx.EVT_BUTTON, self.function1)                                  ### binds this button to the function1 and passed to the Example class
                                                                                ### which is the Frame by the use of self
   def function1(self, e):

      print ('Panel received click event. propagated to Frame class')
      e.Skip()                                                                  ### Continue to pass

   def function2(self,e):
      print ("Button received click event. propagated to Panel class")
      e.Skip()                                                                  ### Continue to pass

#=====================================================================================================================================End of Class MyPanel
#=====================================================================================================================================Start of Class Example

class Example(wx.Frame):                                                        ### Creates the Class named Example that holds function from wx.Python .. wx.Frame

   def __init__(self,parent, title):                                            ### Function that is repeated when class is called. wx.Frame generates a Frame that is referenced by self and a variable is generated to give to the class called title
      super(Example, self).__init__(parent, title = title)                      ### Uses the variables passed to it when class was called. This case a title was passed called 'Title' when the class was called
      self.Move()                                                               ### Looks for class function Move.
      self.InitUI()                                                             ### Run function in class. Self is used to say look in this class

   def InitUI(self):

      mpnl = MyPanel(self)                                                      ### Calls the class MyPanel and puts it under variable mpnl
      self.Bind(wx.EVT_BUTTON, self.function1)                                  ### binds this button to the function1 and passed to the Example class
                                                                                ### which is the Frame by the use of self

      self.SetTitle('Title of Frame')                                           ### sets title of frame
      self.Centre()                                                             ### centers the title
      self.Show(True)                                                           ### show the frame

   def NewWIn(self):                                                            ### Creates a new function
       new = Mypanel(self)                                                      ### calls class Mypanel and put in under a variable new
       self.Bind(wx.EVT_MOVE, self.OnMove)                                      ### bind the frame to a build in function EVT_MOVE to the function onMove
       self.SetSize((x-value, y-value))                                         ### Sets size of the panel
       self.SetTitle('Move event')                                              ### Sets the title
       self.Centre()                                                            ### Centers the frame
       self.Show(True)                                                          ### Shows the frame

   def function1(self, e):                                                      ### propagated the event from the Panel class
      print ('click event received by frame class')                             ### prints click was received by frame class from panel class
      e.Skip()                                                                  ### continue if event was not received

   def Move(self):                                                              ### generates a function Move
      self.Bind(wx.EVT_MOVE, self.OnMove)                                       ### using self if bind the frame to the wx.Python function (wx.EVT_MOVE) which checks if it was moved and passes it to OnMove
      self.SetSize((x-value, y-value))                                          ### Sets the size of frame
      self.SetTitle('Move event')                                               ### Title
      self.Centre()
      self.Show(True)

   def OnMove(self, e):                                                         ### Generated a function OnMove
      x, y = e.GetPosition()                                                    ### gets two variables from GetPosition from the event click 'e'
      print ("current window position x = ",x," y= ",y)                         ### Print position

#===================================================================================================================================== End of Class Example
ex = wx.App()                                                                   ### makes a variable ex that generates the use of wx.Python commands to generates a user Interface
Example(None, title = 'Title')                                                  ### Calls class Example which generates a frame that has a variable title
ex.MainLoop()                                                                   ### Runs the wx.App



'''
This is used to explain the uses and functionality of wx.Python for generating different cases of user Interface software.
Some code was written just for explaination purposes and would not run in a console if executed.

Classes where demonstrated to show the ability to easily pass attributes between different classes.
This example was demonstrated using wx.Python but the understanding of classes could be passed on to different areas.
'''
