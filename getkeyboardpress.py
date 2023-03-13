import pygame,sys

def init():
    pygame.init()
    window=pygame.display.set_mode((300,300))
    pygame.display.set_caption('motorkontrol')
    


def getkey(tus):
    ans=False
    for event in pygame.event.get():
         keyinput=pygame.key.get_pressed()
         basılantus=getattr(pygame,'K_{}'.format(tus))#
         if keyinput [basılantus]:
            ans=True
            
    pygame.display.update()  
    return ans
    
# def main():
#     if getkey("a"):
#         print("a tuşuna basıldı")
#     if getkey("LEFT"):
#         print("LEFT tuşuna basıldı")
            
        
    
# if __name__=='__main__':
#     init()
#     while True:
#         main()
    

    
    
   
    