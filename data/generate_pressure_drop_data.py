import numpy as np
import pandas as pd

nos=2000

np.random.seed(42)

velocity=np.random.uniform(0.5,5.0,nos)
viscosity=np.random.uniform(0.001,0.005, nos)
density=np.random.uniform(800, 1000, nos)
diameter=np.random.uniform(0.05, 0.5, nos)
length=np.random.uniform(1, 50, nos)

friction_factor=np.random.uniform(0.01, 0.05, nos)

#Darcy-Weisbach equation
#Pressure Drop ΔP = f * (L / D) * (ρ * v^2 / 2)

pressure_drop=friction_factor*(length/diameter)*(density*(velocity**2)/2)

data=pd.DataFrame({
    'Velocity (v)': velocity,
    'Viscosity (µ)': viscosity,
    'Density (ρ)': density,
    'Diameter (D)': diameter,
    'Length (L)': length,
    #'Friction Factor': friction_factor,
    'Pressure Drop (ΔP)': pressure_drop
})

data_path='data/pressure_drop_data.csv'
data.to_csv(data_path, index=False)

print(f"Dataset successfully generated and saved to '{data_path}'!")
print(data.head())
