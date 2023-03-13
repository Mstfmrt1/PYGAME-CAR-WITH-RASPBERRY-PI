from motormodul import MOTOR
import getkeyboardpress as kp

motor1=MOTOR(2,3,4,18,14,15) #MOTOR SINIFINDAN MOTOR 1 OBJesi OLUşturuyoruz
kp.init()

def main():
    if kp.getkey("UP"):
        motor1.move(0.6,0,0.1)
    elif kp.getkey("DOWN"):
        motor1.move(-0.6,0,0.1)    
    elif kp.getkey("LEFT"):
        motor1.move(0.6,0.3,0.1)
    elif kp.getkey("RIGHT"):
        motor1.move(0.6,-0.3,0.1)  
        
    else:
       motor1.stop(0.1)

if __name__=='__main__':
   
    while True:
        main()
    
