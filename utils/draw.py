import matplotlib.pyplot as plt
import numpy as np

class Draw():
    def __init__(self, xDim, yDim):
        self.xDim = xDim
        self.yDim = yDim
        self.Figure = plt.figure(figsize = (xDim/yDim*8, 8))

    def Plot(self):
        plt.xlim(-2, self.xDim + 2)
        plt.ylim(-2, self.yDim + 2)
        plt.show(self.Figure)

    def SaveFig(self):
        plt.saveImg(self.Figure)

class VigaDraw(Draw):
    def __init__(self, xDim, yDim, cobrimento, diamEstribo):
        super().__init__(xDim, yDim)
        self.Height = yDim #cm
        self.Width = xDim #cm
        self.Cobrimento = cobrimento #cm
        self.DiamEstribo = diamEstribo #cm

    def DrawViga(self, printEstribo, printBarras):
        self.DrawRectangleViga()
        if (printEstribo):
            self.DrawEstribo()

    def DrawRectangleViga(self):
        plt.plot([0, 0], [0, self.Height], color = 'black')
        plt.plot([0, self.Width], [0, 0], color = 'black')
        plt.plot([0, self.Width], [self.Height, self.Height], color = 'black')
        plt.plot([self.Width, self.Width], [0, self.Height], color = 'black')

    def DrawEstribo(self):
        plt.plot([0, 0], [0, self.Height], color = 'red')
        plt.plot([0, self.Width], [0, 0], color = 'red')
        plt.plot([0, self.Width], [self.Height, self.Height], color = 'red')
        plt.plot([self.Width, self.Width], [0, self.Height], color = 'red')

    def DrawArmor(self, center, radius, color='black'):
        circle = plt.Circle(center, radius, color=color, fill=False)
        plt.gca().add_patch(circle)

    def DrawMultipleArmor(self, circles):
       for circle in circles:
        self.DrawArmor(*circle)

    def CalcArmorDistante(self, QuantBar, bitola):
        distUsal = self.xDim - 2*(self.DiamEstribo + self.Cobrimento)
        print(distUsal)