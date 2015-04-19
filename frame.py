__author__ = 'volodya'
import pandas as pd

def frame(num):
    name = 'provinces/vhi_id_' + str(num) + '.csv'
    df = pd.read_csv(name,index_col=False, header=1)
    df.columns = ['Year', 'Week', 'SMN','SMT','VegetationConditionIndex','ThermalConditionIndex','VegetationHealthIndex','AreaLess15','AreaLess35']
    print list(df.columns.values)
    print df

def minMaxProvince(num, year):
    name = 'provinces/vhi_id_' + str(num) + '.csv'
    df = pd.read_csv(name,index_col=False, header=1)
    result = df[df['year'] == year]
    minVHI = min(result.VHI)
    maxVHI = max(result.VHI)

    print(result.VHI)
    print("Min VHI = " + str(minVHI))
    print("Max VHI = " + str(maxVHI))

def droughtExtremal(num, percent):
    name = 'provinces/vhi_id_' + str(num) + '.csv'
    df = pd.read_csv(name,index_col=False, header=1)
    a = df[(df['%Area_VHI_LESS_15'] > percent)]
    print a.VHI

def drought(num, percent):
    name = 'provinces/vhi_id_' + str(num) + '.csv'
    df = pd.read_csv(name,index_col=False, header=1)
    a = df[(df['%Area_VHI_LESS_35'] > percent)]
    print a.VHI


drought("16", 0.19)