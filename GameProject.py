import wx
import wx.lib.buttons as buttons
import sys, os
from english_words import english_words_lower_set as wordset
import random
import wx.lib.inspection as insp



class tiktac(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.toggled = False
        self.playerwins = False
        self.counter = 0
        self.layout()
    #initialize panel
    def layout(self):
        self.btn = wx.Button(self, -1, "Return to Title", (345, 500))
        sizer = wx.BoxSizer(wx.VERTICAL)
        size = (100,100)
        self.turn = wx.StaticText(self)
        font = wx.Font(18, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        self.button1 = buttons.GenToggleButton(self, size=size)
        self.button2 = buttons.GenToggleButton(self, size=size)
        self.button3 = buttons.GenToggleButton(self, size=size)
        self.button4 = buttons.GenToggleButton(self, size=size)
        self.button5 = buttons.GenToggleButton(self, size=size)
        self.button6 = buttons.GenToggleButton(self, size=size)
        self.button7 = buttons.GenToggleButton(self, size=size)
        self.button8 = buttons.GenToggleButton(self, size=size)
        self.button9 = buttons.GenToggleButton(self, size=size)
        self.grid = [self.button1, self.button2, self.button3,
                        self.button4, self.button5, self.button6,
                        self.button7, self.button8, self.button9]
        #create buttons and arrange in crid
        self.res = wx.Button(self, 0, "Reset Game")
        self.ann = wx.StaticText(self,1,"", (195,340))
        self.ann.SetFont(font)
        self.res.Bind(wx.EVT_BUTTON, self.reset)

        for button in self.grid:
            button.Bind(wx.EVT_BUTTON, self.onToggle)
            button.SetBackgroundColour("Grey")
        #bind buttons to toggle and bind reset game button
        self.winCond = [(self.button1, self.button2, self.button3),
                        (self.button4, self.button5, self.button6),
                        (self.button7, self.button8, self.button9),

                        (self.button1, self.button5, self.button9),
                        (self.button3, self.button5, self.button7),

                        (self.button1, self.button4, self.button7),
                        (self.button2, self.button5, self.button8),
                        (self.button3, self.button6, self.button9)]

        self.fgSizer = wx.FlexGridSizer(rows=3, cols=3, vgap=5, hgap=5)
        self.fgSizer.AddMany(self.grid)
        sizer.Add(self.fgSizer, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(self.btn, flag=wx.ALIGN_CENTER_HORIZONTAL)
        sizer.Add(self.ann,1, flag=wx.ALL|wx.ALIGN_CENTER_HORIZONTAL)
        sizer.Add(self.res,0, wx.ALIGN_CENTER_HORIZONTAL|wx.BOTTOM, 10)
        self.SetSizer(sizer)
        #add all elements to sizer

    def onToggle(self, event):
        self.counter+=1
        evt = event.GetEventObject()
        fonts = wx.Font(20, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_MAX, wx.FONTWEIGHT_BOLD)
        if self.counter == 1:
            evt.SetLabel("X")
            evt.SetFont(fonts)
        if self.counter == 2:
            evt.SetLabel("O")
            evt.SetFont(fonts)
        if self.counter == 3:
            evt.SetLabel("X")
            evt.SetFont(fonts)
        if self.counter == 4:
            evt.SetLabel("O")
            evt.SetFont(fonts)
        if self.counter == 5:
            evt.SetLabel("X")
            evt.SetFont(fonts)
        if self.counter == 6:
            evt.SetLabel("O")
            evt.SetFont(fonts)
        if self.counter == 7:
            evt.SetLabel("X")
            evt.SetFont(fonts)
        if self.counter == 8:
            evt.SetLabel("O")
            evt.SetFont(fonts)
        if self.counter == 9:
            evt.SetLabel("X")
            evt.SetFont(fonts)
        #set X or O on click based on click counter
        self.checkWin()
        if self.counter%2==0:
            if self.checkWin() is True:
                self.ann.SetLabel("The O Team Wins!")
        elif self.checkWin() is True and self.counter%2!=0:
            self.ann.SetLabel("The X Team Wins!")
        #check for win on toggle and check counter for which team last played
        if not self.toggled:
            self.toggled = True

        for btn in self.grid:
            if btn.GetLabel():
                btn.Disable()
        #if button has label then disable button so can't click twice
    def reset(self, event):
        for b in self.grid:
            b.SetLabel("")
            b.SetValue(False)
            b.SetBackgroundColour("Grey")
        self.ann.SetLabel("")
        self.toggled = False
        self.playerwins = False
        self.enableButtons()
        self.counter = 0
    #reset game by setting everything back to default
    def checkWin(self):
        for button1, button2, button3 in self.winCond:
            if button1.GetLabel() == button2.GetLabel() and \
               button2.GetLabel() == button3.GetLabel() and \
               button1.GetLabel() != "":
                button1.SetBackgroundColour("Red")
                button2.SetBackgroundColour("Red")
                button3.SetBackgroundColour("Red")
                for btn in self.grid:
                    btn.Disable()
                self.Layout()
                return True
        #check for three in a row and if so set those to red background and disable all buttons

    def enableButtons(self):
        for button in self.grid:
            if button.GetLabel() == "":
                button.Enable()
        self.Refresh()
        self.Layout()
     #on reset button enable all buttons in grid and layout


class intro(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self, parent=parent)
        self.btn = wx.Button(self, 2, "Start Game", (345, 600))
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer2 = wx.BoxSizer(wx.HORIZONTAL)
        centeredLabel = wx.StaticText(self, -1, 'Tic - Tac - Toe !')
        font = wx.Font(20, family = wx.FONTFAMILY_MODERN, style = 0, weight = 90,underline = False, faceName ="", encoding = wx.FONTENCODING_DEFAULT)
        sizer.Add(centeredLabel, flag=wx.ALIGN_CENTER_HORIZONTAL)
        sizer.Add(self.btn, 1,flag=wx.ALIGN_CENTER_HORIZONTAL)
        centeredLabel.SetFont(font)
        #intro screen title with sizer and font and start button

        self.result=wx.StaticText(self)
        self.result.SetLabel("This game of tic-tac-toe is simple, take turns and try to get three in a row!")
        sizer.Add(self.result,1,wx.ALL|wx.CENTER,5)
        self.SetSizer(sizer)
        self.Fit()
    #title static text, start game button, rules description, everything centered


class hangman(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        self.tries = 7
        self.word = self.setword()
        self.layout()
        self.word_complete = "_" * len(self.word)
        self.wrdcom.SetLabel(self.word_complete)
    #global varaibles def and create word gap and call layout
    def layout(self):
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        centeredLabel = wx.StaticText(self, -1, 'Hang - Man')
        self.instruction = wx.StaticText(self, 0, 'Guess Letter or Word:')
        self.guess_box = wx.TextCtrl(self, 0, size=(100,25))
        self.go = wx.Button(self, 1, 'Guess')
        self.reset = wx.Button(self,1,'Restart Game')
        self.feedback = wx.StaticText(self, 1, '')
        self.wrdcom = wx.StaticText(self, 1, '')
        self.ret = wx.Button(self, 1, "Return to Title")

        self.go.Bind(wx.EVT_BUTTON, self.guess_button)
        self.reset.Bind(wx.EVT_BUTTON, self.resets)

        #set all elements texts, label, and buttons then bind buttons

        self.hang = wx.Bitmap(self.resource_path('hangman/hang1.png'), wx.BITMAP_TYPE_ANY)
        image = self.hang.ConvertToImage()
        self.bmpp = wx.Bitmap(image.Scale(125, 125))
        self.bmp = wx.StaticBitmap(self,id=wx.ID_ANY, bitmap=self.bmpp, size=(125,125), style=0)

        self.hang2 = wx.Bitmap(self.resource_path('hangman/hang2.png'), wx.BITMAP_TYPE_ANY)
        image2 = self.hang2.ConvertToImage()
        self.bmpp2 = wx.Bitmap(image2.Scale(125, 125))
        self.bmp2 = wx.StaticBitmap(self,id=wx.ID_ANY, bitmap=self.bmpp2, size=(125,125), style=0)
        self.bmp2.Hide()

        self.hang3 = wx.Bitmap(self.resource_path('hangman/hang3.png'), wx.BITMAP_TYPE_ANY)
        image3 = self.hang3.ConvertToImage()
        self.bmpp3 = wx.Bitmap(image3.Scale(125, 125))
        self.bmp3 = wx.StaticBitmap(self,id=wx.ID_ANY, bitmap=self.bmpp3, size=(125,125), style=0)
        self.bmp3.Hide()

        self.hang4 = wx.Bitmap(self.resource_path('hangman/hang4.png'), wx.BITMAP_TYPE_ANY)
        image4 = self.hang4.ConvertToImage()
        self.bmpp4 = wx.Bitmap(image4.Scale(125, 125))
        self.bmp4 = wx.StaticBitmap(self,id=wx.ID_ANY, bitmap=self.bmpp4, size=(125,125), style=0)
        self.bmp4.Hide()

        self.hang5 = wx.Bitmap(self.resource_path('hangman/hang5.png'), wx.BITMAP_TYPE_ANY)
        image5 = self.hang5.ConvertToImage()
        self.bmpp5 = wx.Bitmap(image5.Scale(125, 125))
        self.bmp5 = wx.StaticBitmap(self,id=wx.ID_ANY, bitmap=self.bmpp5, size=(125,125), style=0)
        self.bmp5.Hide()

        self.hang6 = wx.Bitmap(self.resource_path('hangman/hang6.png'), wx.BITMAP_TYPE_ANY)
        image6 = self.hang6.ConvertToImage()
        self.bmpp6 = wx.Bitmap(image6.Scale(125, 125))
        self.bmp6 = wx.StaticBitmap(self,id=wx.ID_ANY, bitmap=self.bmpp6, size=(125,125), style=0)
        self.bmp6.Hide()

        self.hang7 = wx.Bitmap(self.resource_path('hangman/hang7.png'), wx.BITMAP_TYPE_ANY)
        image7 = self.hang7.ConvertToImage()
        self.bmpp7 = wx.Bitmap(image7.Scale(125, 125))
        self.bmp7 = wx.StaticBitmap(self,id=wx.ID_ANY, bitmap=self.bmpp7, size=(125,125), style=0)
        self.bmp7.Hide()

        self.hang8 = wx.Bitmap(self.resource_path('hangman/hang8.png'), wx.BITMAP_TYPE_ANY)
        image8 = self.hang8.ConvertToImage()
        self.bmpp8 = wx.Bitmap(image8.Scale(125, 125))
        self.bmp8 = wx.StaticBitmap(self,id=wx.ID_ANY, bitmap=self.bmpp8, size=(125,125), style=0)
        self.bmp8.Hide()

        #create sized static bitmap from image in folder and hide all but first

        font = wx.Font(20, family = wx.FONTFAMILY_MODERN, style = 0, weight = 90,underline = True, faceName ="", encoding = wx.FONTENCODING_DEFAULT)
        self.wrdcom.SetFont(font)

        self.sizer.Add(centeredLabel, flag=wx.ALIGN_CENTER_HORIZONTAL)

        self.sizer.Add(self.bmp, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 10)
        self.sizer.Add(self.bmp2, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 10)
        self.sizer.Add(self.bmp3, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 10)
        self.sizer.Add(self.bmp4, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 10)
        self.sizer.Add(self.bmp5, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 10)
        self.sizer.Add(self.bmp6, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 10)
        self.sizer.Add(self.bmp7, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 10)
        self.sizer.Add(self.bmp8, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 10)
        self.sizer.Add(self.wrdcom, 1, wx.ALIGN_CENTER_HORIZONTAL)
        self.sizer.Add(self.instruction, 2, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL)
        self.sizer.Add(self.guess_box, 1,wx.ALIGN_CENTER_HORIZONTAL)
        self.sizer.Add(self.feedback,1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL,5)
        self.sizer.Add(self.go,1,  wx.ALIGN_CENTER_HORIZONTAL)
        self.sizer.Add(self.reset, 1, wx.ALIGN_CENTER_HORIZONTAL)
        self.sizer.Add(self.ret, 2, wx.ALIGN_CENTER_HORIZONTAL)
        self.SetSizer(self.sizer)
        self.Fit()

        #add all bitmaps to sizer and all elements as well

    def sethang(self):
        if self.tries == 7:
            self.bmp.Show()
        elif self.tries == 6:
            self.bmp.Hide()
            self.bmp2.Show()
            self.Layout()
        elif self.tries == 5:
            self.bmp2.Hide()
            self.bmp3.Show()
            self.Layout()
        elif self.tries == 4:
            self.bmp3.Hide()
            self.bmp4.Show()
            self.Layout()
        elif self.tries == 3:
            self.bmp4.Hide()
            self.bmp5.Show()
            self.Layout()
        elif self.tries == 2:
            self.bmp5.Hide()
            self.bmp6.Show()
            self.Layout()
        elif self.tries == 1:
            self.bmp6.Hide()
            self.bmp7.Show()
            self.Layout()
        elif self.tries == 0:
            self.bmp7.Hide()
            self.bmp8.Show()
            self.Layout()
        #sets current bitmap phase based on counter of how many guesses player has

    def setword(self):
        counter = 0
        words = []
        while counter < 10:
            for i in wordset:
                words.append(i)
                counter +=1
        choi = random.choice(words)
        return(choi)
        #chooses word from a random selection of 10 words from enlgish words library
    def guess_button(self, word):
        print(self.word)
        print(self.tries)
        guessed = False
        guess_letters = []
        guessed_words = []
        #if word is not already guess and tries remaining
        if not guessed and self.tries > 0:
            guess = str(self.guess_box.GetValue())
            self.guess_box.SetValue('')
            #guess is the input in the guess box and guess box is emptied
            print(guess)
            if len(guess) == 1 and guess.isalpha():
                #if guess is 1 long and is a letter then check if already guessed, in word or not in word
                #if not in word tries -1 and add to guessed
                if guess in guess_letters:
                    self.feedback.SetLabel('Letter Already Guessed')
                elif guess not in self.word:
                    self.feedback.SetLabel('Letter Is Not In Word')
                    self.tries -= 1
                    guess_letters.append(guess)
                else:
                    self.feedback.SetLabel('Your guess is in the word!')
                    guess_letters.append(guess)
                    word_list = list(self.word_complete)
                    ind = [i for i, letter in enumerate(self.word) if letter == guess]
                    for index in ind:
                        word_list[index] = guess
                    self.word_complete = "".join(word_list)
                    self.wrdcom.SetLabel(self.word_complete)
                    if "_" not in self.word_complete:
                        guessed = True
                    #in the enumerate of guessed letter display if the letter is guessed set the empty space to the letter
                    #and set the label
            elif len(guess) == len(self.word) and guess.isalpha():
                #if they guess a word then do the same, if not tries - 1 and append to guesses,
                #if it is the word guessed is true and fill in blanks for word
                if guess in guessed_words:
                    self.feedback.SetLabel('Word Already Guessed')
                elif guess != self.word:
                    self.feedback.SetLabel('Your guess is not the word')
                    self.tries -= 1
                    guessed_words.append(guess)
                else:
                    guessed = True
                    self.word_complete = self.word
                    self.wrdcom.SetLabel(self.word_complete)
            else:
                #if not letter or word return not valid guess
                self.feedback.SetLabel('Not a Valid Guess')
        if guessed:
            self.feedback.SetLabel('Congrats, you guessed the word!')
        else:
            if self.tries == 0:
                self.feedback.SetLabel('You Ran out of tries The true word will be shown above')
                self.word_complete = self.word
                self.wrdcom.SetLabel(self.word_complete)
                #if no more tries then return loosing message and reveal word
        self.sethang()
        #on button click set image

    def resets(self, event):
        self.feedback.SetLabel('')
        self.tries = 7
        self.guess_box.SetValue('')
        self.wrdcom.SetLabel('')
        self.word = self.setword()
        self.word_complete = "_" * len(self.word)
        self.wrdcom.SetLabel(self.word_complete)
        self.bmp.Show()
        self.bmp2.Hide()
        self.bmp3.Hide()
        self.bmp4.Hide()
        self.bmp5.Hide()
        self.bmp6.Hide()
        self.bmp7.Hide()
        self.bmp8.Hide()
        #reset button returns all to defult and gets new word

    def resource_path(self, relative_path):
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return(os.path.join(base_path, relative_path))
    #finds path on any computer by joining absolute path in directory and relative path


class titlescreen(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self, parent=parent)
        sizer = wx.BoxSizer(wx.VERTICAL)
        centeredLabel = wx.StaticText(self, -1, 'Welcome to Game Net')
        authors = wx.StaticText(self, 0, 'Projecy by: \n Asher Reeves, Zofia Dukala, Mekhola Doha, Emma Schönborn, Eman Ansari')
        self.splayer = wx.Button(self, 1, "Single Player Games")
        self.tplayer = wx.Button(self, 1, 'Two Player Games')
        #set title and attributes and two buttons for single and multiplayer

        font = wx.Font(20, family = wx.FONTFAMILY_MODERN, style = 0, weight = 90,underline = False, faceName ="", encoding = wx.FONTENCODING_DEFAULT)
        font2 = wx.Font(15, family = wx.FONTFAMILY_MODERN, style = 0, weight = 90,underline = False, faceName ="", encoding = wx.FONTENCODING_DEFAULT)
        centeredLabel.SetFont(font)
        authors.SetFont(font2)
        #applies two fonts
        sizer.Add(centeredLabel, flag=wx.ALIGN_CENTER_HORIZONTAL)
        sizer.Add(authors, 1,wx.ALIGN_CENTER_HORIZONTAL, 5)
        sizer.Add(self.splayer, 0, wx.EXPAND)
        sizer.Add(self.tplayer, 2, wx.EXPAND)
        self.SetSizer(sizer)
        self.Fit()
        #add to sizer

class tetristitle(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self, parent=parent)
        sizer = wx.BoxSizer(wx.VERTICAL)
        title = wx.StaticText(self, 0, "Tetris")
        intructions = wx.StaticText(self, 1, "\n\n\n Press UP to rotate the block clockwise \n Press LEFT and RIGHT to move the blocks sideways \n Press DOWN to make the block move faster \n Clearing each row gives the player 10 points \n Game over, if the blocks reach the top of the grid")
        self.startbutton = wx.Button(self, 1, "Start Game")
        self.rtitle = wx.Button(self, 1, "Return To Title")

        font = wx.Font(20, family = wx.FONTFAMILY_MODERN, style = 0, weight = 90,underline = True, faceName ="", encoding = wx.FONTENCODING_DEFAULT)
        title.SetFont(font)

        sizer.Add(title, 0, wx.ALIGN_CENTER_HORIZONTAL)
        sizer.Add(intructions, 1, wx.ALIGN_CENTER_HORIZONTAL)
        sizer.Add(self.startbutton, 1, wx.ALIGN_CENTER_HORIZONTAL)
        sizer.Add(self.rtitle, 1, wx.ALIGN_CENTER_HORIZONTAL)
        self.SetSizer(sizer)
        self.Fit()
        #makes title, instructions, start game and return to title buttons and adds to sizer, applies font

class pongtitle(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self, parent=parent)
        sizer = wx.BoxSizer(wx.VERTICAL)
        title = wx.StaticText(self, 0, "Pong")
        intructions = wx.StaticText(self, 1, "\n\n\nUse the down and up keys to move the paddle and dont let the ball touch your side of the screen!")
        self.startbutton = wx.Button(self, 1, "Start Game")
        self.rtitle = wx.Button(self, 1, "Return To Title")

        font = wx.Font(20, family = wx.FONTFAMILY_MODERN, style = 0, weight = 90,underline = True, faceName ="", encoding = wx.FONTENCODING_DEFAULT)
        title.SetFont(font)

        sizer.Add(title, 0, wx.ALIGN_CENTER_HORIZONTAL)
        sizer.Add(intructions, 1, wx.ALIGN_CENTER_HORIZONTAL)
        sizer.Add(self.startbutton, 1, wx.ALIGN_CENTER_HORIZONTAL)
        sizer.Add(self.rtitle, 1, wx.ALIGN_CENTER_HORIZONTAL)
        self.SetSizer(sizer)
        self.Fit()
         #makes title, instructions, start game and return to title buttons and adds to sizer, applies font


class memorytitle(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self, parent=parent)
        sizer = wx.BoxSizer(wx.VERTICAL)
        title = wx.StaticText(self, 0, "Memory Game")
        intructions = wx.StaticText(self, 1, "\n \n \nClick each box to reveal the numbers below and try to match them all in as few turns as possible!")
        self.startbutton = wx.Button(self, 1, "Start Game")
        self.rtitle = wx.Button(self, 1, "Return To Title")

        font = wx.Font(20, family = wx.FONTFAMILY_MODERN, style = 0, weight = 90,underline = True, faceName ="", encoding = wx.FONTENCODING_DEFAULT)
        title.SetFont(font)

        sizer.Add(title, 0, wx.ALIGN_CENTER_HORIZONTAL)
        sizer.Add(intructions, 1, wx.ALIGN_CENTER_HORIZONTAL)
        sizer.Add(self.startbutton, 1, wx.ALIGN_CENTER_HORIZONTAL)
        sizer.Add(self.rtitle, 1, wx.ALIGN_CENTER_HORIZONTAL)
        self.SetSizer(sizer)
        self.Fit()

class snaketitle(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self, parent=parent)
        sizer = wx.BoxSizer(wx.VERTICAL)
        title = wx.StaticText(self, 0, "Snake")
        intructions = wx.StaticText(self, 1, "   The goal of the game of snake is to make the snake as long as possible by eating “fruits” that appear on \n   the screen. With every fruit that is eaten, the snake grows by one block. When the snake head touches the \n   edge of the screen or any part of its own body, the game is lost. In the button right the score will be counted,\n   for every fruit that is eaten the score will increase by one. \n  To play this game the player only needs the UP, DOWN, RIGHT, and LEFT buttons on the keyboard. This version \n  of snake is also programmed so that players with a German keyboard can additionally use the W,S,A,D \n  keys to move the snake on the screen.")
        self.startbutton = wx.Button(self, 1, "Start Game")
        self.rtitle = wx.Button(self, 1, "Return To Title")

        font = wx.Font(20, family = wx.FONTFAMILY_MODERN, style = 0, weight = 90,underline = True, faceName ="", encoding = wx.FONTENCODING_DEFAULT)
        title.SetFont(font)

        sizer.Add(title, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 20)
        sizer.Add(intructions, 1, wx.ALIGN_CENTER_HORIZONTAL)
        sizer.Add(self.startbutton, 1, wx.ALIGN_CENTER_HORIZONTAL)
        sizer.Add(self.rtitle, 1, wx.ALIGN_CENTER_HORIZONTAL)
        self.SetSizer(sizer)
        self.Fit()
         #makes title, instructions, start game and return to title buttons and adds to sizer, applies font
#class rockpapertitle(wx.Panel):
#    def __init__(self, parent):
#        wx.Panel.__init__(self, parent=parent)
#        sizer = wx.BoxSizer(wx.VERTICAL)
#        title = wx.StaticText(self, 0, "Rock Paper Scissors")
#        intructions = wx.StaticText(self, 1, "")
#        self.startbutton = wx.Button(self, 1, "Start Game")
#        self.rtitle = wx.Button(self, 1, "Return To Title")

#        font = wx.Font(20, family = wx.FONTFAMILY_MODERN, style = 0, weight = 90,underline = True, faceName ="", encoding = wx.FONTENCODING_DEFAULT)
#        title.SetFont(font)

#        sizer.Add(title, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 20)
#        sizer.Add(intructions, 1, wx.ALIGN_CENTER_HORIZONTAL)
#        sizer.Add(self.startbutton, 1, wx.ALIGN_CENTER_HORIZONTAL)
#        sizer.Add(self.rtitle, 1, wx.ALIGN_CENTER_HORIZONTAL)
#        self.SetSizer(sizer)
#        self.Fit()
             #makes title, instructions, start game and return to title buttons and adds to sizer, applies font
class singleplayer(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self, parent=parent)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.rtitle = wx.Button(self, 1, "Return To Title")
        title = wx.StaticText(self, 0, "Single Player Games")

        bmp = wx.Bitmap(self.resource_path('hang1.png'), wx.BITMAP_TYPE_ANY)
        image = bmp.ConvertToImage()
        bmpp = wx.Bitmap(image.Scale(75, 75))
        self.hang = wx.BitmapButton(self, id = wx.ID_ANY, bitmap = bmpp,size =(75, 75))

        bmp2 = wx.Bitmap(self.resource_path('snake.jpg'), wx.BITMAP_TYPE_ANY)
        image2 = bmp2.ConvertToImage()
        bmpp2 = wx.Bitmap(image2.Scale(75, 75))
        self.snake = wx.BitmapButton(self, id = wx.ID_ANY, bitmap = bmpp2,size =(75, 75))

        bmp3 = wx.Bitmap(self.resource_path('pong.png'), wx.BITMAP_TYPE_ANY)
        image3 = bmp3.ConvertToImage()
        bmpp3 = wx.Bitmap(image3.Scale(75, 75))
        self.pong = wx.BitmapButton(self, id = wx.ID_ANY, bitmap = bmpp3,size =(75, 75))

        bmp4 = wx.Bitmap(self.resource_path('tetris.png'), wx.BITMAP_TYPE_ANY)
        image4 = bmp4.ConvertToImage()
        bmpp4 = wx.Bitmap(image4.Scale(75, 75))
        self.tetris = wx.BitmapButton(self, id = wx.ID_ANY, bitmap = bmpp4,size =(75, 75))

        bmp5 = wx.Bitmap(self.resource_path('memory.png'), wx.BITMAP_TYPE_ANY)
        image5 = bmp5.ConvertToImage()
        bmpp5 = wx.Bitmap(image5.Scale(75, 75))
        self.memory = wx.BitmapButton(self, id = wx.ID_ANY, bitmap = bmpp5,size =(75, 75))

        self.grid = [self.hang, self.snake, self.pong, self.tetris, self.memory]
        self.fgSizer = wx.FlexGridSizer(rows=2, cols=3, vgap=10, hgap=10)
        self.fgSizer.AddMany(self.grid)
        #adds title, font return button and grid of bitmap buttons
        sizer.Add(title, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 20)
        sizer.Add(self.fgSizer, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(self.rtitle,2, wx.ALIGN_CENTER_HORIZONTAL)

        self.SetSizer(sizer)
        self.Fit()
            #adds elements to sizer

    def resource_path(self, relative_path):
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)

class twoplayer(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self, parent=parent)
        sizer = wx.BoxSizer(wx.VERTICAL)
        title = wx.StaticText(self, 0, "Two Player Games")
        self.rtitle = wx.Button(self, 1, "Return To Title")

        bmp = wx.Bitmap(self.resource_path('tic-tac-toe.jpg'), wx.BITMAP_TYPE_ANY)
        image = bmp.ConvertToImage()
        bmpp = wx.Bitmap(image.Scale(75, 75))
        self.tic = wx.BitmapButton(self, id = wx.ID_ANY, bitmap = bmpp,size =(75, 75))

#        bmp2 = wx.Bitmap(self.resource_path('rockpaper.jpg'), wx.BITMAP_TYPE_ANY)
#        image2 = bmp2.ConvertToImage()
#        bmpp2 = wx.Bitmap(image2.Scale(75, 75))
#        self.rock = wx.BitmapButton(self, id = wx.ID_ANY, bitmap = bmpp2,size =(75, 75))
        #adds title, font return button and grid of bitmap buttons
        self.grid = [self.tic,]
        self.fgSizer = wx.FlexGridSizer(rows=1, cols=2, vgap=10, hgap=10)
        self.fgSizer.AddMany(self.grid)
        sizer.Add(title, 0, wx.DOWN|wx.ALIGN_CENTER_HORIZONTAL, 20)
        sizer.Add(self.fgSizer, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(self.rtitle,2,  wx.ALIGN_CENTER_HORIZONTAL)
        self.SetSizer(sizer)
        self.Fit()
             #adds elements to sizer
    def resource_path(self, relative_path):
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)

class Frame(wx.Frame):
    def __init__(self):
        title = "Game Net"
        size = (675,450)
        wx.Frame.__init__(self,parent=None, title=title, size=size)
            #sets frame size title and initialize
        sizer = wx.BoxSizer()
        self.SetSizer(sizer)
        #creates sizer and creates an object in each panel class in the frame, then hides all exept title
        #and adds to sizer
        # binds buttons in each panel to panel change functions
        # for pygame files binds button to run file function
        self.title_screen = titlescreen(self)
        sizer.Add(self.title_screen, 1, wx.EXPAND)
        self.title_screen.splayer.Bind(wx.EVT_BUTTON, self.show_s_player)
        self.title_screen.tplayer.Bind(wx.EVT_BUTTON, self.show_t_player)

        self.oneplayer = singleplayer(self)
        sizer.Add(self.oneplayer, 1, wx.EXPAND)
        self.oneplayer.rtitle.Bind(wx.EVT_BUTTON, self.show_sp_title)
        self.oneplayer.hang.Bind(wx.EVT_BUTTON, self.show_hang)
        self.oneplayer.snake.Bind(wx.EVT_BUTTON, self.show_snake_titile)
        self.oneplayer.pong.Bind(wx.EVT_BUTTON, self.show_pong_title)
        self.oneplayer.tetris.Bind(wx.EVT_BUTTON, self.show_tetris_title)
        self.oneplayer.memory.Bind(wx.EVT_BUTTON, self.show_memory_title)
        self.oneplayer.Hide()

        self.snake = snaketitle(self)
        sizer.Add(self.snake,1, wx.EXPAND)
        self.snake.rtitle.Bind(wx.EVT_BUTTON, self.show_title_snake)
        self.snake.startbutton.Bind(wx.EVT_BUTTON, self.run_snake)
        self.snake.Hide()


        self.pong = pongtitle(self)
        sizer.Add(self.pong, 1, wx.EXPAND)
        self.pong.rtitle.Bind(wx.EVT_BUTTON, self.show_title_pong)
        self.pong.startbutton.Bind(wx.EVT_BUTTON, self.run_pong)
        self.pong.Hide()

        self.tetris = tetristitle(self)
        sizer.Add(self.tetris, 1, wx.EXPAND)
        self.tetris.rtitle.Bind(wx.EVT_BUTTON, self.show_title_tertis)
        self.tetris.startbutton.Bind(wx.EVT_BUTTON, self.run_tetris)
        self.tetris.Hide()

        self.hangman = hangman(self)
        sizer.Add(self.hangman, 1, wx.EXPAND)
        self.hangman.ret.Bind(wx.EVT_BUTTON, self.show_title_hang)
        self.hangman.Hide()

#        self.rockpaper = rockpapertitle(self)
#        sizer.Add(self.rockpaper, 1, wx.EXPAND)
#        self.rockpaper.rtitle.Bind(wx.EVT_BUTTON, self.show_title_rock)
#        self.rockpaper.startbutton.Bind(wx.EVT_BUTTON, self.run_rockpaper)
#        self.rockpaper.Hide()

        self.memory = memorytitle(self)
        sizer.Add(self.memory, 1, wx.EXPAND)
        self.memory.rtitle.Bind(wx.EVT_BUTTON, self.show_title_memory)
        self.memory.startbutton.Bind(wx.EVT_BUTTON, self.run_memory)
        self.memory.Hide()

        self.twoplayer = twoplayer(self)
        sizer.Add(self.twoplayer, 1, wx.EXPAND)
        self.twoplayer.tic.Bind(wx.EVT_BUTTON, self.show_tic_title)
#        self.twoplayer.rock.Bind(wx.EVT_BUTTON, self.show_rock)
        self.twoplayer.rtitle.Bind(wx.EVT_BUTTON, self.show_tp_title)
        self.twoplayer.Hide()

        self.panel_one = intro(self)
        sizer.Add(self.panel_one, 1, wx.EXPAND)
        self.panel_one.btn.Bind(wx.EVT_BUTTON, self.show_tic_game)
        self.panel_one.Hide()

        self.panel_two = tiktac(self)
        sizer.Add(self.panel_two, 1, wx.EXPAND)
        self.panel_two.btn.Bind(wx.EVT_BUTTON, self.show_title)
        self.panel_two.Hide()

        self.Centre()
        #centers object in frame


        #shows panel name and .show
        #takes current frame and names it and .hide
        #if its not hidden then get value of it


    #each function shows next frame, hides current frame and sets layout
    def show_t_player(self, event):
        self.twoplayer.Show()
        self.title_screen.Hide()
        self.Layout()

    def show_s_player(self, event):
        self.oneplayer.Show()
        self.title_screen.Hide()
        self.Layout()

    def show_snake_titile(self, event):
        self.snake.Show()
        self.oneplayer.Hide()
        self.Layout()

    def show_title_snake(self, event):
        self.title_screen.Show()
        self.snake.Hide()
        self.Layout()

    def show_title_tertis(self, event):
        self.title_screen.Show()
        self.tetris.Hide()
        self.Layout()

    def show_memory_title(self, event):
        self.memory.Show()
        self.oneplayer.Hide()
        self.Layout()

    def show_title_memory(self, event):
        self.title_screen.Show()
        self.memory.Hide()
        self.Layout()

    def show_title_pong(self, event):
        self.title_screen.Show()
        self.pong.Hide()
        self.Layout()

    def run_snake(self, event):
        with open(self.resource_path("SnakeProject2.py")) as f:
            code = compile(f.read(), self.resource_path("SnakeProject2.py"), 'exec')
            exec(code, globals(), globals())

    def run_pong(self, event):
        with open(self.resource_path("pingpong.py")) as f:
            code = compile(f.read(), self.resource_path("pingpong.py"), 'exec')
            exec(code, globals(), globals())

    def run_memory(self, event):
        with open(self.resource_path("memory.py")) as f:
            code = compile(f.read(), self.resource_path("memory.py"), 'exec')
            exec(code, globals(), globals())

    def run_tetris(self, event):
        with open(self.resource_path("tetris.py")) as f:
            code = compile(f.read(), self.resource_path("tetris.py"), 'exec')
            exec(code, globals(), globals())

#    def run_rockpaper(self, event):
#        with open(self.resource_path("rps.py")) as f:
#            code = compile(f.read(), self.resource_path("rps.py"), 'exec')
#            exec(code, globals(), globals())
    #run file functions retreive file path and reads file, setting all variables to global
    # so main script has access

    def show_title(self, event):
        self.title_screen.Show()
        self.panel_two.Hide()
        self.Layout()

#    def show_title_rock(self, event):
#        self.title_screen.Show()
#        self.rockpaper.Hide()
#        self.Layout()

#    def show_rock(self, event):
#        self.rockpaper.Show()
#        self.twoplayer.Hide()
#        self.Layout()

    def show_tetris_title(self, event):
        self.tetris.Show()
        self.oneplayer.Hide()
        self.Layout()

    def show_pong_title(self, event):
        self.pong.Show()
        self.oneplayer.Hide()
        self.Layout()

    def show_sp_title(self, event):
        self.title_screen.Show()
        self.oneplayer.Hide()
        self.Layout()

    def show_tp_title(self, event):
        self.title_screen.Show()
        self.twoplayer.Hide()
        self.Layout()

    def show_hang(self, event):
        self.oneplayer.Hide()
        self.hangman.Show()
        self.Layout()

    def show_title_hang(self, event):
        self.hangman.Hide()
        self.title_screen.Show()
        self.Layout()

    def show_tic_title(self, event):
        self.twoplayer.Hide()
        self.panel_one.Show()
        self.Layout()

    def show_tic_game(self, event):
        self.panel_two.Show()
        self.panel_one.Hide()
        self.Layout()

    def resource_path(self, relative_path):
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)

if __name__ == "__main__":
    app = wx.App(False)
    frame = Frame()
    frame.Show()
    app.MainLoop()
        #creates frame object and shows, app in mainloop to keep running and displaying
