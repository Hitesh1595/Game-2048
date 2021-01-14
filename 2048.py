from tkinter import Frame, Label, CENTER

import Logics
import constant as c
# frame is superclass which in which we inherit widgets like cell button
class Game2048(Frame):
# when Game2048 is called all __init__ funtionality has been called and program runs 


    # frame is created below line
    # frame provide a functionality to add widget ,box etc
    def __init__(self):
        Frame.__init__(self)
        # frame has been created with the help of class

        self.grid()
        # thinter has a manager to form a frame like a grid(),a whole grid
        self.master.title('2048')
        self.master.bind("<Key>", self.key_down)
        # frame is binded by master if any key is pressed in Frame key.down happen

        self.commands = {c.KEY_UP: Logics.move_up, c.KEY_DOWN: Logics.move_down,
                        c.KEY_LEFT: Logics.move_left, c.KEY_RIGHT: Logics.move_right}
                        
        # created a grid cells
        self.grid_cells = []
        # add the grid cells
        self.init_grid()
        # add the grid cells
        self.init_matrix()
        # start the game and initial steps like add 2's 
        self.update_grid_cells()
        # background colour and font colour need to changed when number updates
        # sets the colour acc to no
        
        # frame has been created and game can run continous
        self.mainloop()
        # frame can run 


    def init_grid(self):
        # inside a frame create a  another frame with given dimension
        background = Frame(self, bg=c.BACKGROUND_COLOUR_GAME, width=c.SIZE, height=c.SIZE)
        # visualise backgroud as a grid
        background.grid()
        # creation of cells that is 16 cells
        for i in range(c.GRID_LEN):
            grid_row = []
            for j in range(c.GRID_LEN):
                # creation of cells inside a frame inside Frame
                cell = Frame(background, bg=c.BACKGROUND_COLOUR_CELL_EMPTY,
                              width=c.SIZE / c.GRID_LEN,
                              height=c.SIZE / c.GRID_LEN)

                cell.grid(row=i, column=j, padx=c.GRID_PADDING, pady=c.GRID_PADDING)
                    # create a space padding around a gridcells 10x10
                t = Label(master=cell, text="", bg=c.BACKGROUND_COLOUR_CELL_EMPTY,
                          justify=CENTER, font=c.FONT, width=4, height=2)
                # inside a cell there is label as master is cell
                # inside a cell colour and digit will be changed

                t.grid()
                grid_row.append(t)

            self.grid_cells.append(grid_row)
            # appending of labels as l1,l2,l3,l4...S

    def init_matrix(self):
        self.matrix = Logics.start_game()
        Logics.add_new_2(self.matrix)
        Logics.add_new_2(self.matrix)

    def update_grid_cells(self):
        for i in range(c.GRID_LEN):
            for j in range(c.GRID_LEN):
                new_number = self.matrix[i][j]
                if new_number == 0:
                    self.grid_cells[i][j].configure(text="", bg=c.BACKGROUND_COLOUR_CELL_EMPTY)
                    # update of bg colour if 0 is found 
                else:
                    self.grid_cells[i][j].configure(text=str(new_number),
                    bg=c.BACKGROUND_COLOUR_DICT[new_number],
                    fg=c.CELL_COLOUR_DICT[new_number])
                    # update colour as per constant file (number,background colour)
        self.update_idletasks()
        # wait till all colour are changed

    def key_down(self, event):
        # self -> object is called,event as key is pressed like a,s,d,w
        key = repr(event.char)
        if key in self.commands:
        # if only a,s,d,w is pressed
            self.matrix, changed = self.commands[repr(event.char)](self.matrix)
            if changed:
                Logics.add_new_2(self.matrix)
                self.update_grid_cells()
                changed = False
                if Logics.get_current_state(self.matrix) == 'WON':
                    self.grid_cells[1][1].configure(text="YOU",
                            bg=c.BACKGROUND_COLOUR_CELL_EMPTY)
                    
                    self.grid_cells[1][2].configure(text="WIN",
                            bg=c.BACKGROUND_COLOUR_CELL_EMPTY)
                if Logics.get_current_state(self.matrix) == "LOST":
                    self.grid_cells[1][1].configure(text="YOU",
                            bg=c.BACKGROUND_COLOUR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(text="LOSE",
                            bg=c.BACKGROUND_COLOUR_CELL_EMPTY)

gamegrid = Game2048()


                    
                



                           
  