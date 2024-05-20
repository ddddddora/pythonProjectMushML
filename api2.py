from requests import get
length_leg = input('Введите length_leg = ')
diameter_hat = input('Введите diameter_hat = ')
thickness_leg = input('Введите thickness_leg = ')
print(get('http://localhost:5000/api_knnv2', json={'length_leg':length_leg,'diameter_hat':diameter_hat, 'thickness_leg':thickness_leg}).json())


length_leg = input('Введите length_leg = ')
diameter_hat = input('Введите diameter_hat = ')
thickness_leg = input('Введите thickness_leg = ')
print(get('http://localhost:5000/api_lrv2', json={'length_leg':length_leg,'diameter_hat':diameter_hat, 'thickness_leg':thickness_leg}).json())


length_leg = input('Введите length_leg = ')
diameter_hat = input('Введите diameter_hat = ')
thickness_leg = input('Введите thickness_leg = ')
print(get('http://localhost:5000/api_drv2', json={'length_leg':length_leg,'diameter_hat':diameter_hat, 'thickness_leg':thickness_leg}).json())

