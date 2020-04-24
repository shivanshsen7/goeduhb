# pattern 1
"""
 ****                                                                  

*                                                                      

*                                                                      

 ***                                                                   

    *                                                                  

    *                                                                  

****
"""
# pattern 2
"""
 ooooooooooooooooo                                                       
ooooooooooooooooo                                                       
ooooooooooooooooo                                                       
oooo                                                                    
oooo                                                                    
oooo                                                                    
ooooooooooooooooo                                                       
ooooooooooooooooo                                                       
ooooooooooooooooo                                                       
             oooo                                                       
             oooo                                                       
             oooo                                                       
ooooooooooooooooo                                                       
ooooooooooooooooo                                                       
ooooooooooooooooo
"""

just = ('<','<','<','^','>','>','<',)
pat1 = ('*'*4, '*', '*', '*'*3, '*', '*', '*'*4)
for x in range(7):
    print('{:{}5s}'.format(pat1[x], just[x]))


just = ('>', '<', '<', '<', '<', '<', '<', '<', '<',
        '>', '>', '>', '<', '<', '<',)
pat2 = ('o'*18, 'o'*19, 'o'*19, 'o'*4, 'o'*4, 'o'*4, 'o'*19, 'o'*19, 'o'*19,
     'o'*4, 'o'*4, 'o'*4, 'o'*19, 'o'*19, 'o'*19)
for x in range(28):
    print('{:{}19s}'.format(pat2[x], just[x]))
