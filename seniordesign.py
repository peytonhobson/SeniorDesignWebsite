def take_off_distance():
    # get inputs
    wt = get_weight()
    oat = get_temp()
    pa = get_alt()
    rfc = get_rolling_friction()
    windmag = get_wind_mag()
    winddir = get_wind_dir()
    rwdir = get_runway_dir()

    # logic
    # equation 1
    import numpy as np
    from scipy.interpolate import interp2d
    xdatac = np.array([-40, -20, 0, 20, 40])
    ydatac = np.array([0, 500, 1000, 1500, 2000])
    zdatam = np.array([[3.76,4.14,4.57,5.29,6.52], [4.29,4.67,5.19,6.00,7.57], [4.86,5.29,5.90,6.90,8.76], [5.57,6.00,6.62,7.76,10.38],[6.29,6.90,7.67,9.00,11.81]])
    zinterp = interp2d(xdatac, ydatac, zdatam, kind='linear')
    gr0 = zinterp(oat,pa)

    # equation 2
    xdatac2 = np.array([5.07,7.46,10])
    ydatac2 = np.array([3800,4400,5000,5600])
    zdatam2 = np.array([[3.64,5.44,7.26], [5.07,7.46,10], [6.59,9.68,12.92], [8.59,12.8,17.1]])
    zinterp2 = interp2d(xdatac2, ydatac2, zdatam2, kind='linear')
    gr1 = zinterp(gr0,wt)

    # equation 3
    import math
    head_wind = windmag * math.cos((winddir-rwdir)*math.pi/180)
    xdatac3 = np.array([5.07,7.57,10,12.53,15.01])
    ydatac3 = np.array([-10,0,10])
    zdatam3 = np.array([[7.2,11.01,14.8,18.53,22],[5.07,7.57,10,12.53,15.01],[3.41,5.12,6.75,8.53,10.21]])
    zinterp3 = interp2d(xdatac3, ydatac3, zdatam3, kind='linear')
    gr2 = zinterp(gr1,head_wind)

    # equation 4
    xdatac4 = np.array([.04,.08,.12,.16])
    ydatac4 = np.array([5.05,7.43,9.9,12.55])
    zdatam4 = np.array([[5.05,5.9,7.08,9],[7.43,8.85,10.73,13.5],[9.9,11.85,14.2,18],[12.55,14.78,17.9,22.55]])
    zinterp4 = interp2d(xdatac4, ydatac4, zdatam4, kind='linear')
    gr3 = zinterp(rfc,gr2)

    to_ground_run = gr3*100
    print(f'Take off ground run is {to_ground_run} meters.')




def get_weight():
    while True:
        weight = 0
        try:
            weight = int(input('Enter weight in kg: '))
        except:
            print('Error: input must be number. Try again.')
        else:
            if weight not in range(3800,5601):
                print('Weight must be between 3,800 and 5,600 kg.')
            else:
                break
    return weight

def get_temp():
    while True:
        oat = 0
        try:
            oat = int(input('Enter temperature(Celsius): '))
        except:
            print('Error: input must be number. Try again.')
        else:
            if oat not in range(-40,41):
                print('Temperature must be between -40 and 40.')
            else:
                break
    return oat

def get_alt():
    while True:
        pa = 0
        try:
            pa = int(input('Enter altitude in meters: '))
        except:
            print('Error: input must be number. Try again.')
        else:
            if pa not in range(0,2001):
                print('Altitude must be between 0 and 2,000.')
            else:
                break
    return pa

def get_rolling_friction():
    while True:
        rfc = 0
        try:
            rfc = float(input('Enter rolling friction coefficient: '))
        except:
            print('Error: input must be number. Try again.')
        else:
            if rfc < .04 or rfc > .16:
                print('RFC must be between .04 and .16.')
            else:
                break
    return rfc

def get_braking_friction():
    while True:
        bc = 0
        try:
            bc = float(input('Enter braking friction coefficient: '))
        except:
            print('Error: input must be number. Try again.')
        else:
            if bc < .1 or bc > .4:
                print('Braking coefficient must be between .1 and .4.')
            else:
                break
    return bc

def get_wind_mag():
    while True:
        windmag = 0
        try:
            windmag = int(input('Enter wind speed(m/s): '))
        except:
            print('Error: input must be number. Try again.')
        else:
            if windmag not in range(0,21):
                print('Wind speed must be between 0 and 20.')
            else:
                break
    return windmag

def get_wind_dir():
    while True:
        winddir = 0
        try:
            winddir = int(input('Enter wind direction(N=0,E=90,S=180,W=270): '))
        except:
            print('Error: input must be number. Try again.')
        else:
            if winddir not in range(0,360):
                print('Wind direction must be between 0 and 359.')
            else:
                break
    return winddir

def get_runway_dir():
    while True:
        rwdir = 0
        try:
            rwdir = int(input('Enter runway direction(N=0,E=90,S=180,W=270): '))
        except:
            print('Error: input must be number. Try again.')
        else:
            if rwdir not in range(0,360):
                print('Runway direction must be between 0 and 359.')
            else:
                break
    return rwdir

if __name__ == '__main__':
    while True:
        choice = input('What are you trying to find?\n(t=take-off distance,s=take-off speed,a=accel-stop distance,\nr=landing reference speed,d=landing distance,g=ground run)\ntype q to quit: ')
        if choice == 't':
            take_off_distance()
        if choice == 'q':
            break