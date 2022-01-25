def shell():
    wt = get_weight()
    oat = get_temp()
    pa = get_alt()
    rfc = get_rolling_friction()
    bc = get_braking_friction()
    windmag = get_wind_mag()
    winddir = get_wind_dir()
    rwdir = get_runway_dir()

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
            if windmag not in range(0,11):
                print('Wind speed must be between 0 and 10.')
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
    shell()