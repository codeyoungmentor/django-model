from django.db import models

class LinearRegression(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    @staticmethod
    def fit( X_train , y_train):
        return X_train + y_train
    
    @staticmethod
    def line_equation(m , b):
        return f"y = {m}x + {b}"
