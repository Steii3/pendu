

def ascii_switch(vie):
    switcher = {
        10: '''








====================
            ''',
        9: '''
   ||
   ||
   ||
   ||
   ||
   ||
  /||
 //||
====================''',
        8: '''  
  ,==========Y===
   ||       
   ||      
   ||      
   ||      
   ||       
   ||
  /||
 //||
====================''',
        7: '''
  ,==========Y===
   ||  /     
   || /     
   ||/      
   ||      
   ||       
   ||
  /||
 //||
====================''',
        6: '''  
  ,==========Y===
   ||  /      |
   || /       |
   ||/        
   ||        
   ||        
   ||
  /||
 //||
====================''',
        5: '''
  ,==========Y===
   ||  /      |
   || /       |
   ||/        O
   ||        
   ||        
   ||
  /||
 //||
====================''',
        4: '''  
  ,==========Y===
   ||  /      |
   || /       |
   ||/        O
   ||         |
   ||        
   ||
  /||
 //||
====================''',
        3: '''  
  ,==========Y===
   ||  /      |
   || /       |
   ||/        O
   ||        /|
   ||        
   ||
  /||
 //||
====================''',
        2: '''  
  ,==========Y===
   ||  /      |
   || /       |
   ||/        O
   ||        /|\\
   ||        
   ||
  /||
 //||
==================== ''',
        1: '''  
  ,==========Y===
   ||  /      |
   || /       |
   ||/        O
   ||        /|\\
   ||        /
   ||
  /||
 //||
====================''',
        0: '''  
  ,==========Y===
   ||  /      |
   || /       |
   ||/        O
   ||        /|\\
   ||        / \\
   ||
  /||
 //||
====================''' 

    }
    return switcher.get(vie,"erreur dans la saisie de la fonction de switch ascii")
